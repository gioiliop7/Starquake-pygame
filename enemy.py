import pygame

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)

class enemy(pygame.sprite.Sprite):
    """
    This class represents the enemy
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height, name):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(name)
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Instance variables that control the edges of where we bounce
        self.left_boundary = 10
        self.right_boundary = 10
        self.top_boundary = 10
        self.bottom_boundary = 10

        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0

    def collision_test(self, rect, tiles):
        "Returns the Rect of the tile with which the player collides"
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1