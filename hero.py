import pygame

BLACK = (0,0,0)

class Hero(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the spaceship 
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()