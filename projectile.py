import pygame

#le prjectile
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("C:/Users/Antonin/OneDrive/Documents/Python/Mon_Jeu/assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    #faire tourner le projectile
    def rotate(self):
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    #supprimer le projectile
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x +=self.velocity
        self.rotate()
        #vérifier si le projectile entre en collision avec le monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger des dégats
            monster.damage(self.player.attack)

        #vérifier si le projectile sort de l'écran
        if self.rect.x > 1080:
            self.remove()            