import pygame  # Importa a biblioteca Pygame para criação do jogo


# Definindo as dimensões da janela do jogo
WIDTH = 1200
HEIGHT = 750

# Variáveis de controle do estado do jogo
game_started = False  # Define o estado inicial do jogo como não iniciado
jogo_acabou = False  # Indica se o jogo acabou
moedas_coletadas = 0  # Contador de moedas coletadas pelo jogador
num_conjuntos = 1  # Número de conjuntos de moedas que serão criadas

# Configuração do relógio e FPS (Frames Por Segundo)
clock = pygame.time.Clock()  # Cria um objeto Clock para controlar o tempo no jogo
FPS = 100  # Define a taxa de FPS

# Variável para controlar a posição inicial do plano de fundo
background_x = 0

# Variáveis de controle de fase
fase_atual = 1  # Define a fase atual do jogo
fase_atingida = False  # Indica se uma nova fase foi atingida
GAME = True  # Indica se o jogo está em execução

# Temporizadores para criação de objetos no jogo
criar_moedas_timer = pygame.time.get_ticks()  
criar_laser_timer = pygame.time.get_ticks()  
criar_raposa_timer = pygame.time.get_ticks() 
criar_bob_timer = pygame.time.get_ticks()  
