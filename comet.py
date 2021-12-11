import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        #image de la comète
        self.image = pygame.image.load("C:/Users/Antonin/OneDrive/Documents/Python/Mon_Jeu/assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 5)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play("meteorite")
        #vérifier si le nombre de comètes est de 0
        if len(self.comet_event.all_comets) == 0:
            #reset la barre
            self.comet_event.reset_percent()
            #faire apparaitre les deux premiers monstres
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        #collision avec le sol
        if self.rect.y >= 500:
            #supprimer la comète
            self.remove()
            #si il n'y a plus de comètes
            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #vérifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            #retirer la boule de feu
            self.remove()
            #infliger des dégats au joueur
            self.comet_event.game.player.damage(20)