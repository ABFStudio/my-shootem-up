import pygame

#classe pour contenir les animations
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"C:/Users/Antonin/OneDrive/Documents/Python/Mon_Jeu/assets/{sprite_name}.png" )
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    #animer le sprite
    def animate(self, loop=False):
        #vérifier si l'animation est active
        if self.animation:

            self.current_image += 1
            #vérifier si on est à la fin des images
            if self.current_image >= len(self.images):
                #remettre l'animation au début
                self.current_image = 0
                #vérifier si l'animation n'est pas en mode boucle
                if loop is False:
                    #désactiver l'animation
                    self.animation = False
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image,self.size)

#charger les images d'un sprite
def load_animation_images(sprite_name):
    images = []
    path = f"C:/Users/Antonin/OneDrive/Documents/Python/Mon_Jeu/assets/{sprite_name}/{sprite_name}"

    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))
    return images

#dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    "mummy": load_animation_images("mummy"), 
    "player": load_animation_images("player"), 
    "alien": load_animation_images("alien")
}