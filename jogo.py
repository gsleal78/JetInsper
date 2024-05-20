import pygame  # Importa a biblioteca Pygame para criação do jogo
from config import WIDTH, HEIGHT, game_started, jogo_acabou, fase_atingida, fase_atual, GAME, clock, FPS, background_x, criar_laser_timer, criar_moedas_timer, criar_raposa_timer, criar_bob_timer  # Importa variáveis do arquivo config
pygame.init()  # Inicializa o Pygame
pygame.mixer.init()  # Inicializa o mixer de áudio do Pygame

window = pygame.display.set_mode((WIDTH, HEIGHT))  # Define a janela do jogo com as dimensões especificadas
pygame.display.set_caption('JetInsper')  # Define o título da janela do jogo

from imagens_sons import imagens, textos, fonte_moeda, background, sons  # Importa imagens, textos, fontes e sons do jogo do arquivo imagens_sons

from classes import all_sprites, all_bullets, all_moedas, lasersprite, raposasprite, bobsprite, voando, Barry  # Importa todas as classes necessárias para o jogo do arquivo classes e o personagem barry

from funcoes import criar_laser, criar_moedas, criar_raposa, criar_bob  # Importa as funções necessárias para criar os obstaculos do jogo

pygame.mixer.music.play(loops=-1)  # Toca a música de fundo do jogo em loop


 # Loop principal do jogo enquanto a variável GAME for True
