import pygame
import random
from config import HEIGHT, WIDTH, moedas_coletadas
from imagens_sons import sons, imagens_classes,variaveis_dimensoes


# Grupos de sprites
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
all_moedas = pygame.sprite.Group()
lasersprite = pygame.sprite.Group()
raposasprite = pygame.sprite.Group()
bobsprite = pygame.sprite.Group()
class Barry(pygame.sprite.Sprite):
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
        self.moedas_coletadas = moedas_coletadas
        self.mask = pygame.mask.from_surface(self.image)  # Adicionada máscara de colisão

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
        new_bullet = Tiro(imagens_classes["TIRO"], self.rect.bottom + 75, self.rect.centerx)
        all_sprites.add(new_bullet)
        all_bullets.add(new_bullet)
        self.last_shot = pygame.time.get_ticks()

class Tiro(pygame.sprite.Sprite):
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
        self.mask = pygame.mask.from_surface(self.image)  # Adicionada máscara de colisão

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()

class Laser(pygame.sprite.Sprite):
    def __init__(self, img,x,y,velocidade):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.velocidade = velocidade
        self.mask = pygame.mask.from_surface(self.image)  # Adicionada máscara de colisão

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()


voando = Barry(imagens_classes["BARRY"], 50, 750, moedas_coletadas)
all_sprites.add(voando)


class Raposa(pygame.sprite.Sprite): 
    def __init__(self,img,velocidade,x,y): 
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.velocidade = velocidade
        self.mask = pygame.mask.from_surface(self.image)  # Adicionada máscara de colisão

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()

class Bob(pygame.sprite.Sprite): 
    def __init__(self,img,velocidade,x,y): 
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.velocidade = velocidade
        self.mask = pygame.mask.from_surface(self.image)  # Adicionada máscara de colisão

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()


