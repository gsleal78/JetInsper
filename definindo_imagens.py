import pygame 
import random

# Inicialização do Pygame


# Definição do tamanho da janela


#planos de fundo d


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
barry_v_img = pygame.image.load('assets/img/boneco_voando_normal.png').convert_alpha()
barry_v_img = pygame.transform.scale(barry_v_img, (BARRY_WIDTH, BARRY_HEIGHT))
barry_a_img = pygame.image.load('assets/img/Assim-que-ele-atira.png').convert_alpha()
barry_a_img = pygame.transform.scale(barry_a_img, (BARRY_WIDTH, BARRY_HEIGHT))

#CIENTISTA
CIENTISTA_WIDTH = 100
CIENTISTA_HEIGHT = 100
CIENTISTA_img = pygame.image.load('assets/img/cientista.png').convert_alpha()
CIENTISTA_img = pygame.transform.scale(CIENTISTA_img, (CIENTISTA_WIDTH, CIENTISTA_HEIGHT))


#TIRO
TIRO_WIDTH = 50
TIRO_HEIGHT = 70
tiro_img = pygame.image.load('assets/img/tiro.png').convert_alpha()
tiro_img = pygame.transform.scale(tiro_img,(TIRO_WIDTH,TIRO_HEIGHT))

#OBSTACULOS
MOEDAS_WIDTH = 50
MOEDAS_HEIGHT = 38
MOEDAS_img = pygame.image.load('assets/img/moeda.webp').convert_alpha()
MOEDAS_img = pygame.transform.scale(MOEDAS_img,(MOEDAS_WIDTH,MOEDAS_HEIGHT))
CHOQUE_WIDTH = random.randint(200,400)
CHOQUE_HEIGHT = random.randint(200,500)
CHOQUE1_img = pygame.image.load('assets/img/bolinhas do chao.webp').convert_alpha()
CHOQUE1_img = pygame.transform.scale(CHOQUE1_img,(CHOQUE_WIDTH,CHOQUE_HEIGHT))
CHOQUE2_img = pygame.image.load('assets/img/bolinhas_do_chao_2.png').convert_alpha()
CHOQUE2_img = pygame.transform.scale(CHOQUE2_img,(CHOQUE_WIDTH,CHOQUE_HEIGHT))
MISSIL_WIDTH = 300
MISSIL_HEIGHT = 150
MISSIL_img = pygame.image.load('assets/img/missil com fogo.png').convert_alpha()
MISSIL_img = pygame.transform.scale(MISSIL_img,(MISSIL_WIDTH,MISSIL_HEIGHT))


#ALERTAS 
ALERTA_I_WIDTH = 150
ALERTA_I_HEIGHT = 125
ALERTA_I_img = pygame.image.load('assets/img/alerta-inicial.png').convert_alpha()
ALERTA_I_img = pygame.transform.scale(ALERTA_I_img,(ALERTA_I_WIDTH,ALERTA_I_HEIGHT))
ALERTA_P_WIDTH = 150
ALERTA_P_HEIGHT = 125
ALERTA_P_img = pygame.image.load('assets/img/Alerta-chegando.png').convert_alpha()
ALERTA_P_img = pygame.transform.scale(ALERTA_P_img,(ALERTA_P_WIDTH,ALERTA_P_HEIGHT))



chaves = [
    background_i,
    logo,
    TESTLAB,
    FUNDOPEDRA,
    FUNDOSELVA,
    barry_v_img,
    barry_a_img,
    CIENTISTA_img,
    tiro_img,
    MOEDAS_img,
    CHOQUE1_img,
    CHOQUE2_img,
    MISSIL_img,
    ALERTA_I_img,
    ALERTA_P_img
]

imagens = {
    "background_i": background_i,
    "logo": logo,
    "TESTLAB": TESTLAB,
    "FUNDOPEDRA": FUNDOPEDRA,
    "FUNDOSELVA": FUNDOSELVA,
    "barry_v_img": barry_v_img,
    "barry_a_img": barry_a_img,
    "CIENTISTA_img": CIENTISTA_img,
    "tiro_img": tiro_img,
    "MOEDAS_img": MOEDAS_img,
    "CHOQUE1_img": CHOQUE1_img,
    "CHOQUE2_img": CHOQUE2_img,
    "MISSIL_img": MISSIL_img,
    "ALERTA_I_img": ALERTA_I_img,
    "ALERTA_P_img": ALERTA_P_img
}


