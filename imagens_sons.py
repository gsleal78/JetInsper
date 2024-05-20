import pygame # Importa a biblioteca Pygame para criação do jogo
import random # Importa o módulo random para geração de números aleatórios
from config import HEIGHT, WIDTH # Importa as configurações de altura e largura da janela do jogo do arquivo config


# Carrega e configura os efeitos sonoros do jogo
pygame.mixer.music.load('assets/snd/Jetpack Joyride OST 🎼🎹 - Main Theme.mp3')
pygame.mixer.music.set_volume(0.4)  # Define o volume da música
coin_sound = pygame.mixer.Sound('assets/snd/Mario Som Moedas ♪ 🔥🤑Olhe A Descrição 🤑🔥 (mp3cut.net).mp3')
eletric_sound = pygame.mixer.Sound('assets/snd/eletrecutado.mp3')
som_morte = pygame.mixer.Sound('assets/snd/som morrendo.mp3')
som_tiro = pygame.mixer.Sound('assets/snd/Fortnite Scar Sound Effect (mp3cut.net).mp3')
hod_rider = pygame.mixer.Sound('assets/snd/hogrider.mp3')
som_bob = pygame.mixer.Sound('assets/snd/som_bob.mp3')

# Cria um dicionário para armazenar os efeitos sonoros
sons = {
    
    "coin_sound": coin_sound,
    "eletric_sound": eletric_sound,
    "som_morte": som_morte,
    "som_tiro": som_tiro,
    "hog_rider": hod_rider,
    "som_bob": som_bob
}


caminho_fonte = "assets/fontes/PublicPixel-E447g.ttf"  # Caminho para a fonte usada nos textos
minha_fonte = pygame.font.Font(caminho_fonte, 36)  # Cria uma fonte para exibir textos na tela

# Configura o texto para ser exibido na tela inicial do jogo
texto_linha1 = "Aperte ENTER para"
texto_linha2 = "iniciar o jogo"

# Renderiza o texto
texto_renderizado1 = minha_fonte.render(texto_linha1, True, (0, 100, 255))
texto_renderizado2 = minha_fonte.render(texto_linha2, True, (0, 100, 255))

# Define as posições do texto na tela
posicao_y_linha1 = HEIGHT // 2 - texto_renderizado1.get_height()
posicao_y_linha2 = HEIGHT // 2

minha_fonte = pygame.font.Font(caminho_fonte, 32)  # Cria uma nova fonte para outros textos

# Configura os textos para serem exibidos após o jogo ser parado por colisão entre o Barry (Resina) e um obstáculo
texto_linha2_1 = "Aperte ENTER para continuar jogando"
texto_linha2_2 = "ou ESC para sair"

# Renderiza os textos
texto_renderizado2_1 = minha_fonte.render(texto_linha2_1, True, (0, 100, 255))
texto_renderizado2_2 = minha_fonte.render(texto_linha2_2, True, (0, 100, 255))

# Define as posições do texto na tela
posicao_y_linha2_1 = HEIGHT // 2 - texto_renderizado2_1.get_height()
posicao_y_linha2_2 = HEIGHT // 2

# Dicionário para armazenar os textos e suas respectivas posições
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



# Carrega os planos de fundo do jogo
WIDTH = 1200
HEIGHT = 750
background_i = pygame.image.load('assets/img/tela inicial.webp').convert()
background_i = pygame.transform.scale(background_i, (WIDTH, HEIGHT))
logo = pygame.image.load('assets/img/logoresina.png').convert_alpha()
logo = pygame.transform.scale(logo, (WIDTH-200, HEIGHT-300))
TESTLAB = pygame.image.load('assets/img/plano de fundo testlab.jpg').convert()
TESTLAB = pygame.transform.scale(TESTLAB, (WIDTH, HEIGHT))
FUNDOSELVA = pygame.image.load('assets/img/plano de fundo selva.webp').convert()
FUNDOSELVA = pygame.transform.scale(FUNDOSELVA, (WIDTH, HEIGHT))
IMAGEM_TRANSICAO_1 = pygame.image.load('assets/img/tela inicial.webp').convert()
IMAGEM_TRANSICAO_1 = pygame.transform.scale(IMAGEM_TRANSICAO_1, (WIDTH, HEIGHT))
IMAGEM_TRANSICAO_2 = pygame.image.load('assets/img/tela inicial.webp').convert()
IMAGEM_TRANSICAO_2 = pygame.transform.scale(IMAGEM_TRANSICAO_2, (WIDTH, HEIGHT))
background = FUNDOSELVA

