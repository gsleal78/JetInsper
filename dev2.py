print("Ishai")

acabou = 0
jogando = 1
explodindo = 2
estadoo = jogando

'''
if estadoo == jogando:
            # Verifica se houve colisão entre barry e laser amarelo
            hits = pygame.sprite.groupcollide(all_meteors, all_bullets, True, True, pygame.sprite.collide_mask)
            for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                assets[DESTROY_SOUND].play()
                m = Meteor(assets)
                all_sprites.add(m)
                all_meteors.add(m)

                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(meteor.rect.center, assets)
                all_sprites.add(explosao)

                # Ganhou pontos!
                score += 100
                if score % 1000 == 0:
                    lives += 1

            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, all_meteors, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Ship(groups, assets)
                    all_sprites.add(player)

'''

########################################################################################
# Desenhando o score
text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
text_rect = text_surface.get_rect()
text_rect.midtop = (WIDTH / 2,  10)
window.blit(text_surface, text_rect)