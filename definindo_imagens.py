import pygame 
import random

#DIMENSÕES DA TELA 
WIDHT = 1200
HEIGHT = 750



#caminho da fonte do texto

caminho_fonte = "assets/fontes/PublicPixel-E447g.ttf"
minha_fonte = pygame.font.Font(caminho_fonte, 36)
texto_linha1 = "Aperte ENTER para"
texto_linha2 = "iniciar o jogo"
texto_renderizado1 = minha_fonte.render(texto_linha1, True, (0, 100, 255))
texto_renderizado2 = minha_fonte.render(texto_linha2, True, (0, 100, 255))
posicao_y_linha1 = HEIGHT // 2 - texto_renderizado1.get_height()
posicao_y_linha2 = HEIGHT // 2
minha_fonte = pygame.font.Font(caminho_fonte, 32)
texto_linha2_1 = "Aperte ESPACO para continuar jogando"
texto_linha2_2 = "ou ENTER para sair"
texto_renderizado2_1 = minha_fonte.render(texto_linha2_1, True, (0, 100, 255))
texto_renderizado2_2 = minha_fonte.render(texto_linha2_2, True, (0, 100, 255))
posicao_y_linha2_1 = HEIGHT // 2 - texto_renderizado2_1.get_height()
posicao_y_linha2_2 = HEIGHT // 2

textos = {
    "texto_renderizado1": texto_renderizado1,
    "texto_renderizado2": texto_renderizado2,
    "posicao_y_linha1": posicao_y_linha1,
    "posicao_y_linha2": posicao_y_linha2,
    "texto_renderizado2_1": texto_renderizado2_1,
    "texto_renderizado2_2": texto_renderizado2_2,
    "posicao_y_linha2_1": posicao_y_linha2_1,
    "posicao_y_linha2_2": posicao_y_linha2_2

}


#TEXTO MOEDAS
moeda_fonte = "assets/fontes/PressStart2P.ttf"
fonte_moeda = pygame.font.Font(moeda_fonte,56)


#planos de fundo 


WIDTH = 1200
HEIGHT = 750
background_i = pygame.image.load('assets/img/tela inicial.webp').convert()
background_i = pygame.transform.scale(background_i, (WIDTH, HEIGHT))
logo = pygame.image.load('assets/img/logoresina.png').convert_alpha()
logo = pygame.transform.scale(logo, (WIDTH-200, HEIGHT-300))
TESTLAB = pygame.image.load('assets/img/plano de fundo testlab.jpg').convert()
TESTLAB = pygame.transform.scale(TESTLAB, (WIDTH, HEIGHT))
FUNDOPEDRA = pygame.image.load('assets/img/fundo pedra fogo.png').convert()
FUNDOPEDRA = pygame.transform.scale(FUNDOPEDRA, (WIDTH, HEIGHT))
FUNDOSELVA = pygame.image.load('assets/img/plano de fundo selva.webp').convert()
FUNDOSELVA = pygame.transform.scale(FUNDOSELVA, (WIDTH, HEIGHT))
FUNDOFINAL = pygame.image.load('assets/img/fundo_final.jpg')
FUNDOFINAL = pygame.transform.scale(FUNDOFINAL, (WIDTH, HEIGHT))
IMAGEM_TRANSICAO_1 = pygame.image.load('assets/img/tela inicial.webp').convert()
IMAGEM_TRANSICAO_1 = pygame.transform.scale(IMAGEM_TRANSICAO_1, (WIDTH, HEIGHT))
IMAGEM_TRANSICAO_2 = pygame.image.load('assets/img/tela inicial.webp').convert()
IMAGEM_TRANSICAO_2 = pygame.transform.scale(IMAGEM_TRANSICAO_2, (WIDTH, HEIGHT))
background = background_i

#BARRY
BARRY_WIDTH = 100
BARRY_HEIGHT = 100
barry_v_img = pygame.image.load('assets/img/boneco_voando_normal.png').convert_alpha()
barry_v_img = pygame.transform.scale(barry_v_img, (BARRY_WIDTH, BARRY_HEIGHT))
barry_a_img = pygame.image.load('assets/img/Assim-que-ele-atira.png').convert_alpha()
barry_a_img = pygame.transform.scale(barry_a_img, (BARRY_WIDTH, BARRY_HEIGHT))
barry_ed_img = pygame.image.load('assets/img/BARRY CHOQUE deitado.png').convert_alpha()
barry_ed_img = pygame.transform.scale(barry_ed_img, (BARRY_WIDTH, BARRY_HEIGHT))
barry_ep_img = pygame.image.load('assets/img/BARRY CHOQUE.png').convert_alpha()
barry_ep_img = pygame.transform.scale(barry_ep_img, (BARRY_WIDTH, BARRY_HEIGHT))

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
CHOQUE_HEIGHT = 400
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




imagens = {
    "background_i": background_i,
    "logo": logo,
    "TESTLAB": TESTLAB,
    "FUNDOPEDRA": FUNDOPEDRA,
    "FUNDOSELVA": FUNDOSELVA,
    "FUNDOFINAL": FUNDOFINAL,
    "barry_v_img": barry_v_img,
    "barry_a_img": barry_a_img,
    "CIENTISTA_img": CIENTISTA_img,
    "tiro_img": tiro_img,
    "MOEDAS_img": MOEDAS_img,
    "CHOQUE1_img": CHOQUE1_img,
    "CHOQUE2_img": CHOQUE2_img,
    "MISSIL_img": MISSIL_img,
    "ALERTA_I_img": ALERTA_I_img,
    "ALERTA_P_img": ALERTA_P_img,
    "IMAGEM_TRANSICAO_2": IMAGEM_TRANSICAO_2,
    "IMAGEM_TRANSICAO_1": IMAGEM_TRANSICAO_1,
    "barry_ed_img": barry_ed_img,
    "barry_ep_img": barry_ep_img
}
variaveis_dimensoes = {
    "WIDTH": 1200,
    "HEIGHT": 750,
    "BARRY_WIDTH": 100,
    "BARRY_HEIGHT": 100,
    "CIENTISTA_WIDTH": 100,
    "CIENTISTA_HEIGHT": 100,
    "TIRO_WIDTH": 50,
    "TIRO_HEIGHT": 70,
    "MOEDAS_WIDTH": 50,
    "MOEDAS_HEIGHT": 38,
    "CHOQUE_WIDTH": random.randint(200, 400),
    "CHOQUE_HEIGHT": random.randint(200, 500),
    "MISSIL_WIDTH": 300,
    "MISSIL_HEIGHT": 150,
    "ALERTA_I_WIDTH": 150,
    "ALERTA_I_HEIGHT": 125,
    "ALERTA_P_WIDTH": 150,
    "ALERTA_P_HEIGHT": 125
}