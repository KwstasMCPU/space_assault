import os, sys
import pygame
import time
from hero import Hero
from aliens import Alien
from random import choices


pygame.init() # Prepare the pygame module for use

# setting up the screen
size = (700 , 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Invaders')

# setting colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# setting the clock
clock = pygame.time.Clock()

#sprites
# hero spacehip
hero_width = 15
hero_height = 25
hero_spaceship = Hero(WHITE, hero_width, hero_height)
hero_spaceship.rect.x = 350
hero_spaceship.rect.y = 700
# alien vessels
# alien_vessels = []
# for i in range(10)
alien_width = 20
alien_height = 15
alien_vessel = Alien(WHITE, alien_width, alien_height)
alien_vessel.rect.x = 350
alien_vessel.rect.y = 150

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(hero_spaceship)
all_sprites_list.add(alien_vessel)



# main program loop
RUNNING = True
while RUNNING:
    clock.tick(60)

    # polls for events 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            RUNNING = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE: 
                RUNNING = False
    # moving the spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hero_spaceship.moveUp(5)
    if keys[pygame.K_DOWN]:
        hero_spaceship.moveDown(5) 
    if keys[pygame.K_LEFT]:
        hero_spaceship.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        hero_spaceship.moveRight(5)
  
    alien_vessel.moveRandomY(choices([-2,2]))
    alien_vessel.moveRandomX(choices([-2,2]))
    all_sprites_list.update()
    

    # Drawing
    # screen to black
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip()

    # end of main loop
pygame.quit()