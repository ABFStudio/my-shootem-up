import pygame
import random 
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 450 - offset
        self.loot_amount = 10
        self.speed = random.randint(2, 6)
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = self.speed
        self.velocity = random.randint(2, 6)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        #infliger des dégats au monstre
        self.health -= amount

        #vérifier si son nombre de points de vie est inférieur ou égal à 0
        if self.health <= 0:
            #faire réapparaitre le monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(2, self.default_speed)
            #ajouter des points au score
            self.game.add_score(self.loot_amount)

            #si la barre d'évènement  est chargée
            if self.game.comet_event.is_full_loaded():
                #supprimer le monstre
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):  
        #afficher l'autre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y -15, self.max_health, 5])
        #afficher la barre principale
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y -15, self.health, 5])        

    def forward(self):
        #le déplacement est possible uniquement sans collisions
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en collisions avec le joueur
        else:
            #infliger des dégats au joueur
            self.game.player.damage(self.attack)

#classe pour la momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)
#l'alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(50)