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
font = pygame.font.Font(None,25)


clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # end if
    # next event
    
    screen.fill(WHITE)


    text = font.render('My Text', True, RED)

    screen.blit(text,[100,100])
    # for i in range(200):
 
    #     radians_x = i / 20
    #     radians_y = i / 6
 
    #     x = int(75 * math.sin(radians_x)) + 200
    #     y = int(75 * math.cos(radians_y)) + 200
 
    #     pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)
    # for x_offset in range(30, 300, 30):
    #     pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)
    #     pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)

    pygame.display.flip()


    clock.tick(60)


# end while

pygame.quit()
# end