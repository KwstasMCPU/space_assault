import pygame, time
from space_assault.envs.hero import Hero
from space_assault.envs.aliens import Alien
from space_assault.envs.hero_lazer import Lazer
from space_assault.envs.alien_lazer import Alien_lazer
from random import randrange, choice, choices, randint
from datetime import datetime
import gym
from gym import error, spaces, utils
from gym.utils import seeding

# difficulty
easy = 2000
normal = 1000
hard = 400
epic = 50 # hidden difficulty
nightmare = 10
difficulty = 1000
# Setting colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RED = (255, 0, 0)
PURPLE = (128,0,128)
# Hero spacehip
hero_width = 10
hero_height = 20
hero_health = 3
hero_spaceship = Hero(WHITE, hero_height, hero_width, hero_health)
hero_spaceship.rect.x = 350
hero_spaceship.rect.y = 700

alien_height = 10
alien_width = 10
alien_health = 1
alien_direction_list = []   #
alien_pos_list = []         # both alien_direction_list and alien_pos_list are used in order to determine the initial position and direction, which are used in the alien_movement function
margin = 60                 # the initial distance between aliens
screen_size = (700 , 750)

class SpaceAssault(gym.Env):
    metadata = {'render.modes': ['human']}
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Space Invaders')

        self.score = 0

        self.clock = pygame.time.Clock()


        self.all_sprites_list = pygame.sprite.Group()
        self.alien_vessels_list = pygame.sprite.Group()
        self.hero_lazer_list = pygame.sprite.Group()
        self.alien_lazer_list = pygame.sprite.Group()

        self.alien_generator(GREEN)
        self.hero_spaceship = self.hero_generator()
        self.shoot_time = datetime.now()
        self.done = False
        self.fps = 0
        self.fps_last_considered_frame = datetime.now()
        self.frames_count = 0
        self.action_space = spaces.Discrete(5)

    def check_shooting_condition(self):
        if(self.frames_count%10==0):
            return True
        return False

    def count_fps(self):
        self.frames_count+=1
        delta = datetime.now() - self.fps_last_considered_frame
        if(delta.seconds>=1):
            self.fps = self.frames_count
            self.frames_count=0
            self.fps_last_considered_frame = datetime.now()

    def alien_generator(self, alien_color):
        '''
        multiplies the alien object on the screen.
        setting up the x,y coordinates with the value of margin between them
        '''
        for x in range(margin, screen_size[0] - margin, margin):

            for y in range(margin, int(screen_size[1]/2), margin):
                alien_vessel = Alien(alien_color, alien_height, alien_width, alien_health, x)
                alien_vessel.rect.x = x
                alien_vessel.rect.y = y
                self.alien_vessels_list.add(alien_vessel)
                self.all_sprites_list.add(alien_vessel)

    def hero_generator(self):
        hero = Hero(WHITE, hero_height, hero_width, hero_health)
        hero.rect.x = 350
        hero.rect.y = 700
        self.all_sprites_list.add(hero)
        return hero

    def alien_movement_and_attacking(self):
        '''
        sets the movement of the alien instances.
        the Alien class has a get__initial_pos and get_initial_dir method which gets their initial x,y coordinations and direction(left or right),
        those are stored within relevant lists ( alien_pos_list and alien_direction_list).
        '''    
        for alien in self.alien_vessels_list:
            alien_attack = choices([True, False], weights=[1, difficulty])
            if alien_attack[0] == True:
                alien_lazer_shoot = Alien_lazer(PURPLE, 4, 5, 1)
                alien_lazer_shoot.rect.x = alien.rect.x
                alien_lazer_shoot.rect.y = alien.rect.y
                self.all_sprites_list.add(alien_lazer_shoot)
                self.alien_lazer_list.add(alien_lazer_shoot)
            if alien.direction:
                alien.moveLeft()
            else:
                alien.moveRight()
            if alien.rect.x < (alien.the_initialest_pos - choice([10, 20])):
                alien.moveRight()
                alien.direction = not alien.direction
            if alien.rect.x > (alien.the_initialest_pos + choice([10, 20])):
                alien.moveLeft()
                alien.direction = not alien.direction

    def remove_lazers_from_screen(self):
            for lazer in self.hero_lazer_list:
                if lazer.rect.y < 0:
                    self.hero_lazer_list.remove(lazer)
                    self.all_sprites_list.remove(lazer)

            for lazer in self.alien_lazer_list:
                if lazer.rect.y > 750:
                    self.alien_lazer_list.remove(lazer)
                    self.all_sprites_list.remove(lazer)

    def step(self, action):
        if action==0:
            self.hero_spaceship.moveUp(5)
        if action==1:
            self.hero_spaceship.moveDown(5)
        if action==2:
            self.hero_spaceship.moveLeft(5)
        if action==3:
            self.hero_spaceship.moveRight(5)
        if (action==4 and self.check_shooting_condition()):
            self.shoot_time = datetime.now()
            hero_lazer_shoot = Lazer(RED, 4, 5, 1)
            hero_lazer_shoot.rect.x = self.hero_spaceship.rect.x + 5
            hero_lazer_shoot.rect.y = self.hero_spaceship.rect.y
            self.all_sprites_list.add(hero_lazer_shoot)
            self.hero_lazer_list.add(hero_lazer_shoot)
        self.all_sprites_list.update()    
        self.alien_movement_and_attacking()
        self.remove_lazers_from_screen()

        hero_lazer_to_aliens_collision = pygame.sprite.groupcollide(self.hero_lazer_list, self.alien_vessels_list, True, True)
        alien_lazer_to_hero_collision = pygame.sprite.spritecollide(self.hero_spaceship, self.alien_lazer_list, True)
        reward = 0
        if hero_lazer_to_aliens_collision:
            self.score += 1
            reward = 1
        if alien_lazer_to_hero_collision:
            self.hero_spaceship.health -= 1
            self.score -= 3
            reward = -3
            # check if hero vessel is destroyed
        if self.hero_spaceship.health == 0:
            self.all_sprites_list.remove(hero_spaceship)
            self.done = True
            # check if all enemies are destroyed
        if len(self.alien_vessels_list) == 0:
            self.all_sprites_list.remove(hero_spaceship)
            # remove any lazers hovering the screen
            for lazer in self.hero_lazer_list:
                lazer.kill()
            reward = 10
        self.count_fps()
        return self.all_sprites_list, reward, self.done, {}

    def reset(self):
        for item in self.all_sprites_list:
            item.kill()
        for item in self.hero_lazer_list:
            item.kill()
        for item in self.alien_vessels_list:
            item.kill()
        for item in self.alien_lazer_list:
            item.kill()

        self.alien_generator(GREEN)
        self.hero_spaceship = self.hero_generator()
        self.score = 0
        self.done = False
        return self.all_sprites_list
        
    def render(self, mode='human'):
        self.screen.fill(BLACK)
        self.all_sprites_list.draw(self.screen)

        font = pygame.font.Font("/home/michal/Repos/space-assault/space_assault/envs/AtariSmall.ttf", 30)# definitely to change

        fps_sign = font.render(str('fps:'), 1, WHITE)
        self.screen.blit(fps_sign, (400, 10))

        fps = font.render(str(self.fps), 1, WHITE)
        self.screen.blit(fps, (460, 10))

        score_sign = font.render(str('score:'), 1, WHITE)
        self.screen.blit(score_sign, (540, 10))

        text = font.render(str(self.score), 1, WHITE)
        self.screen.blit(text, (660, 10))

        pygame.display.flip()

    def close(self):
        pygame.quit()