import pygame
import random

pygame.init()

WIDTH = 1200
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JetInsper')

from definindo_imagens import imagens,MOEDAS_HEIGHT,MOEDAS_WIDTH,CHOQUE_HEIGHT,CHOQUE_WIDTH

game = True

clock = pygame.time.Clock()
FPS = 30

background = imagens["TESTLAB"]
BARRY = imagens["barry_v_img"]
TIRO = imagens["tiro_img"]

class barry(pygame.sprite.Sprite):
    def __init__(self, img, x, y):  # Adicione x e y como parâmetros
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x  # Use x como posição x
        self.rect.y = y  # Use y como posição y
        self.rect.bottom = y + 75  # Atualize também a posição inferior
        self.speedx = 0
        self.speedy = 0
        self.last_shot = pygame.time.get_ticks()  # Último momento em que o personagem atirou
        self.shoot_delay = 75  # Intervalo de tempo entre os tiros (em milissegundos)
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
        new_bullet = tiro(TIRO, self.rect.bottom+75, self.rect.centerx)  # Criar um novo tiro
        all_sprites.add(new_bullet)  # Adicionar o novo tiro ao grupo de sprites
        all_bullets.add(new_bullet)  # Adicionar o novo tiro ao grupo de balas
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
num_conjuntos = 1
all_moedas = pygame.sprite.Group()

for _ in range(num_conjuntos):
    # Posição aleatória do centro do grupo de moedas
    center_x = random.randint(100 + 3*MOEDAS_WIDTH, WIDTH - 100 - 3*MOEDAS_WIDTH)
    center_y = random.randint(100 + 3*MOEDAS_HEIGHT, HEIGHT - 100 - 3*MOEDAS_HEIGHT)

    # Calcula as posições das moedas em torno do centro
    positions = [
        (center_x - 20, center_y - 20),
        (center_x + 20, center_y - 20),
        (center_x - 20, center_y + 20),
        (center_x + 20, center_y + 20),
        (center_x - 20 - MOEDAS_WIDTH, center_y - 20),
        (center_x + 20 + MOEDAS_WIDTH, center_y - 20),
        (center_x - 20 - MOEDAS_WIDTH, center_y + 20),
        (center_x + 20 + MOEDAS_WIDTH, center_y + 20),
        (center_x - 20 - 2*MOEDAS_WIDTH, center_y - 20),
        (center_x + 20 + 2*MOEDAS_WIDTH, center_y - 20),
        (center_x - 20 - 2*MOEDAS_WIDTH, center_y + 20),
        (center_x + 20 + 2*MOEDAS_WIDTH, center_y + 20),
        (center_x - 20 - 3*MOEDAS_WIDTH, center_y - 20),
        (center_x + 20 + 3*MOEDAS_WIDTH, center_y - 20),
        (center_x - 20 - 3*MOEDAS_WIDTH, center_y + 20),
        (center_x + 20 + 3*MOEDAS_WIDTH, center_y + 20),
    ]

    # Criando as moedas nas posições calculadas
    for pos in positions:
        moeda = Moeda(imagens["MOEDAS_img"], *pos)
        all_moedas.add(moeda)
#Inicia estrutura de dados Laser
class Laser(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH-CHOQUE_WIDTH)
        self.rect.bottom = random.randint (CHOQUE_HEIGHT,HEIGHT)
#criando laser
laser=Laser(imagens["CHOQUE1_img"])
lasersprite=pygame.sprite.Group()
lasersprite.add(laser)

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
                voando.shooting = False
    if pygame.sprite.spritecollideany(laser, all_moedas):
        # Se houver colisão, move o laser para uma nova posição
        laser.rect.x = random.randint(0, WIDTH - CHOQUE_WIDTH)
        laser.rect.bottom = random.randint(CHOQUE_HEIGHT, HEIGHT)
    # Atualize a posição do personagem
    all_sprites.update()
    window.blit(background, (0,0))
    all_sprites.draw(window)
    all_moedas.draw(window)
    lasersprite.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador
    clock.tick(FPS)
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
