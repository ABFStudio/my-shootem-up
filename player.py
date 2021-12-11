import pygame
from projectile import Projectile
import animation

#le joueur
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 400

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):  
        #afficher l'autre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y +15, self.max_health, 7])
        #afficher la barre principale
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y +15, self.health, 7])
    
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        #démarrer l'animation
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play("tir")

    #aller à droite
    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    #aller à gauche
    def move_left(self):
        self.rect.x -= self.velocity