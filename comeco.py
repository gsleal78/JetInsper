import pygame
import random
from os import path

from definindo_imagens import imagens

FPS = 30
ini = 0
jogo = 1
sair = 2

def tela_inicio(tela_m,logo_m):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(imagens, 'background_i')).convert()
    background_rect = background.get_rect()
    logo = pygame.image.load(path.join(imagens, 'logo')).convert()
    logo_rect = logo.get_rect()

    

    rodando = True
    while rodando:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for evento in pygame.event.get():
            # Verifica se foi fechado.
            if evento.type == pygame.QUIT:
                estado = sair
                rodando = False

            if evento.type == pygame.KEYUP:
                estado = jogo
                rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela_m.fill(0,0,0)
        tela_m.blit(background, background_rect)
        logo_m.blit(logo, logo_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado
