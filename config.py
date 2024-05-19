import pygame
import random

WIDTH = 1200
HEIGHT = 750

game_started = False  # Define o estado inicial do jogo como False
jogo_acabou = False  # Controla se o jogo acabou ou não
moedas_coletadas = 0
num_conjuntos = 1

clock = pygame.time.Clock()
FPS = 100


background_x = 0

# Variáveis de controle de fase
fase_atual = 1
fase_atingida = False
GAME = True

criar_moedas_timer = pygame.time.get_ticks()
criar_laser_timer = pygame.time.get_ticks()
criar_raposa_timer = pygame.time.get_ticks()
criar_bob_timer = pygame.time.get_ticks()

