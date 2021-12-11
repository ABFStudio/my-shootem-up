import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent
from monster import Mummy
from monster import Alien
from sounds import SoundManager

#créer une classe pour le jeu
class Game:
    def __init__(self):
        #vérifier si le jeu a commencé
        self.is_playing = False
        #générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #générer l'évènement
        self.comet_event = CometFallEvent(self)
        #groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        #gérer le son
        self.sound_manager = SoundManager()
        #gérer la police d'écriture
        self.font = pygame.font.Font("C:/Users/Antonin/OneDrive/Documents/Python/Mon_Jeu/assets/my_custom_font.ttf", 50)
        #mettre le score à 0
        self.score = 0
        self.pressed = {}
        

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        #reset le jeu
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        #jouer le son
        self.sound_manager.play("game_over")

    def update(self,  screen):
        #afficher le score
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        #affficher le joueur
        screen.blit(self.player.image, self.player.rect)

        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        #actualiser l'animation
        self.player.update_animation()

        #actualiser la barre d'évènement
        self.comet_event.update_bar(screen)

        #récupérer les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        #récupérer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #recuperer les comètes
        for comet in self.comet_event.all_comets:
            comet.fall()

        #afficher les projectiles
        self.player.all_projectiles.draw(screen)

         #afficher les monstres
        self.all_monsters.draw(screen)

        #appliquer les comètes
        self.comet_event.all_comets.draw(screen)

        #vérifier ou va le joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
       
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))