import pygame

# Inicialize o Pygame
pygame.init()

# Defina a altura e largura da tela
largura = 800
altura = 600

# Defina as cores que você usará
branco = (255, 255, 255)

# Caminho para o arquivo de fonte TTF
caminho_fonte = "assets/fontes/PublicPixel-E447g.ttf"  # Substitua pelo caminho da sua fonte TTF

# Inicialize a janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo de Carregamento de Fonte")

# Carregue a fonte TTF
minha_fonte = pygame.font.Font(caminho_fonte, 36)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Limpe a tela
    tela.fill(branco)

    # Renderize o texto usando a fonte carregada
    texto_renderizado = minha_fonte.render("Olá, Mundo!", True, (0, 0, 0))

    # Desenhe o texto na tela
    tela.blit(texto_renderizado, (largura // 2 - texto_renderizado.get_width() // 2, altura // 2 - texto_renderizado.get_height() // 2))

    # Atualize a tela
    pygame.display.flip()

# Saia do Pygame
pygame.quit()
