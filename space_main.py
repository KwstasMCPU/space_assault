import os, sys
import pygame
import time
from hero import Hero


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
hero_spaceship = Hero(WHITE,15,25)
hero_spaceship.rect.x = 350
hero_spaceship.rect.y = 600

all_sprites_list = pygame.sprite.RenderPlain(hero_spaceship)


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


    all_sprites_list.update()
    

    # Drawing
    # screen to black
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip()

    # end of main loop
pygame.quit()