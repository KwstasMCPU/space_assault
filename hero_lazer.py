import pygame
from hero import Hero
BLACK = (0,0,0)

class Lazer(Hero):
    '''
    child class from Hero Parent Class
    '''
    def update(self):
        self.rect.y -= 6

