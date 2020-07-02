import pygame, time
from hero import Hero
from aliens import Alien
from hero_lazer import Lazer
from alien_lazer import Alien_lazer
from random import randrange, choice, choices, randint

pygame.init() # Prepare the pygame module for use

# Initialise screen screen
screen_size = (700 , 750)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Space Invaders')

# Score
score = 0

# difficulty
easy = 4000
normal = 2600
hard = 1100
epic = 50

# Setting colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RED = (255, 0, 0)
PURPLE = (128,0,128)

# Setting the clock
clock = pygame.time.Clock()

# Setting sounds
crash_effect = pygame.mixer.Sound('sounds/alien_vessel_explosion.wav')  # sound effect from https://www.zapsplat.com/
lazer_sound = pygame.mixer.Sound('sounds/lazer_shoot1.wav')             # sound effect from https://www.zapsplat.com/

# Sprites
# setting up the groups
all_sprites_list = pygame.sprite.Group()
alien_vessels_list = pygame.sprite.Group()
hero_lazer_list = pygame.sprite.Group()
alien_lazer_list = pygame.sprite.Group()

# Hero spacehip
hero_width = 10
hero_height = 20
hero_health = 3
hero_spaceship = Hero(WHITE, hero_height, hero_width, hero_health)
hero_spaceship.rect.x = 350
hero_spaceship.rect.y = 700
all_sprites_list.add(hero_spaceship)
# Alien vessels
alien_height = 10
alien_width = 10
alien_health = 1
alien_direction_list = []   #
alien_pos_list = []         # both alien_direction_list and alien_pos_list are used in order to determine the initial position and direction, which are used in the alien_movement function
margin = 60                 # the initial distance between aliens

# Alien generator
def alien_generator(alien_color):
    '''
    multiplies the alien object on the screen.
    setting up the x,y coordinates with the value of margin between them
    '''
    for x in range(margin, screen_size[0] - margin, margin):
        for y in range(margin, int(screen_size[1]/2), margin):
            alien_vessel = Alien(alien_color, alien_height, alien_width, alien_health)
            alien_vessel.rect.x = x
            alien_vessel.rect.y = y
            alien_pos_list.append(alien_vessel.get_initial_pos())
            alien_direction_list.append(alien_vessel.get_initial_dir())
            alien_vessels_list.add(alien_vessel)
            all_sprites_list.add(alien_vessel)

alien_generator(GREEN)

# Alien movement
def alien_movement_and_attacking(alien_vessels_list, i, difficulty=normal):
    '''
    sets the movement of the alien instances.
    the Alien class has a get__initial_pos and get_initial_dir method which gets their initial x,y coordinations and direction(left or right),
    those are stored within relevant lists ( alien_pos_list and alien_direction_list).
    '''
    for alien in alien_vessels_list:
        alien_attack = choices([True, False], weights=[1, difficulty])
        if alien_attack[0] == True:
            alien_lazer_shoot = Alien_lazer(PURPLE, 4, 5, 1)
            alien_lazer_shoot.rect.x = alien.rect.x
            alien_lazer_shoot.rect.y = alien.rect.y
            lazer_sound.play()
            all_sprites_list.add(alien_lazer_shoot)
            alien_lazer_list.add(alien_lazer_shoot)
        if alien_direction_list[i]:
            alien.moveLeft()
        else:
            alien.moveRight()
        if alien.rect.x < (alien_pos_list[i] - choice([10, 10])):
            alien.moveRight()
            alien_direction_list[i] = not alien_direction_list[i]
        if alien.rect.x > (alien_pos_list[i] + choice([10, 10])):
            alien.moveLeft()
            alien_direction_list[i] = not alien_direction_list[i]
        i += 1

def remove_lazers_from_screen(hero_lazer_list, alien_lazer_list):
        # remove hero lazer if flies off the screen
        for lazer in hero_lazer_list:
            if lazer.rect.y < 0:
                hero_lazer_list.remove(lazer)
                all_sprites_list.remove(lazer)
        # remove alien lazer if flies off the screen
        for lazer in alien_lazer_list:
            if lazer.rect.y > 750:
                alien_lazer_list.remove(lazer)
                all_sprites_list.remove(lazer)

def display_message(font, font_size, message, x, y):
    screen.fill(BLACK)
    font = pygame.font.Font(font, font_size)
    text = font.render(message, 1, WHITE)
    screen.blit(text, (x, y))

