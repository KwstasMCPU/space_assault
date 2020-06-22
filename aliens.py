import pygame
from hero import Hero
from random import randint
import time

BLACK = (0,0,0)

class Alien(Hero):
    '''
    child class from Hero Parent Class
    '''

    def moveRandomY(self, pixels):
        self.rect.y += pixels.pop()
        if self.rect.y < 100:
            self.rect.y = 100
        if self.rect.y > 300:
            self.rect.y = 300
       
    
    def moveRandomX(self, pixels):
        self.rect.x += pixels.pop()
        if self.rect.x < 300:
            self.rect.x = 300
        if self.rect.x > 400:
            self.rect.x = 400
        

 