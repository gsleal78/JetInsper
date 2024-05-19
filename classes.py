import pygame  # Importa a biblioteca Pygame para desenvolvimento de jogos
import random  # Importa o módulo random para gerar números aleatórios
from config import HEIGHT, WIDTH, moedas_coletadas  # Importa variáveis do arquivo config
from imagens_sons import sons, imagens_classes, variaveis_dimensoes  # Importa sons, imagens e dimensões das variáveis do arquivo imagens_sons

# Grupos de sprites
all_sprites = pygame.sprite.Group()  # Grupo para todos os sprites
all_bullets = pygame.sprite.Group()  # Grupo para todos os tiros
all_moedas = pygame.sprite.Group()  # Grupo para todas as moedas
lasersprite = pygame.sprite.Group()  # Grupo para todos os lasers
raposasprite = pygame.sprite.Group()  # Grupo para todas as raposas
bobsprite = pygame.sprite.Group()  # Grupo para todos os Bobs

class Barry(pygame.sprite.Sprite):  # Define a classe Barry (Prof Resina no jogo)
    def __init__(self, img, x, y, moedas_coletadas):
        pygame.sprite.Sprite.__init__(self)  # Inicializa o Sprite
        self.image = img  # Define a imagem do sprite
        self.rect = self.image.get_rect()  # Define o retângulo de colisão baseado na imagem
        self.rect.x = x  # Define a posição x inicial do sprite
        self.rect.y = y  # Define a posição y inicial do sprite
        self.rect.bottom = y + 75  # Define a posição inferior do retângulo
        self.speedx = 0  # Velocidade inicial em x
        self.speedy = 0  # Velocidade inicial em y
        self.last_shot = pygame.time.get_ticks()  # Tempo do último tiro disparado
        self.shoot_delay = 75  # Intervalo entre tiros
        self.shooting = False  # Vai verificar se está atirando
        self.moedas_coletadas = moedas_coletadas  # Número de moedas coletadas
        self.mask = pygame.mask.from_surface(self.image)  # Máscara de colisão

    def update(self):  # Método para atualizar o estado do sprite
        self.rect.x += self.speedx  # Atualiza a posição x
        self.rect.y -= self.speedy  # Atualiza a posição y
        if self.rect.bottom > HEIGHT:  # Verifica se o sprite está fora da tela (parte inferior)
            self.rect.bottom = HEIGHT
        elif self.rect.top < 0:  # Verifica se o sprite está fora da tela (parte superior)
            self.rect.top = 0
        if self.shooting and pygame.time.get_ticks() - self.last_shot > self.shoot_delay:  # Verifica se deve atirar
            self.shoot()

    def shoot(self):  # Método para atirar
        new_bullet = Tiro(imagens_classes["TIRO"], self.rect.bottom + 75, self.rect.centerx)  # Cria um novo tiro
        all_sprites.add(new_bullet)  # Adiciona o tiro ao grupo de todos os sprites
        all_bullets.add(new_bullet)  # Adiciona o tiro ao grupo de tiros
        self.last_shot = pygame.time.get_ticks()  # Atualiza o tempo do último tiro

class Tiro(pygame.sprite.Sprite):  # Define a classe Tiro
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)  # Inicializa o Sprite
        self.image = img  # Define a imagem do tiro
        self.rect = self.image.get_rect()  # Define o retângulo de colisão baseado na imagem
        self.rect.centerx = centerx  # Define a posição x central do tiro
        self.rect.bottom = bottom  # Define a posição y inferior do tiro
        self.speedy = 10  # Define a velocidade do tiro

    def update(self):  # Método para atualizar o estado do tiro
        self.rect.y += self.speedy  # Atualiza a posição y do tiro
        if self.rect.bottom < 0:  # Verifica se o tiro está fora da tela
            self.kill()  # Remove o tiro do jogo

class Moeda(pygame.sprite.Sprite):  # Define a classe Moeda
    def __init__(self, img, x, y, velocidade):
        pygame.sprite.Sprite.__init__(self)  # Inicializa o Sprite
        self.image = img  # Define a imagem da moeda
        self.rect = self.image.get_rect()  # Define o retângulo de colisão baseado na imagem
        self.rect.x = x  # Define a posição x inicial da moeda
        self.rect.y = y  # Define a posição y inicial da moeda
        self.velocidade = velocidade  # Define a velocidade da moeda
        self.mask = pygame.mask.from_surface(self.image)  # Máscara de colisão

    def update(self):  # Método para atualizar o estado da moeda
        self.rect.x -= self.velocidade  # Atualiza a posição x da moeda
        if self.rect.right < 0:  # Verifica se a moeda está fora da tela
            self.kill()  # Remove a moeda do jogo

class Laser(pygame.sprite.Sprite):  # Define a classe Laser
    def __init__(self, img, x, y, velocidade):
        pygame.sprite.Sprite.__init__(self)  # Inicializa o Sprite
        self.image = img  # Define a imagem do laser
        self.rect = self.image.get_rect()  # Define o retângulo de colisão baseado na imagem
        self.rect.x = x  # Define a posição x inicial do laser
        self.rect.bottom = y  # Define a posição y inferior do laser
        self.velocidade = velocidade  # Define a velocidade do laser
        self.mask = pygame.mask.from_surface(self.image)  # Máscara de colisão

    def update(self):  # Método para atualizar o estado do laser
        self.rect.x -= self.velocidade  # Atualiza a posição x do laser
        if self.rect.right < 0:  # Verifica se o laser está fora da tela
            self.kill()  # Remove o laser do jogo

# Cria uma instância do sprite Barry
voando = Barry(imagens_classes["BARRY"], 50, 750, moedas_coletadas)
all_sprites.add(voando)  # Adiciona o sprite Barry ao grupo de todos os sprites

class Raposa(pygame.sprite.Sprite):  # Define a classe Raposa
    def __init__(self, img, velocidade, x, y):
        pygame.sprite.Sprite.__init__(self)  # Inicializa o Sprite
        self.image = img  # Define a imagem da raposa
        self.rect = self.image.get_rect()  # Define o retângulo de colisão baseado na imagem
        self.rect.x = x  # Define a posição x inicial da raposa
        self.rect.bottom = y  # Define a posição y inferior da raposa
        self.velocidade = velocidade  # Define a velocidade da raposa
        self.mask = pygame.mask.from_surface(self.image)  # Máscara de colisão

    def update(self):  # Método para atualizar o estado da raposa
        self.rect.x -= self.velocidade  # Atualiza a posição x da raposa
        if self.rect.right < 0:  # Verifica se a raposa está fora da tela
            self.kill()  # Remove a raposa do jogo

class Bob(pygame.sprite.Sprite):  # Define a classe Bob
    def __init__(self, img, velocidade, x, y):
        pygame.sprite.Sprite.__init__(self)  # Inicializa o Sprite
        self.image = img  # Define a imagem do Bob
        self.rect = self.image.get_rect()  # Define o retângulo de colisão baseado na imagem
        self.rect.x = x  # Define a posição x inicial do Bob
        self.rect.bottom = y  # Define a posição y inferior do Bob
        self.velocidade = velocidade  # Define a velocidade do Bob
        self.mask = pygame.mask.from_surface(self.image)  # Máscara de colisão

    def update(self):  # Método para atualizar o estado do Bob
        self.rect.x -= self.velocidade  # Atualiza a posição x do Bob
        if self.rect.right < 0:  # Verifica se o Bob está fora da tela
            self.kill()  # Remove o Bob do jogo
