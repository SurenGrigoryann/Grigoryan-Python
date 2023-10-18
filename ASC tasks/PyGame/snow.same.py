# This is snowflakes.

import pygame
import random
import math

pygame.init()

WHITE = (255, 255, 255)
NAVY = (0, 0, 128)

size = (800, 600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snowflakes")

done = False
clock = pygame.time.Clock()

# CLASSES
class Snow(pygame.sprite.Sprite):

    #CONSTRUCTORS
    def __init__(self, s_width, s_length):
        super().__init__()

        self.image= pygame.Surface([s_width, s_length])
        self.image.fill(WHITE)
        self.speed = random.randrange(1,20)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = random.randrange(0, 600)
    #end def

    def update(self):
        if self.rect.y > 600:
            self.rect.y = -50
        else:
            self.rect.y = self.rect.y + self.speed
    #end def
#end class

#GLOBAL VARIABLES
snow_group = pygame.sprite.Group()
number_of_flakes = 10000
for i in range(0, number_of_flakes):
    flake = Snow(1, 1)
    snow_group.add(flake)
#end for

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #end if
    #end for
  
    # Clear the screen and set the screen background
    screen.fill(NAVY)

    snow_group.draw(screen)
    snow_group.update()

    pygame.display.flip()

    # 60 updates per second.
    clock.tick(60)
#end while

