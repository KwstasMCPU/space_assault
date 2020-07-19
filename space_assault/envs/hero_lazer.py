import pygame
from space_assault.envs.hero import Hero

class Lazer(Hero):

    def update(self):
        self.rect.y -= 6

