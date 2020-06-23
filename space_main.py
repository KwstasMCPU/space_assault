import os, sys
import pygame
import time
from hero import Hero
from aliens import Alien
from hero_lazer import Lazer
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
alien_width = 20
alien_height = 15
alien_vessel = Alien(WHITE, alien_width, alien_height)
alien_vessel.rect.x = 350
alien_vessel.rect.y = 150
move_left = True
# setting up the lists
lazer_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(hero_spaceship)
all_sprites_list.add(alien_vessel)


#-------------- main program loop
RUNNING = True
while RUNNING:

#-------------- polls for events 
    # quiting game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            RUNNING = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE: 
                RUNNING = False
            # lazer gun # space for shoot
            if event.key==pygame.K_SPACE: 
                        lazer_shoot = Lazer(WHITE, 4, 5)
                        lazer_shoot.rect.x = hero_spaceship.rect.x
                        lazer_shoot.rect.y = hero_spaceship.rect.y
                        all_sprites_list.add(lazer_shoot)
                        lazer_list.add(lazer_shoot)
    # controling hero spacehip  # arrow keys for movment
    keys = pygame.key.get_pressed()
    # moving the spaceship
    if keys[pygame.K_UP]:
        hero_spaceship.moveUp(5)
    if keys[pygame.K_DOWN]:
        hero_spaceship.moveDown(5) 
    if keys[pygame.K_LEFT]:
        hero_spaceship.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        hero_spaceship.moveRight(5)
         
    # --- Game logic
    all_sprites_list.update()

    # lazer mechanics
    # remove lazer if flies off the screen
    for lazer in lazer_list:
        if lazer.rect.y < -1:
            lazer_list.remove(lazer)
            all_sprites_list.remove(lazer)

    
     
    # alien moveshet
    if move_left == True:
        alien_vessel.moveLeft()
    else:
        alien_vessel.moveRight()
    if alien_vessel.rect.x < 300:
        move_left = False
    if alien_vessel.rect.x > 400:
        move_left = True
    
    
    
    # Drawing
    # Clear the screan (screen to black)
    screen.fill(BLACK)

    # Draw all the sprites
    all_sprites_list.draw(screen)

    # update the screen with the drawn
    pygame.display.flip()
    
    # limit fps
    clock.tick(60)

    # end of main loop
pygame.quit()