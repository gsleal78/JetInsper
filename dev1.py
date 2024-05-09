
import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JetInsper')

from definindo_imagens import imagens 

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
        self.shoot_delay = 150  # Intervalo de tempo entre os tiros (em milissegundos)
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
        new_bullet = tiro(TIRO, self.rect.bottom, self.rect.centerx)  # Criar um novo tiro
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
        self.speedy = 10

    def update(self): 
        self.rect.y += self.speedy
        if self.rect.bottom < 0:  
            self.kill()  

all_sprites = pygame.sprite.Group()
voando = barry(BARRY, 50,750/2)
all_sprites.add(voando)
all_bullets = pygame.sprite.Group()
    


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
    # Atualize a posição do personagem
    all_sprites.update()
    window.blit(background, (0,0))
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador
    clock.tick(FPS)
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
