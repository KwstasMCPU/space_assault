import pygame
from hero import Hero

class Lazer(Hero):

    def update(self):
        self.rect.y -= 6

