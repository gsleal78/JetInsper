# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

# ----- Inicia assets
moeda_WIDTH = 50
moeda_HEIGHT = 38
laser_WIDTH = random.randint(200,400)
laser_HEIGHT = random.randint(200,500)
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/tela inicial.webp').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
moeda_img = pygame.image.load('assets/img/moeda.webp').convert_alpha()
moeda_img = pygame.transform.scale(moeda_img, (moeda_WIDTH, moeda_HEIGHT))
laser_img = pygame.image.load('assets/img/bolinhas_do_chao_2.png').convert_alpha()
laser_img = pygame.transform.scale(laser_img, (laser_WIDTH, laser_HEIGHT))
# ----- Inicia estruturas de dados Moedas
class Moeda(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Número de conjuntos de moedas desejados
num_conjuntos = 1

# Criando um grupo de moedas para cada conjunto
all_moedas = pygame.sprite.Group()

for _ in range(num_conjuntos):
    # Posição aleatória do centro do grupo de moedas
    center_x = random.randint(100 + 3*moeda_WIDTH, WIDTH - 100 - 3*moeda_WIDTH)
    center_y = random.randint(100 + 3*moeda_HEIGHT, HEIGHT - 100 - 3*moeda_HEIGHT)

    # Calcula as posições das moedas em torno do centro
    positions = [
        (center_x - 20, center_y - 20),
        (center_x + 20, center_y - 20),
        (center_x - 20, center_y + 20),
        (center_x + 20, center_y + 20),
        (center_x - 20 - moeda_WIDTH, center_y - 20),
        (center_x + 20 + moeda_WIDTH, center_y - 20),
        (center_x - 20 - moeda_WIDTH, center_y + 20),
        (center_x + 20 + moeda_WIDTH, center_y + 20),
        (center_x - 20 - 2*moeda_WIDTH, center_y - 20),
        (center_x + 20 + 2*moeda_WIDTH, center_y - 20),
        (center_x - 20 - 2*moeda_WIDTH, center_y + 20),
        (center_x + 20 + 2*moeda_WIDTH, center_y + 20),
        (center_x - 20 - 3*moeda_WIDTH, center_y - 20),
        (center_x + 20 + 3*moeda_WIDTH, center_y - 20),
        (center_x - 20 - 3*moeda_WIDTH, center_y + 20),
        (center_x + 20 + 3*moeda_WIDTH, center_y + 20),
    ]

    # Criando as moedas nas posições calculadas
    for pos in positions:
        moeda = Moeda(moeda_img, *pos)
        all_moedas.add(moeda)
#Inicia estrutura de dados Laser
class Laser(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH-laser_WIDTH)
        self.rect.bottom = random.randint (laser_HEIGHT,HEIGHT)
#criando laser
laser=Laser(laser_img)
lasersprite=pygame.sprite.Group()
lasersprite.add(laser)
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    if pygame.sprite.spritecollideany(laser, all_moedas):
        # Se houver colisão, move o laser para uma nova posição
        laser.rect.x = random.randint(0, WIDTH - laser_WIDTH)
        laser.rect.bottom = random.randint(laser_HEIGHT, HEIGHT)
    # ----- Gera saídas aleatórias
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando moedas
    all_moedas.draw(window)
    lasersprite.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados