import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.image.load("mov_new.png").convert()
        self.image.set_colorkey(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x