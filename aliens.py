import pygame
from hero import Hero
from random import choice
import time


class Alien(Hero):

    def moveRight(self):
        self.rect.x += 1

    def moveLeft(self):
        self.rect.x -= 1

    def get_initial_pos(self):
        '''
        returns the initial x position of any alien object
        '''
        init_x = self.rect.x
        return init_x

    def get_initial_dir(self):
        '''
        sets and returns initial direction of the alien object
        '''
        direction = self.direction = choice([True, False]) # True is for left, and False is for right
        return direction