def you_lost():
    global LOST_MSG_SCREEN
    screen.fill(BLACK)
    display_message("AtariSmall.ttf", 30, 'Humanity is doomed. Continue? [y]/[n]', 50, 350)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_n or event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key==pygame.K_y:
                for alien in alien_vessels_list:
                    alien.kill()
                alien_generator(GREEN)
                global hero_spaceship
                hero_spaceship = Hero(WHITE, hero_height, hero_width, hero_health)
                hero_spaceship.rect.x = 350
                hero_spaceship.rect.y = 700
                all_sprites_list.add(hero_spaceship)
                LOST_MSG_SCREEN = False
    return LOST_MSG_SCREEN

def you_won():
    global WON_MSG_SCREEN
    screen.fill(BLACK)
    display_message("AtariSmall.ttf", 30, 'YOU SAVED THE HUMAN RACE!! Play again?? [y]/[n]', 50, 350)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_n or event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key==pygame.K_y:
                for alien in alien_vessels_list:
                    alien.kill()
                alien_generator(GREEN)
                global hero_spaceship
                hero_spaceship = Hero(WHITE, hero_height, hero_width, hero_health)
                hero_spaceship.rect.x = 350
                hero_spaceship.rect.y = 700
                all_sprites_list.add(hero_spaceship)
                WON_MSG_SCREEN = False
    return WON_MSG_SCREEN

def paused():
    global PAUSE
    screen.fill(BLACK)
    display_message("AtariSmall.ttf", 30, 'Paused', 300, 350)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                PAUSE = False
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
    return PAUSE

def game_introduction():
    INTRO = True
    while INTRO:
        screen.fill(BLACK)
        display_message("AtariSmall.ttf", 30, 'PRESS \'E\' : Ez, \'N\' : Normal, \'H\' : HARD', 50, 350)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_e:
                    difficulty = easy
                    INTRO = False
                if event.key == pygame.K_n:
                    difficulty = normal
                    INTRO = False
                if event.key == pygame.K_h:
                    difficulty = hard
                    INTRO = False
                # hidden difficulty
                if event.key == pygame.K_1:
                    difficulty = epic
                    INTRO = False
    return difficulty

#-------------- main program loop -------------------------------------------------------------------#
INTRO = True
RUNNING = True
while RUNNING:

    while INTRO:
        game_introduction()
        INTRO = False

#-------------- polls for events
    # quiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                RUNNING = False
            if event.key==pygame.K_p:
                PAUSE = True
                while PAUSE:
                    paused()
            # lazer gun # space for shoot
            if event.key==pygame.K_SPACE:
                        hero_lazer_shoot = Lazer(RED, 4, 5, 1)
                        lazer_sound.play()
                        hero_lazer_shoot.rect.x = hero_spaceship.rect.x + 5
                        hero_lazer_shoot.rect.y = hero_spaceship.rect.y
                        all_sprites_list.add(hero_lazer_shoot)
                        hero_lazer_list.add(hero_lazer_shoot)
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

    # ---- Game logic
    all_sprites_list.update()

    # lazer mechanics
    # remove lazers if fly off the screen
    remove_lazers_from_screen(hero_lazer_list, alien_lazer_list)

    # alien movement
    i = 0
    alien_movement_and_attacking(alien_vessels_list, i, difficulty=normal)

    # Check if the lazer block has collided with anything. If yes both lazer and aliens are removed from their lists
    hero_lazer_to_aliens_collision = pygame.sprite.groupcollide(hero_lazer_list, alien_vessels_list, True, True)
    alien_lazer_to_hero_collision = pygame.sprite.spritecollide(hero_spaceship, alien_lazer_list, True)
    if hero_lazer_to_aliens_collision:
        score += 1
        crash_effect.play()
    if alien_lazer_to_hero_collision:
        crash_effect.play()
        hero_spaceship.health -= 1
        if hero_spaceship.health == 0:
            all_sprites_list.remove(hero_spaceship)
            LOST_MSG_SCREEN = True
            while LOST_MSG_SCREEN:
                you_lost()
    if len(alien_vessels_list) == 0:
        all_sprites_list.remove(hero_spaceship)
        for lazer in hero_lazer_list:
            lazer.kill()
            score = 0
        WON_MSG_SCREEN = True
        while WON_MSG_SCREEN:
            you_won()

    # Drawing
    # Clear the screan (screen to black)
    screen.fill(BLACK)

    # Draw all the sprites
    all_sprites_list.draw(screen)

    # show score
    font = pygame.font.Font("AtariSmall.ttf", 30)
    text = font.render(str(score), 1, WHITE)
    screen.blit(text, (660, 10))

    # update the screen with the drawn
    pygame.display.flip()

    # limit fps
    clock.tick(60)
    # end of main loop
pygame.quit()