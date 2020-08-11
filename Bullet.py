import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self, stay_right):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("bullet.png").convert()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.right = stay_right

    def update(self):
        """ Move the bullet. """
        if self.right == True:
            self.rect.x += 6.5
        else:
            self.rect.x -= 6.5