import pygame
import random

pygame.init()

# Dimensões da janela
WIDTH = 1200
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JetInsper')

# Importando imagens e variáveis de dimensões
from definindo_imagens import imagens, variaveis_dimensoes

# Estado inicial do jogo
game_started = False

clock = pygame.time.Clock()
FPS = 30

# Carregamento das imagens
background_i = imagens["background_i"]
logo = imagens["logo"]
background = imagens["TESTLAB"]
BARRY = imagens["barry_v_img"]
TIRO = imagens["tiro_img"]

class Barry(pygame.sprite.Sprite):
    def __init__(self, img, x, y):  
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x  
        self.rect.y = y  
        self.rect.bottom = y + 75  
        self.speedx = 0
        self.speedy = 0
        self.last_shot = pygame.time.get_ticks()  
        self.shoot_delay = 75  
        self.shooting = False
        self.moedas_coletadas = 0  # Inicializa a contagem de moedas

    def update(self):
        self.rect.x += self.speedx
        self.rect.y -= self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        elif self.rect.top < 0:
            self.rect.top = 0
        if self.shooting and pygame.time.get_ticks() - self.last_shot > self.shoot_delay:
            self.shoot()

    def shoot(self):
        new_bullet = Tiro(TIRO, self.rect.bottom+75, self.rect.centerx)  
        all_sprites.add(new_bullet)  
        all_bullets.add(new_bullet)  
        self.last_shot = pygame.time.get_ticks()

class Tiro(pygame.sprite.Sprite): 
    def __init__(self,img, bottom, centerx): 
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 35

    def update(self): 
        self.rect.y += self.speedy
        if self.rect.bottom < 0:  
            self.kill()  

all_sprites = pygame.sprite.Group()
voando = Barry(BARRY, 50,750)
all_sprites.add(voando)
all_bullets = pygame.sprite.Group()

class Moeda(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 10  # Movimento para a esquerda
        if self.rect.right < 0:  # Se a moeda sair completamente da tela
            self.kill()  # Remover a moeda

        # Verificar colisão com o Barry
        if pygame.sprite.collide_mask(self, voando):
            voando.moedas_coletadas += 1  # Aumenta a contagem de moedas
            print("Moedas coletadas:", voando.moedas_coletadas)  # Imprime a quantidade de moedas coletadas
            self.kill()  # Remove a moeda

num_conjuntos = 1
all_moedas = pygame.sprite.Group()

# Função para criar um novo conjunto de moedas
def criar_moedas():
    for _ in range(num_conjuntos):
        # Posição aleatória do centro do grupo de moedas
        center_x = random.randint(WIDTH, WIDTH + 200)
        center_y = random.randint(100 + 3*variaveis_dimensoes["MOEDAS_HEIGHT"], HEIGHT - 100 - 3*variaveis_dimensoes["MOEDAS_HEIGHT"])

        # Calcula as posições das moedas em torno do centro
        positions = [
            (center_x - 20, center_y - 20),
            (center_x + 20, center_y - 20),
            (center_x - 20, center_y + 20),
            (center_x + 20, center_y + 20),
            (center_x - 20 - variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x + 20 + variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x - 20 - variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
            (center_x + 20 + variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
            (center_x - 20 - 2*variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x + 20 + 2*variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x - 20 - 2*variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
            (center_x + 20 + 2*variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
            (center_x - 20 - 3*variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x + 20 + 3*variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x - 20 - 3*variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
            (center_x + 20 + 3*variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
        ]

        # Criando as moedas nas posições calculadas
        for pos in positions:
            moeda = Moeda(imagens["MOEDAS_img"], *pos)
            all_moedas.add(moeda)

# Variável para controlar o tempo para criar novas moedas
criar_moedas_timer = pygame.time.get_ticks()

class Laser(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH + 200)
        self.rect.bottom = random.randint(0+variaveis_dimensoes["CHOQUE_HEIGHT"], HEIGHT)

    def update(self):
        self.rect.x -= 10  # Movimento para a esquerda
        if self.rect.right < 0:  # Se o laser sair completamente da tela
            self.kill()  # Remover o laser

lasersprite = pygame.sprite.Group()

# Função para criar um novo laser
def criar_laser():
    laser = Laser(imagens["CHOQUE1_img"])
    lasersprite.add(laser)

# Variável para controlar o tempo para criar novos lasers
criar_laser_timer = pygame.time.get_ticks()

# Variável para controlar a posição x do fundo
background_x = 0

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if not game_started and event.key == pygame.K_SPACE:  # Se o jogo ainda não começou e a tecla de espaço for pressionada
                game_started = True  # Começa o jogo
            elif game_started:
                if event.key == pygame.K_SPACE:
                    voando.shooting = True
                    voando.speedy = 20
            elif not game_started and event.key == pygame.K_SPACE:  # Se o jogo não começou e a tecla de espaço for pressionada
                game_started = True  # Começa o jogo

        elif event.type == pygame.KEYUP:
            if game_started and event.key == pygame.K_SPACE:
                voando.shooting = False
                voando.speedy -= 40  # Reduz a velocidade vertical

    if not game_started:  # Se o jogo não começou, continua na tela inicial
        window.blit(background_i, (0, 0))
        window.blit(logo, (WIDTH / 2 - logo.get_width() / 2, HEIGHT / 2 - logo.get_height() / 2))
        pygame.display.update()
        clock.tick(FPS)
        continue  # Volta ao início do loop para verificar eventos

    # Verificar se é hora de criar um novo conjunto de moedas
    if pygame.time.get_ticks() - criar_moedas_timer > 3000:  # 3000 milissegundos = 3 segundos
        criar_moedas()
        criar_moedas_timer = pygame.time.get_ticks()

    # Verificar se é hora de criar um novo laser
    if pygame.time.get_ticks() - criar_laser_timer > 5000:  # 5000 milissegundos = 5 segundos
        criar_laser()
        criar_laser_timer = pygame.time.get_ticks()

    # Atualize a posição do personagem
    all_sprites.update()

    # Atualize a posição x do fundo para movê-lo para a esquerda
    background_x -= 10

    # Verifique se o fundo original saiu completamente da tela
    if background_x <= -WIDTH:
        background_x = 0

    # Desenhe o fundo duas vezes para criar o efeito de loop infinito
    window.blit(background, (background_x, 0))
    window.blit(background, (background_x + WIDTH, 0))

    all_moedas.update()  
    all_moedas.draw(window)  
    lasersprite.update()  
    lasersprite.draw(window)  
    all_sprites.draw(window)   

    pygame.display.update()  
    clock.tick(FPS)

pygame.quit()
