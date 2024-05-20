import pygame  # Importa a biblioteca Pygame para desenvolvimento de jogos
from config import HEIGHT,moedas_coletadas  # Importa variáveis do arquivo config
from imagens_sons import imagens_classes  #Importa o dicionario contendo as imagens utilizadas para gerar o jogo

# Definindo os Grupos de sprites
all_sprites = pygame.sprite.Group() 
all_bullets = pygame.sprite.Group()
all_moedas = pygame.sprite.Group() 
lasersprite = pygame.sprite.Group()  
raposasprite = pygame.sprite.Group() 
bobsprite = pygame.sprite.Group()  

class Barry(pygame.sprite.Sprite):  # Define a classe Barry (Prof Resina no jogo)
    '''
    Classe para o jogador principal
    Define a posição, imagem, e numero de moedas coletadas, tiros que saem do personagem

    '''
    def __init__(self, img, x, y, moedas_coletadas):
        pygame.sprite.Sprite.__init__(self)  # Inicializa o Sprite
        self.image = img  # Define a imagem do sprite
        self.rect = self.image.get_rect()  #Define as coordenadas do retangulo da imagem

        #Definindo as posições iniciais em x,y e posição inferior do retangulo
        self.rect.x = x  
        self.rect.y = y  
        self.rect.bottom = y + 75  

        #definindo velocidades inicias 
        self.speedx = 0  
        self.speedy = 0 

        #criando timer e delay para os tiros 
        self.last_shot = pygame.time.get_ticks()  
        self.shoot_delay = 75 
        self.shooting = False  

        self.moedas_coletadas = moedas_coletadas  # Número de moedas coletadas
        self.mask = pygame.mask.from_surface(self.image)  # Máscara de colisão

    def update(self):  # Método para atualizar o estado do sprite
        #atualizando as posições
        self.rect.x += self.speedx  
        self.rect.y -= self.speedy  

        #verificando se o sprite saiu da tela
        if self.rect.bottom > HEIGHT:  
            self.rect.bottom = HEIGHT
        elif self.rect.top < 0:  
            self.rect.top = 0

        # Verifica se deve atirar
        if self.shooting and pygame.time.get_ticks() - self.last_shot > self.shoot_delay: 
            self.shoot()

     # Método para atirar, criando um novo tiro, adicionando-o para os grupos de sprites e reiniciando o timer
    def shoot(self): 
        new_bullet = Tiro(imagens_classes["TIRO"], self.rect.bottom + 75, self.rect.centerx)  
        all_sprites.add(new_bullet)  
        all_bullets.add(new_bullet)  
        self.last_shot = pygame.time.get_ticks()  

#Definindo uma classe para os tiros
class Tiro(pygame.sprite.Sprite):
    '''
    Classe para criar os tiros, seguindo o jogador
    '''
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 10

    #Atualiza a posição dos tiros e remove o tiro se ele chegar no final da tela
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


#Definindo uma classe para as moedas
class Moeda(pygame.sprite.Sprite):
    '''
    Classe para criar as moedas e torna-las coletáveis

    '''
    def __init__(self, img, x, y, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade = velocidade
        self.mask = pygame.mask.from_surface(self.image)

    #Atualiza a posição das moedas e remove o tiro se ele chegar no final da tela
    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()

#Definindo uma classe para os Lasers
class Laser(pygame.sprite.Sprite):
    '''
    Classe para criar os Laser 
    '''
    def __init__(self, img, x, y, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.velocidade = velocidade
        self.mask = pygame.mask.from_surface(self.image)
     #Atualiza a posição dos Lasers e remove o tiro se ele chegar no final da tela
    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()

# Cria uma instância do sprite Barry
voando = Barry(imagens_classes["BARRY"], 50, 750, moedas_coletadas)
all_sprites.add(voando)  # Adiciona o sprite Barry ao grupo de todos os sprites



#Definindo uma classe para as Raposas
class Raposa(pygame.sprite.Sprite):
    '''
    Classe para criar os Raposa 
    '''
    def __init__(self, img, velocidade, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.velocidade = velocidade
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()

#Definindo uma classe para os Bobs
class Bob(pygame.sprite.Sprite):
    '''
    Classe para criar os Bob
    '''
    def __init__(self, img, velocidade, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.velocidade = velocidade
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()
