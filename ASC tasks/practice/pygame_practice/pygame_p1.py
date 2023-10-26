# importing pygame
import pygame
import math


#Colors
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



# start 
pygame.init()

size = (800,600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('My practice')
done = False
sun_x = 0
sun_y = 580


clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # end if
    # next event
    
    screen.fill(BLACK)

    pygame.draw.rect(screen, BROWN, (340,400,120,200))
    pygame.draw.rect(screen, CYAN, (360,450,20,40))
    pygame.draw.rect(screen, CYAN, (420,450,20,40))

    pygame.draw.rect(screen, GREEN, (375,540,50,70))

    sun_x += 1
    if sun_x > 800:
        sun_x = 0
    
    sun_y += 0.1   
    
    pygame.draw.circle(screen, YELLOW, [sun_x, (300 * math.cos(0.0769*sun_y)+300)], 20)

    pygame.display.flip()


    clock.tick(60)


# end while

pygame.quit()
# end