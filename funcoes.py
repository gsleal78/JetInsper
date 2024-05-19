import pygame
import random
from config import num_conjuntos, WIDTH, HEIGHT
from imagens_sons import variaveis_dimensoes, imagens, imagens_classes
from classes import Moeda, Laser, Raposa, Bob, all_moedas, lasersprite, raposasprite, bobsprite, all_sprites

def verificar_colisao_com_todos(sprite, grupos):
    for grupo in grupos:
        if pygame.sprite.spritecollideany(sprite, grupo, collided=pygame.sprite.collide_mask):
            return True
    return False

def criar_moedas(velocidade):
    max_tentativas = 50  # Limite de tentativas
    tentativas = 0
    
    while tentativas < max_tentativas: 
        tentativas += 1
        for i in range(num_conjuntos):
            center_x = random.randint(WIDTH, WIDTH + 200)
            center_y = random.randint(100 + 3 * variaveis_dimensoes["MOEDAS_HEIGHT"], HEIGHT - 100 - 3 * variaveis_dimensoes["MOEDAS_HEIGHT"])

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

        pode_criar = True
        for pos in positions:
            moeda = Moeda(imagens["MOEDAS_img"], *pos, velocidade)
            if verificar_colisao_com_todos(moeda, [all_sprites]):
                pode_criar = False
                break

        if pode_criar:
            for pos in positions:
                moeda = Moeda(imagens["MOEDAS_img"], *pos, velocidade)
                all_moedas.add(moeda)
                all_sprites.add(moeda)
            break

def criar_laser(velocidade):
    max_tentativas = 50  # Limite de tentativas
    tentativas = 0

    while tentativas < max_tentativas: 
        tentativas += 1
        LASER = random.choice(imagens_classes["LASER_LISTA"])   
        x = random.randint(WIDTH, WIDTH + 200)
        y = random.randint(100 + variaveis_dimensoes["CHOQUE_HEIGHT"], HEIGHT)
        laser = Laser(LASER, x, y, velocidade)
        colisao = verificar_colisao_com_todos(laser, [all_sprites])
        if not colisao:
            lasersprite.add(laser)
            all_sprites.add(laser)
            break

def criar_raposa(velocidade): 
    max_tentativas = 50  # Limite de tentativas
    tentativas = 0

    while tentativas < max_tentativas: 
        tentativas += 1
        x = random.randint(WIDTH, WIDTH + 200)
        y = random.randint(100 + variaveis_dimensoes["RAPOSA_HEIGHT"], HEIGHT)
        raposa = Raposa(imagens["RAPOSA_img"], velocidade, x, y)
        colisao = verificar_colisao_com_todos(raposa, [all_sprites])
        if not colisao: 
            raposasprite.add(raposa)
            all_sprites.add(raposa)
            break

def criar_bob(velocidade): 
    max_tentativas = 50  # Limite de tentativas
    tentativas = 0

    while tentativas < max_tentativas:
        tentativas += 1
        x = random.randint(WIDTH, WIDTH + 200)
        y = random.randint(100 + variaveis_dimensoes["BOB_HEIGHT"], HEIGHT)
        bob = Bob(imagens["BOB_img"], velocidade, x, y)
        colisao = verificar_colisao_com_todos(bob, [all_sprites])
        if not colisao: 
            bobsprite.add(bob)
            all_sprites.add(bob)
            break
