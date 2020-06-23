import pygame
from hero import Hero
from random import randint
import time

BLACK = (0,0,0)

class Alien(Hero):
    '''
    child class from Hero Parent Class
    ''' 
    def moveRight(self):
        self.rect.x += 1

    def moveLeft(self):
        self.rect.x -= 1
        

 