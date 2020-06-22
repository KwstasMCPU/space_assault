import pygame
from hero import Hero
BLACK = (0,0,0)

class Lazer(Hero):

    def update(self):
        '''moves the lazer'''
        self.rect.y -= 6

