import pygame
from random import randint
import time

BLACK = (0,0,0)

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw alien ship
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRandomY(self, pixels):
        self.rect.y += pixels.pop()
        if self.rect.y < 100:
            self.rect.y = 100
        if self.rect.y > 300:
            self.rect.y = 300
       
    
    def moveRandomX(self, pixels):
        self.rect.x += pixels.pop()
        if self.rect.x < 300:
            self.rect.x = 300
        if self.rect.x > 400:
            self.rect.x = 400
        

 