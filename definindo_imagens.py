import pygame 
import random

#planos de fundo
WIDTH = 1200
HEIGHT = 750
background_i = pygame.image.load('assets/img/tela inicial.webp').convert()
background_i = pygame.transform.scale(background_i, (WIDTH, HEIGHT))
logo = pygame.image.load('assets/img/logo.webp').convert_alpha()
logo = pygame.transform.scale(logo, (WIDTH-200, HEIGHT-300))
TESTLAB = pygame.image.load('assets/img/plano de fundo testlab.webp').convert()
TESTLAB = pygame.transform.scale(TESTLAB, (WIDTH, HEIGHT))
FUNDOPEDRA = pygame.image.load('assets/img/plano de fundo pedra.webp').convert()
FUNDOPEDRA = pygame.transform.scale(FUNDOPEDRA, (WIDTH, HEIGHT))
FUNDOSELVA = pygame.image.load('assets/img/plano de fundo selva.webp').convert()
FUNDOSELVA = pygame.transform.scale(FUNDOSELVA, (WIDTH, HEIGHT))


#BARRY
BARRY_WIDTH = 100
BARRY_HEIGHT = 100
barry_img = pygame.image.load('assets/img/boneco_voando_normal.png').convert_alpha()
barry_img = pygame.transform.scale(barry_img, (BARRY_WIDTH, BARRY_HEIGHT))
barry_tiro_img = pygame.image.load('assets/img/Assim-que-ele-atira.webp').convert_alpha()

#TIRO
TIRO_WIDTH = 50
TIRO_HEIGHT = 70
tiro_img = pygame.image.load('assets/img/tiro.png').convert_alpha()
tiro_img = pygame.transform.scale(tiro_img,(TIRO_WIDTH,TIRO_HEIGHT))

#OBSTACULOS
MOEDAS_WIDTH = 50
MOEDAS_HEIGHT = 50
MOEDAS_IMG = pygame.image.load('assets/img/moeda.webp').convert_alpha()
MOEDAS_IMG = pygame.transform.scale(MOEDAS_IMG,(MOEDAS_WIDTH,MOEDAS_HEIGHT))
CHOQUE_WIDTH = 250
CHOQUE_HEIGHT = 250
CHOQUE1_IMG = pygame.image.load('assets/img/bolinhas do chao.webp').convert_alpha()
CHOQUE1_IMG = pygame.transform.scale(CHOQUE1_IMG,(CHOQUE_WIDTH,CHOQUE_HEIGHT))
CHOQUE2_IMG = pygame.image.load('assets/img/bolinhas_do_chao_2.png').convert_alpha()
CHOQUE2_IMG = pygame.transform.scale(CHOQUE2_IMG,(CHOQUE_WIDTH,CHOQUE_HEIGHT))
MISSIL_WIDTH = 300
MISSIL_HEIGHT = 150
MISSIL_IMG = pygame.image.load('assets/img/missil com fogo.png').convert_alpha()
MISSIL_IMG = pygame.transform.scale(MISSIL_IMG,(MISSIL_WIDTH,MISSIL_HEIGHT))


#ALERTAS 
ALERTA_I_WIDTH = 150
ALERTA_I_HEIGHT = 125
ALERTA_I_IMG = pygame.image.load('assets/img/alerta-inicial.png').convert_alpha()
ALERTA_I_IMG = pygame.transform.scale(ALERTA_I_IMG,(ALERTA_I_WIDTH,ALERTA_I_HEIGHT))
ALERTA_P_WIDTH = 150
ALERTA_P_HEIGHT = 125
ALERTA_P_IMG = pygame.image.load('assets/img/Alerta-chegando.png').convert_alpha()
ALERTA_P_IMG = pygame.transform.scale(ALERTA_P_IMG,(ALERTA_P_WIDTH,ALERTA_P_HEIGHT))



