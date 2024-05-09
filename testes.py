import pygame
import random

pygame.init()

WIDTH = 1200
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JetInsper')

from definindo_imagens import imagens, variaveis_dimensoes

game = True

clock = pygame.time.Clock()
FPS = 30

background = imagens["TESTLAB"]
BARRY = imagens["barry_v_img"]
TIRO = imagens["tiro_img"]

class barry(pygame.sprite.Sprite):
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
        new_bullet = tiro(TIRO, self.rect.bottom+75, self.rect.centerx)  
        all_sprites.add(new_bullet)  
        all_bullets.add(new_bullet)  
        self.last_shot = pygame.time.get_ticks()

class tiro(pygame.sprite.Sprite): 
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
voando = barry(BARRY, 50,750)
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

# Inicia estrutura de dados Laser
class Laser(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH + 200)
        self.rect.bottom = random.randint (100 + 3*variaveis_dimensoes["CHOQUE_HEIGHT"], HEIGHT - 100 - 3*variaveis_dimensoes["CHOQUE_HEIGHT"])

# Criando grupo de sprites para os lasers
lasersprite = pygame.sprite.Group()

# Variável para controlar a posição x do fundo
background_x = 0

# Variável para controlar o momento da última criação de laser
criar_laser_timer = pygame.time.get_ticks()

# Variável para controlar o momento da última criação de moedas
criar_moedas_timer = pygame.time.get_ticks()

# No loop principal
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                all_sprites.remove(voando)
                BARRY = imagens["barry_a_img"]
                voando = barry(BARRY, voando.rect.x, voando.rect.y)
                all_sprites.add(voando)
                voando.shooting = True
                voando.speedy = 20  # Reduz a velocidade vertical
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                all_sprites.remove(voando)
                BARRY = imagens["barry_v_img"]
                voando = barry(BARRY, voando.rect.x, voando.rect.y)
                all_sprites.add(voando)
                voando.speedy -= 20  # Reduz a velocidade vertical

    # Verificar se é hora de criar um novo conjunto de moedas
    if pygame.time.get_ticks() - criar_moedas_timer > 3000:  # 3000 milissegundos = 3 segundos
        criar_moedas()
        criar_moedas_timer = pygame.time.get_ticks()

    # Verificar se é hora de criar um novo laser
    if pygame.time.get_ticks() - criar_laser_timer > 5000:  # 5000 milissegundos = 5 segundos
        laser = Laser(imagens["CHOQUE1_img"])
        lasersprite.add(laser)
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

    all_moedas.update()  # Atualize a posição das moedas
    all_moedas.draw(window)  # Desenhe as moedas
    lasersprite.update()  # Atualize a posição dos lasers
    lasersprite.draw(window)  # Desenhe os lasers
    all_sprites.draw(window)  # Desenhe o personagem e os tiros

    pygame.display.update()  
    clock.tick(FPS)

pygame.quit()
