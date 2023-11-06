import random
import pygame
import time
import math


pygame.init()

#COLOURS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
SILVER = (192, 192, 192)
GREY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)

BROWN = (150, 75, 0)

#INITIALISATIONS
PI = 3.141592653

size = (800, 600) # Standard 4:3 ratio

screen = pygame.display.set_mode(size)

pygame.display.set_caption("LET IT SNOW")

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # classes
    class Snow(pygame.sprite.Sprite):


        # constructor function

        def __init__(self,S_width,S_length,x,y):
            super().__init__()
            self.width = S_width
            self.length = S_length
            self.y_pos = y
            self.x_pos = x
            self.image = pygame.surface.Surface(S_width,S_length )
            self.image.fill(WHITE)
            self.speed = 5
            self.rect = self.image.get_rect()
            self.rect.x 
        # end class snow
    snow_list = []
    number_of_flakes = 15
    for i in range(number_of_flakes):
        flake = Snow(10,10,random.randint(0,500),100)
        snow_list.append(flake)
        # next i 

    # end for


    screen.fill(BLUE)

    snow_list.draw(screen)


    # 60 updates per second.
    clock.tick(60)

pygame.quit()