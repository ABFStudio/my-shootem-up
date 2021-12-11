import pygame
import math
from game import Game
from sounds import SoundManager
pygame.init()

#une clock
clock = pygame.time.Clock()
FPS = 120

#la fenêtre
pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 650))

#fond d'écran
background = pygame.image.load('C:/Users/Antonin/OneDrive/Documents/Python/Mon_Jeu/assets/bg.jpg')

#charger la bannière
banner = pygame.image.load("C:/Users/Antonin/OneDrive/Documents/Python/Mon_Jeu/assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer un bouton
play_button = pygame.image.load("C:/Users/Antonin/OneDrive/Documents/Python/Mon_Jeu/assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.333)
play_button_rect.y = math.ceil(screen.get_height() / 1.8)

#charger le jeu
game = Game()

#maintenir la fenêtre ouverte
running = True

#pendant que la fenetre est active
while running:
    screen.blit(background, (0, -300))

    #vérifier si le jeu a commencé
    if game.is_playing:
        #déclencher update()
        game.update(screen)
    #vérifier que le jeu n'a pas envore commencé    
    else:
        #ajouter le bouton
        screen.blit(play_button, play_button_rect)
        #intégrer la bannière
        screen.blit(banner, banner_rect)

    #fermer la fenetre
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()

        #détecter l'enclenchement d'une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #lancer une boule de feu avec espace
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    #lancer le jeu
                    game.start()
                    #jouer le son click
                    game.sound_manager.play("click")
           
        #si la touche est relachée
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                #jouer le son
                game.sound_manager.play("click")

#fixer les fps
clock.tick(FPS)