import pygame
import random
from definindo_imagens import imagens,variaveis_dimensoes,WIDTH,HEIGHT

TIRO = imagens["tiro_img"]
BARRY = imagens["barry_v_img"]
LASER1 = imagens["CHOQUE1_img"]
LASER2 = imagens["CHOQUE2_img"]
LASER_LISTA = [LASER1, LASER2]

moedas_coletadas = 0
num_conjuntos = 1

# Carrega os sons do jogo
pygame.mixer.music.load('assets/snd/Jetpack Joyride OST 🎼🎹 - Main Theme.mp3')
pygame.mixer.music.set_volume(0.4)
coin_sound = pygame.mixer.Sound('assets/snd/Mario Som Moedas ♪ 🔥🤑Olhe A Descrição 🤑🔥 (mp3cut.net).mp3')

all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
lasersprite = pygame.sprite.Group()
all_moedas = pygame.sprite.Group()

class barry(pygame.sprite.Sprite):
    def __init__(self, img, x, y, moedas_coletadas):
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
        self.moedas_coletadas = moedas_coletadas  # A quantidade de moedas coletadas é passada como parâmetro

        # Criar uma máscara de colisão precisa
        self.mask = pygame.mask.from_surface(self.image)

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
        new_bullet = tiro(TIRO, self.rect.bottom + 75, self.rect.centerx)
        all_sprites.add(new_bullet)
        all_bullets.add(new_bullet)
        self.last_shot = pygame.time.get_ticks()

voando = barry(BARRY, 50, 750, moedas_coletadas)  # Passando moedas_coletadas como parâmetro
all_sprites.add(voando)

class tiro(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Moeda(pygame.sprite.Sprite):
    def __init__(self, img, x, y, velocidade):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade = velocidade

    def update(self):
        self.rect.x -= self.velocidade  # Movimento para a esquerda
        if self.rect.right < 0:  # Se a moeda sair completamente da tela
            self.kill()  # Remover a moeda

        if pygame.sprite.collide_mask(self, voando):
            voando.moedas_coletadas += 1  # Aumenta a contagem de moedas
            self.kill()  # Remove a moeda
            coin_sound.play()

def criar_moedas(velocidade):
    for _ in range(num_conjuntos):
        # Posição aleatória do centro do grupo de moedas
        center_x = random.randint(WIDTH, WIDTH + 200)
        center_y = random.randint(100 + 3 * variaveis_dimensoes["MOEDAS_HEIGHT"], HEIGHT - 100 - 3 * variaveis_dimensoes["MOEDAS_HEIGHT"])

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
            (center_x - 20 - 2 * variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x + 20 + 2 * variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x - 20 - 2 * variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
            (center_x + 20 + 2 * variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
            (center_x - 20 - 3 * variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x + 20 + 3 * variaveis_dimensoes["MOEDAS_WIDTH"], center_y - 20),
            (center_x - 20 - 3 * variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
            (center_x + 20 + 3 * variaveis_dimensoes["MOEDAS_WIDTH"], center_y + 20),
        ]

        # Verificar se alguma posição coincide com a posição do laser
        for laser in lasersprite:
            for pos in positions:
                if laser.rect.collidepoint(pos):
                    break
            else:
                continue
            break
        else:
            # Criando as moedas nas posições calculadas
            for pos in positions:
                moeda = Moeda(imagens["MOEDAS_img"], *pos, velocidade)
                all_moedas.add(moeda)

class Laser(pygame.sprite.Sprite):
    def __init__(self, img, velocidade):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH + 200)
        self.rect.bottom = random.randint(100 + variaveis_dimensoes["CHOQUE_HEIGHT"], HEIGHT)
        self.velocidade = velocidade

        # Criar uma máscara de colisão precisa
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= self.velocidade  # Movimento para a esquerda
        if self.rect.right < 0:  # Se o laser sair completamente da tela
            self.kill()  # Remover o laser

        # Verificar colisão com as moedas
        colisoes = pygame.sprite.spritecollide(self, all_moedas, False)
        if colisoes:
            for colisao in colisoes:
                colisao.kill()  # Remover a moeda

        # Verificar colisão com o Barry
        if pygame.sprite.collide_mask(self, voando):
            global jogo_acabou
            jogo_acabou = True  # Parar o jogo se houver colisão


def criar_laser(velocidade):
    LASER = random.choice(LASER_LISTA)
    laser = Laser(LASER, velocidade)
    lasersprite.add(laser)


criar_laser_timer = pygame.time.get_ticks()

classes = {'barry':barry,
           'tiro':tiro,
           'Moeda':Moeda,
           'Laser':Laser}