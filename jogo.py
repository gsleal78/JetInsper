import pygame
import time
from config import WIDTH, HEIGHT, game_started, jogo_acabou, fase_atingida, fase_atual, GAME, clock, FPS, background_x, criar_laser_timer, criar_moedas_timer,criar_raposa_timer,criar_bob_timer
pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JetInsper')

from imagens_sons import imagens, textos, fonte_moeda, background,sons
from classes import all_sprites, all_bullets, all_moedas, lasersprite,raposasprite,bobsprite, voando, Barry
from funcoes import criar_laser, criar_moedas,criar_raposa,criar_bob

pygame.mixer.music.play(loops=-1)

while GAME:
    if not game_started:
        window.blit(imagens["background_i"], (0, 0))
        window.blit(imagens["logo"], (WIDTH / 2 - imagens["logo"].get_width() / 2, HEIGHT / 2 - imagens["logo"].get_height() + 100))
        window.blit(textos["texto_renderizado1"],
                    (WIDTH // 2 - textos["texto_renderizado1"].get_width() // 2,
                    textos["posicao_y_linha1"] + 200))
        window.blit(textos["texto_renderizado2"],
                    (WIDTH // 2 - textos["texto_renderizado2"].get_width() // 2,
                    textos["posicao_y_linha2"] + 220))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_started = True
                    sons["hog_rider"].play()

        clock.tick(FPS)
        continue
    else: 
        if not jogo_acabou: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if fase_atingida:
                    if fase_atual == 2:
                        fase_atingida = False
                        fase_atual += 1
                        background = imagens["TESTLAB"] 
                        criar_moedas_timer = pygame.time.get_ticks()
                        criar_laser_timer = pygame.time.get_ticks()
                        background_x = 0
                        all_sprites.empty()
                        all_moedas.empty()
                        lasersprite.empty()
                        bobsprite.empty
                        raposasprite.empty()
                        moedas_coletadas = voando.moedas_coletadas
                        posicao_y = voando.rect.y
                        speed = voando.speedy
                        voando = Barry(imagens["barry_v_img"], 50, posicao_y, moedas_coletadas)
                        voando.speedy = speed
                        all_sprites.add(voando)
                    else:
                        fase_atingida = False
                        fase_atual += 1
                        all_sprites.empty()
                        all_moedas.empty()
                        lasersprite.empty()
                        bobsprite.empty
                        raposasprite.empty()
                        background = imagens["background_i"]  # Altera a imagem de fundo para a nova fase
                        criar_moedas_timer = pygame.time.get_ticks()
                        criar_laser_timer = pygame.time.get_ticks()
                        background_x = 0
                        moedas_coletadas = voando.moedas_coletadas
                        posicao_y = voando.rect.y
                        speed = voando.speedy
                        voando = Barry(imagens["barry_v_img"], 50, posicao_y, moedas_coletadas)
                        voando.speedy = speed
                        all_sprites.add(voando)
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            all_sprites.remove(voando)
                            BARRY = imagens["barry_a_img"]
                            voando = Barry(BARRY, voando.rect.x, voando.rect.y, voando.moedas_coletadas)
                            all_sprites.add(voando)
                            voando.shooting = True
                            if fase_atual == 3: 
                                voando.speedy +=8
                            else:
                                voando.speedy += 6
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            all_sprites.remove(voando)
                            BARRY = imagens["barry_v_img"]
                            voando = Barry(BARRY, voando.rect.x, voando.rect.y, voando.moedas_coletadas)
                            all_sprites.add(voando)
                            voando.shooting = False
                            if fase_atual == 3: 
                                voando.speedy -=8
                            else:
                                voando.speedy -= 6
            if fase_atual == 1:
                background_x -= 7
                if pygame.time.get_ticks() - criar_moedas_timer > 2500:
                    criar_moedas(7)
                    criar_moedas_timer = pygame.time.get_ticks()
                if pygame.time.get_ticks() - criar_laser_timer > 4000:
                    criar_laser(7)
                    criar_laser_timer = pygame.time.get_ticks()
                if pygame.time.get_ticks() - criar_raposa_timer > 3250: 
                    criar_raposa(7)
                    criar_raposa_timer = pygame.time.get_ticks()
                    
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

            # Verificar colisões
            hits_moedas = pygame.sprite.spritecollide(voando, all_moedas, True, pygame.sprite.collide_mask)
            for hit in hits_moedas:
                voando.moedas_coletadas += 1
                sons['coin_sound'].play()

            hits_lasers = pygame.sprite.spritecollide(voando, lasersprite, True, pygame.sprite.collide_mask)
            hits_raposa = pygame.sprite.spritecollide(voando, raposasprite, True, pygame.sprite.collide_mask)
            hits_bob = pygame.sprite.spritecollide(voando, bobsprite, True, pygame.sprite.collide_mask)
            if hits_raposa:
                sons["som_morte"].play()
                pygame.time.delay(1200)
                jogo_acabou = True
            if hits_lasers: 
                sons["eletric_sound"].play()
                pygame.time.delay(1200)
                jogo_acabou = True
            if hits_bob: 
                sons["som_bob"].play()
                pygame.time.delay(1200)
                jogo_acabou = True
            


            # Verificar se a fase foi atingida
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
                
            # Atualize a posição do personagem
            all_sprites.update()

            if background_x <= -WIDTH:
                background_x = 0

            # Desenhe o fundo duas vezes para criar o efeito de loop infinito
            window.blit(background, (background_x, 0))
            window.blit(background, (background_x + WIDTH, 0))


            all_sprites.draw(window)

            text_surface = fonte_moeda.render("{:05d}".format(voando.moedas_coletadas), True, (10, 10, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2, 10)
            window.blit(text_surface, text_rect)

            pygame.display.update()
            clock.tick(FPS)
                
        else: 
            window.blit(imagens['background_i'], (0, 0))
            window.blit(imagens["logo"], (WIDTH / 2 - imagens["logo"].get_width() / 2, HEIGHT / 2 - imagens["logo"].get_height() + 100))
            window.blit(textos["texto_renderizado2_1"], (WIDTH // 2 - textos["texto_renderizado2_1"].get_width() // 2,textos["posicao_y_linha2_1"] + 200))
            window.blit(textos["texto_renderizado2_2"],(WIDTH // 2 - textos["texto_renderizado2_2"].get_width() // 2,textos["posicao_y_linha2_2"] + 220))
            pygame.display.update()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        GAME = False
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
                        
                        # Reiniciar variáveis de estado dos timers
                        criar_moedas_timer = pygame.time.get_ticks()
                        criar_laser_timer = pygame.time.get_ticks()
                        criar_raposa_timer = pygame.time.get_ticks()
                        criar_bob_timer = pygame.time.get_ticks()
                        
                        # Reiniciar a posição do fundo
                        background_x = 0
                        
                        # Reiniciar a fase atual para a primeira fase
                        fase_atual = 1
                        
                        # Reiniciar a imagem de fundo para a fase inicial
                        background = imagens["FUNDOSELVA"]
                        
                        # Criar um novo objeto jogador e adicionar ao grupo de sprites
                        voando = Barry(imagens["barry_v_img"], 50, 750, 0)
                        all_sprites.add(voando)

pygame.quit()