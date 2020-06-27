import pygame, time
from hero import Hero
from aliens import Alien
from hero_lazer import Lazer
from random import randrange, choice, randint

pygame.init() # Prepare the pygame module for use

# setting up the screen
screen_size = (700 , 750)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Space Invaders')

# setting colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RED = (255, 0, 0)

# setting the clock
clock = pygame.time.Clock()

#setting sounds
crash_effect = pygame.mixer.Sound('alien_vessel_explosion.wav') # sound effect from https://www.zapsplat.com/
lazer_sound = pygame.mixer.Sound('lazer_shoot1.wav') # sound effect from https://www.zapsplat.com/

#sprites
all_sprites_list = pygame.sprite.Group()
alien_vessels_list = pygame.sprite.Group()
lazer_list = pygame.sprite.Group()
# hero spacehip
hero_width = 10
hero_height = 20
hero_spaceship = Hero(WHITE, hero_height, hero_width)
hero_spaceship.rect.x = 350
hero_spaceship.rect.y = 700
all_sprites_list.add(hero_spaceship)
# alien vessels
alien_height = 10
alien_width = 10
alien_direction_list = []   #
alien_pos_list = []         # both alien_direction_list and alien_pos_list are used in order to determine the initial position and direction, which are used in the alien_movement function
margin = 60                 # the initial distance between aliens
# setting up the lists
# alien generator
def alien_generator(alien_color):
    '''
    multiplies the alien object on the screen.
    setting up the x,y coordinates with the value of margin between them
    '''
    for x in range(margin, screen_size[0] - margin, margin):
        for y in range(margin, int(screen_size[1]/2), margin):
            alien_vessel = Alien(alien_color, alien_height, alien_width)
            alien_vessel.rect.x = x
            alien_vessel.rect.y = y
            alien_pos_list.append(alien_vessel.get_initial_pos())
            alien_direction_list.append(alien_vessel.get_initial_dir())
            alien_vessels_list.add(alien_vessel)
            all_sprites_list.add(alien_vessel)

alien_generator(GREEN)

# alien movement
def alien_movement(alien_vessels_list, i):
    '''
    sets the movement of the alien instances.
    the Alien class has a get__initial_pos and get_initial_dir method which gets their initial x,y coordinations and direction(left or right),
    those are stored within relevant lists ( alien_pos_list and alien_direction_list).
    '''
    for alien in alien_vessels_list:
        if alien_direction_list[i]:
            alien.moveLeft()
        else:
            alien.moveRight()
        if alien.rect.x < (alien_pos_list[i] - choice([10, 20])):
            alien.moveRight()
            alien_direction_list[i] = not alien_direction_list[i]
        if alien.rect.x > (alien_pos_list[i] + choice([10, 20])):
            alien.moveLeft()
            alien_direction_list[i] = not alien_direction_list[i]
        i += 1

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
                        lazer_shoot = Lazer(RED, 4, 5)
                        lazer_shoot.rect.x = hero_spaceship.rect.x + 5
                        lazer_shoot.rect.y = hero_spaceship.rect.y
                        lazer_sound.play()
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
        if lazer.rect.y < 0:
            lazer_list.remove(lazer)
            all_sprites_list.remove(lazer)

    # alien moveshet
    i = 0
    alien_movement(alien_vessels_list, i)

    # See if the lazer block has collided with anything. if yes both lazer and aliens are removed from their lists
    collisions = pygame.sprite.groupcollide(lazer_list, alien_vessels_list, True, True)
    if collisions:
        crash_effect.play()

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