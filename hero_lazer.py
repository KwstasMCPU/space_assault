import pygame
from hero import Hero
BLACK = (0,0,0)

class Lazer(Hero):

    def update(self):
        self.rect.y -= 6