while GAME:  
    if not game_started:  # Se o jogo ainda não começou
        # Desenha a tela de início do jogo
        window.blit(imagens["background_i"], (0, 0))  # Desenha o fundo da tela de início

        #Desenha o logo e o texto inicial
        window.blit(imagens["logo"], (WIDTH / 2 - imagens["logo"].get_width() / 2, HEIGHT / 2 - imagens["logo"].get_height() + 100))  
        window.blit(textos["texto_renderizado1"], (WIDTH // 2 - textos["texto_renderizado1"].get_width() // 2, textos["posicao_y_linha1"] + 200))  
        window.blit(textos["texto_renderizado2"], (WIDTH // 2 - textos["texto_renderizado2"].get_width() // 2, textos["posicao_y_linha2"] + 220))  

        pygame.display.update()  # Atualiza a tela
        # Loop de eventos do pygame
        for event in pygame.event.get(): 
            #Se o evento for fechar a janela, encerra o jogo
            if event.type == pygame.QUIT:  
                pygame.quit()  
            # Se a tecla pressionada for Enter, inicia o jogo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    game_started = True  
                    sons["hog_rider"].play()  

        clock.tick(FPS)  
        continue 
    #Se o jogo já começou
    else:
        #Enquanto o jogador ainda nao morreu
        if not jogo_acabou:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    pygame.quit()  
                # Se o jogador atingiu uma fase nova
                if fase_atingida:  
                    if fase_atual == 2:  # Se a fase atual for 2

                        # Prepara a transição para a próxima fase
                        fase_atingida = False  #Redefine a variavel fase_atingida para False
                        fase_atual += 1  # Sobe de fase
                        background = imagens["TESTLAB"]  # Altera o plano de fundo para a fase seguinte
                        criar_moedas_timer = pygame.time.get_ticks()  # Reinicia o timer para criar moedas
                        criar_laser_timer = pygame.time.get_ticks()  # Reinicia o timer para criar lasers
                        background_x = 0  # Reinicia a posição do plano de fundo
                        # Limpa todos os grupos de sprites
                        all_sprites.empty()
                        all_moedas.empty()
                        lasersprite.empty()
                        bobsprite.empty  
                        raposasprite.empty()  
                        # Salva certas variáveis do jogador para a próxima fase
                        moedas_coletadas = voando.moedas_coletadas
                        posicao_y = voando.rect.y
                        speed = voando.speedy

                        # Cria um novo Barry para a próxima fase
                        voando = Barry(imagens["barry_v_img"], 50, posicao_y, moedas_coletadas)
                        voando.speedy = speed  # Mantém a velocidade do Barry
                        all_sprites.add(voando)  # Adiciona o novo Barry ao grupo de sprites
                    #Se a fase atual for 1
                    else:
                        #Redefine a variavel fase atingida e sobe de fase
                        fase_atingida = False  
                        fase_atual += 1
                        #Limpa todos os grupos de sprites
                        all_sprites.empty()
                        all_moedas.empty()
                        lasersprite.empty()
                        bobsprite.empty
                        raposasprite.empty()

                        #Muda a tela de fundo do jogo, reinicia os timers necessarios e redefine a posição do fundo
                        background = imagens["background_i"] 
                        criar_moedas_timer = pygame.time.get_ticks() 
                        criar_laser_timer = pygame.time.get_ticks()
                        background_x = 0 
                        
                        #mantem o numero de moedas coletadas e a posição e a velocidade do barry para dar continuidade ao jogo
                        moedas_coletadas = voando.moedas_coletadas
                        posicao_y = voando.rect.y
                        speed = voando.speedy

                        # Cria um novo Barry para a próxima fase
                        voando = Barry(imagens["barry_v_img"], 50, posicao_y, moedas_coletadas)
                        voando.speedy = speed 
                        all_sprites.add(voando) 

                #Se ainda nao passou de fase
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:  # Se a tecla pressionada foi a barra de espaço
                            # Troca a imagem do Barry atual por uma imagem do Barry voando, com fogo saindo da mochila a jato
                            all_sprites.remove(voando)
                            BARRY = imagens["barry_a_img"]
                            voando = Barry(BARRY, voando.rect.x, voando.rect.y, voando.moedas_coletadas)
                            all_sprites.add(voando)  # Adiciona o novo Barry ao grupo de sprites
                            voando.shooting = True  # Muda o estado de atirar do Barry para True
                            # Ajusta a velocidade vertical do Barry dependendo da fase
                            if fase_atual == 3: 
                                voando.speedy +=8
                            else:
                                voando.speedy += 6
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:  # Se a tecla solta foi a barra de espaço
                            # Remove o Barry voando e retorna à imagem do Barry normal
                            all_sprites.remove(voando)
                            BARRY = imagens["barry_v_img"]
                            voando = Barry(BARRY, voando.rect.x, voando.rect.y, voando.moedas_coletadas)
                            all_sprites.add(voando) 
                            voando.shooting = False  # Muda o estado de atirar para False
                            
                            if fase_atual == 3: 
                                voando.speedy -=8
                            else:
                                voando.speedy -= 6

            #Definindo as caracteristicas das fases, como velocidade dos obstaculos e  tempo em que são criados 

            if fase_atual == 1:
                background_x -= 7  # Faz o fundo se mover para a esquerda
                if pygame.time.get_ticks() - criar_moedas_timer > 2500:  # Verifica se é hora de criar moedas
                    criar_moedas(7)  # Chama a função para criar moedas
                    criar_moedas_timer = pygame.time.get_ticks()  # Reinicia o temporizador para criar moedas
                if pygame.time.get_ticks() - criar_laser_timer > 4000:  # Verifica se é hora de criar lasers
                    criar_laser(7)  # Chama a função para criar lasers
                    criar_laser_timer = pygame.time.get_ticks()  # Reinicia o temporizador para criar lasers
                if pygame.time.get_ticks() - criar_raposa_timer > 3250:  # Verifica se é hora de criar raposas
                    criar_raposa(7)  # Chama a função para criar raposas
                    criar_raposa_timer = pygame.time.get_ticks()  # Reinicia o temporizador para criar raposas

            elif fase_atual == 2:
                background_x -= 10
                if pygame.time.get_ticks() - criar_moedas_timer > 2000:
                    criar_moedas(10)
                    criar_moedas_timer = pygame.time.get_ticks()
                if pygame.time.get_ticks() - criar_laser_timer > 3500:
                    criar_laser(10)
                    criar_laser_timer = pygame.time.get_ticks()
                if pygame.time.get_ticks() - criar_raposa_timer > 2500: 
                    criar_raposa(10)
                    criar_raposa_timer = pygame.time.get_ticks()
                if pygame.time.get_ticks() - criar_bob_timer> 3000: 
                    criar_bob(10)
                    criar_bob_timer = pygame.time.get_ticks()

            elif fase_atual == 3:
                background_x -= 10
                if pygame.time.get_ticks() - criar_moedas_timer > 1400:
                    criar_moedas(10)
                    criar_moedas_timer = pygame.time.get_ticks()
                if pygame.time.get_ticks() - criar_laser_timer > 1600:
                    criar_laser(10)
                    criar_laser_timer = pygame.time.get_ticks()
                if pygame.time.get_ticks() - criar_raposa_timer > 1050: 
                    criar_raposa(10)
                    criar_raposa_timer = pygame.time.get_ticks()
                if pygame.time.get_ticks() - criar_bob_timer> 1250: 
                    criar_bob(10)
                    criar_bob_timer = pygame.time.get_ticks()

            # Verificar colisões com o barry 

            #Aumenta a quantidade de moedas coletadas e toca o som das moedas
            hits_moedas = pygame.sprite.spritecollide(voando, all_moedas, True, pygame.sprite.collide_mask)
            for hit in hits_moedas:
                voando.moedas_coletadas += 1
                sons['coin_sound'].play()

            #Verifica colisões que levam ao fim do jogo, e toca o som especifico para cada colisão 
            hits_lasers = pygame.sprite.spritecollide(voando, lasersprite, True, pygame.sprite.collide_mask)
            hits_raposa = pygame.sprite.spritecollide(voando, raposasprite, True, pygame.sprite.collide_mask)
            hits_bob = pygame.sprite.spritecollide(voando, bobsprite, True, pygame.sprite.collide_mask)
            if hits_raposa:
                sons["som_morte"].play()
                pygame.time.delay(1200) #pausa o jogo para dar tempo de tocar o audio da colisão
                jogo_acabou = True
            if hits_lasers: 
                sons["eletric_sound"].play()
                pygame.time.delay(1200)
                jogo_acabou = True
            if hits_bob: 
                sons["som_bob"].play()
                pygame.time.delay(1200)
                jogo_acabou = True
            


            # Verificar se o jogador atingiu o numero de moedas para trocar de fase
            if voando.moedas_coletadas >= 50 and not fase_atingida and fase_atual == 1:
                fase_atingida = True  
                lasersprite.empty()
                all_moedas.empty()
                raposasprite.empty()
                all_sprites.empty()
            elif voando.moedas_coletadas >= 150 and not fase_atingida and fase_atual == 2:
                fase_atingida = True  
                bobsprite.empty()
                lasersprite.empty()
                all_moedas.empty()
                raposasprite.empty()
                all_sprites.empty()
                
            # Atualize as posições dos sprites
            all_sprites.update()

            if background_x <= -WIDTH:
                background_x = 0

            # Desenhe o fundo duas vezes para criar o efeito de loop infinito
            window.blit(background, (background_x, 0))
            window.blit(background, (background_x + WIDTH, 0))

            #Desenha os sprites no jogo e a quantidade de moedas coletadas
            all_sprites.draw(window)
            text_surface = fonte_moeda.render("{:05d}".format(voando.moedas_coletadas), True, (10, 10, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2, 10)
            window.blit(text_surface, text_rect)


            pygame.display.update()
            clock.tick(FPS)

        #Se o jogo acabou (se o jogador colidiu com algum obstaculo)
        else: 
            #Dsenha a tela "final do jogo" 
            window.blit(imagens['background_i'], (0, 0))
            window.blit(imagens["logo"], (WIDTH / 2 - imagens["logo"].get_width() / 2, HEIGHT / 2 - imagens["logo"].get_height() + 100))
            window.blit(textos["texto_renderizado2_1"], (WIDTH // 2 - textos["texto_renderizado2_1"].get_width() // 2,textos["posicao_y_linha2_1"] + 200))
            window.blit(textos["texto_renderizado2_2"],(WIDTH // 2 - textos["texto_renderizado2_2"].get_width() // 2,textos["posicao_y_linha2_2"] + 220))
            pygame.display.update()
            clock.tick(FPS)
            #Verifica se o jogador quer jogar de novo ou deseja parar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        GAME = False

                    #Se decidir jogar de novo, reseta o jogo
                    if event.key == pygame.K_RETURN:
                        jogo_acabou = False
                        fase_atingida = False
                        voando.moedas_coletadas = 0
                        
                        # Limpar todos os grupos de sprites
                        all_sprites.empty()
                        all_moedas.empty()
                        lasersprite.empty()
                        all_bullets.empty()
                        raposasprite.empty()
                        bobsprite.empty()
                        
                        # Reinicia os timers de obstáculos
                        criar_moedas_timer = pygame.time.get_ticks()
                        criar_laser_timer = pygame.time.get_ticks()
                        criar_raposa_timer = pygame.time.get_ticks()
                        criar_bob_timer = pygame.time.get_ticks()
                        
                        # Reinicia a posição inicial do fundo
                        background_x = 0
                        
                        # Reinicia a fase atual para a primeira fase
                        fase_atual = 1
                        
                        # Reinicia a imagem de fundo para a fase inicial
                        background = imagens["FUNDOSELVA"]
                        
                        # Cria o barry novamente
                        voando = Barry(imagens["barry_v_img"], 50, 750, 0)
                        all_sprites.add(voando)

#Encerra o jogo
pygame.quit()