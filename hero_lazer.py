import pygame
from hero import Hero

class Lazer(Hero):
    '''
    child class from Hero Parent Class
    '''
    def update(self):
        self.rect.y -= 6

