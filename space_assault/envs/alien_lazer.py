import pygame
from space_assault.envs.hero import Hero

class Alien_lazer(Hero):

    def update(self):
        self.rect.y -= -6