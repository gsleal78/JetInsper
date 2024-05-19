import pygame  # Importa a biblioteca Pygame para criação do jogo
import random  # Importa o módulo random para gerar números aleatórios
from config import num_conjuntos, WIDTH, HEIGHT  # Importa configurações do jogo
from imagens_sons import variaveis_dimensoes, imagens, imagens_classes  # Importa variáveis e imagens do jogo
from classes import Moeda, Laser, Raposa, Bob, all_moedas, lasersprite, raposasprite, bobsprite, all_sprites  # Importa classes e grupos de sprites

# Função para verificar colisão entre um sprite e qualquer sprite de um ou mais grupos
def verificar_colisao_com_todos(sprite, grupos):
    for grupo in grupos:
        if pygame.sprite.spritecollideany(sprite, grupo, collided=pygame.sprite.collide_mask):
            return True  # Retorna True se houver colisão
    return False  # Retorna False se não houver colisão

# Função para criar moedas em posições aleatórias
def criar_moedas(velocidade):
    max_tentativas = 10  # Limite de tentativas para criar moedas
    tentativas = 0
    
    while tentativas < max_tentativas:
        tentativas += 1  # Incrementa o contador de tentativas
        for i in range(num_conjuntos):  # Loop para criar conjuntos de moedas
            center_x = random.randint(WIDTH, WIDTH + 200)
            center_y = random.randint(100 + 3 * variaveis_dimensoes["MOEDAS_HEIGHT"], HEIGHT - 100 - 3 * variaveis_dimensoes["MOEDAS_HEIGHT"])

            # Definindo posições para as moedas em torno de um ponto central
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

        pode_criar = True  # Variável para verificar se as moedas podem ser criadas
        for pos in positions:
            moeda = Moeda(imagens["MOEDAS_img"], *pos, velocidade)
            if verificar_colisao_com_todos(moeda, [all_sprites]):
                pode_criar = False  # Define para False se houver colisão
                break

        if pode_criar:  # Se não houver colisão, cria as moedas
            for pos in positions:
                moeda = Moeda(imagens["MOEDAS_img"], *pos, velocidade)
                all_moedas.add(moeda)  # Adiciona a moeda ao grupo all_moedas
                all_sprites.add(moeda)  # Adiciona a moeda ao grupo all_sprites
            break

# Função para criar lasers em posições aleatórias
def criar_laser(velocidade):
    max_tentativas = 10  # Limite de tentativas para criar lasers
    tentativas = 0

    while tentativas < max_tentativas:
        tentativas += 1  # Incrementa o contador de tentativas
        LASER = random.choice(imagens_classes["LASER_LISTA"])  # Escolhe uma imagem de laser aleatoriamente
        x = random.randint(WIDTH, WIDTH + 200)
        y = random.randint(100 + variaveis_dimensoes["CHOQUE_HEIGHT"], HEIGHT)
        laser = Laser(LASER, x, y, velocidade)
        colisao = verificar_colisao_com_todos(laser, [all_sprites])
        if not colisao:  # Se não houver colisão, adiciona o laser
            lasersprite.add(laser)  # Adiciona o laser ao grupo lasersprite
            all_sprites.add(laser)  # Adiciona o laser ao grupo all_sprites
            break

# Função para criar raposas em posições aleatórias
def criar_raposa(velocidade):
    max_tentativas = 10  # Limite de tentativas para criar raposas
    tentativas = 0

    while tentativas < max_tentativas:
        tentativas += 1  # Incrementa o contador de tentativas
        x = random.randint(WIDTH, WIDTH + 200)
        y = random.randint(100 + variaveis_dimensoes["RAPOSA_HEIGHT"], HEIGHT)
        raposa = Raposa(imagens["RAPOSA_img"], velocidade, x, y)
        colisao = verificar_colisao_com_todos(raposa, [all_sprites])
        if not colisao:  # Se não houver colisão, adiciona a raposa
            raposasprite.add(raposa)  # Adiciona a raposa ao grupo raposasprite
            all_sprites.add(raposa)  # Adiciona a raposa ao grupo all_sprites
            break

# Função para criar Bob em posições aleatórias
def criar_bob(velocidade):
    max_tentativas = 10  # Limite de tentativas para criar Bob
    tentativas = 0

    while tentativas < max_tentativas:
        tentativas += 1  # Incrementa o contador de tentativas
        x = random.randint(WIDTH, WIDTH + 200)
        y = random.randint(100 + variaveis_dimensoes["BOB_HEIGHT"], HEIGHT)
        bob = Bob(imagens["BOB_img"], velocidade, x, y)
        colisao = verificar_colisao_com_todos(bob, [all_sprites])
        if not colisao:  # Se não houver colisão, adiciona Bob
            bobsprite.add(bob)  # Adiciona Bob ao grupo bobsprite
            all_sprites.add(bob)  # Adiciona Bob ao grupo all_sprites
            break
