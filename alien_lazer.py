import pygame
from hero import Hero

class Alien_lazer(Hero):

    def update(self):
        self.rect.y -= -6