# Imagens e dimensões relacionadas ao Barry (Resina)
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


# Imagens e dimensões relacionadas aos tiros
TIRO_WIDTH = 50
TIRO_HEIGHT = 70
tiro_img = pygame.image.load('assets/img/tiro.png').convert_alpha()
tiro_img = pygame.transform.scale(tiro_img,(TIRO_WIDTH,TIRO_HEIGHT))

# Imagens e dimensões relacionadas aos obstáculos
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
MISSIL_WIDTH = 500
MISSIL_HEIGHT = 500
MISSIL_img = pygame.image.load('assets/img/missil com fogo.png').convert_alpha()
MISSIL_img = pygame.transform.scale(MISSIL_img,(MISSIL_WIDTH,MISSIL_HEIGHT))
RAPOSA_WIDTH = 100
RAPOSA_HEIGHT = 100
RAPOSA_img = pygame.image.load('assets/img/raposa.png').convert_alpha()
RAPOSA_img = pygame.transform.scale(RAPOSA_img,(RAPOSA_WIDTH,RAPOSA_HEIGHT))
BOB_WIDTH = 100
BOB_HEIGHT = 100
BOB_img = pygame.image.load('assets/img/bobrow.png').convert_alpha()
BOB_img = pygame.transform.scale(BOB_img,(BOB_WIDTH,BOB_HEIGHT))


# Imagens e dimensões relacionadas aos alertas
ALERTA_I_WIDTH = 150
ALERTA_I_HEIGHT = 125
ALERTA_I_img = pygame.image.load('assets/img/alerta-inicial.png').convert_alpha()
ALERTA_I_img = pygame.transform.scale(ALERTA_I_img,(ALERTA_I_WIDTH,ALERTA_I_HEIGHT))
ALERTA_P_WIDTH = 150
ALERTA_P_HEIGHT = 125
ALERTA_P_img = pygame.image.load('assets/img/Alerta-chegando.png').convert_alpha()
ALERTA_P_img = pygame.transform.scale(ALERTA_P_img,(ALERTA_P_WIDTH,ALERTA_P_HEIGHT))



# Dicionário para armazenar as imagens do jogo
imagens = {
    "background_i": background_i,
    "logo": logo,
    "TESTLAB": TESTLAB,
    "FUNDOSELVA": FUNDOSELVA,
    "barry_v_img": barry_v_img,
    "barry_a_img": barry_a_img,
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
    "barry_ep_img": barry_ep_img,
    "RAPOSA_img": RAPOSA_img,
    "BOB_img": BOB_img
}

# Dicionário para armazenar dimensões
variaveis_dimensoes = {
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
    "ALERTA_P_HEIGHT": 125,
    "RAPOSA_HEIGHT": 38,
    "RAPOSA_WIDTH": 50,
    "BOB_HEIGHT": 38,
    "BOB_WIDTH": 50
}



# Define imagens que certas variáveis recebem
background_i = imagens["background_i"]
logo = imagens["logo"]
background = imagens["FUNDOSELVA"]
BARRY = imagens["barry_v_img"]
TIRO = imagens["tiro_img"]
LASER1 = imagens["CHOQUE1_img"]
LASER2 = imagens["CHOQUE2_img"]
LASER_LISTA = [LASER1, LASER2]

#cria um dicionario para as imagens que serão utilziadas dentro do arquivo classes 
imagens_classes = {
    "TIRO": TIRO,
    "BARRY": BARRY,
    "LASER_LISTA": LASER_LISTA
}


#Define o background inicial
background = imagens["FUNDOSELVA"]