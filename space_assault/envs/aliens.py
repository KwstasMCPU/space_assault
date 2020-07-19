import pygame
from space_assault.envs.hero import Hero
from random import choice

class Alien(Hero):
    '''
    
    '''
    def __init__(self, color, height, width, health, initialPosX):
        super().__init__(color, height, width, health)

        self.the_initialest_pos = initialPosX
        self.direction = False

    def moveRight(self):
        self.rect.x += 1

    def moveLeft(self):
        self.rect.x -= 1

    def get_initial_pos(self):
        '''
        returns the initial x position of any alien object
        '''
        init_x = self.rect.x
        # init_y = self.rect.y
        return init_x

    def get_initial_dir(self):
        '''
        sets and returns initial direction of the alien object
        '''
        direction = self.direction = choice([True, False]) # True is for left, and False is for right
        return direction


