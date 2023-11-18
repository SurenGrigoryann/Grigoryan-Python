import pygame
import time
import math

"""""""""
Task at hand:

- Static house (middle bottom of screen)
  - Windows
  - Chimney
  - Frame (using a triangle)

- Sun moving across the screen from LEFT to RIGHT (from x = 0 to x = length of screen)
- Changes colour from night when x-coordinate out of bounds

"""""""""

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
x_circle = 0
y_circle = 0.1
colour_change = 0
incr = 0.6

size = (800, 600) # Standard 4:3 ratio

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sunrise / Sunset")

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
  
    # Clear the screen and set the screen background
    screen.fill(NAVY)

    #CHANGING BACKGROUND
    colour_change += incr
    if colour_change > 254:
      incr = -0.6
    elif colour_change < 1:
      incr = 0.6
    screen.fill((0, colour_change, 255))

    # pygame.draw.rect(screen, COLOUR, [X_COORD, Y_COORD, WIDTH, HEIGHT], BORDER_THICKNESS)

    # HOUSE
    pygame.draw.rect(screen, MAROON, [300, 400, 200, 200], 0)

    #CHIMNEY

    pygame.draw.rect(screen, MAROON, [425, 300, 40, 80], 0)

    #WINDOWS

    #WINDOW TOP LEFT
    pygame.draw.rect(screen, (255-colour_change, 255, colour_change), [320, 420, 60, 60], 0)

    #WINDOW TOP RIGHT
    pygame.draw.rect(screen, (255-colour_change, 255, colour_change), [420, 420, 60, 60], 0)

    #DOOR

    pygame.draw.rect(screen, BROWN, [375, 540, 50, 60], 0)

    #DOORKNOB
    pygame.draw.circle(screen, YELLOW, [385, 570], 5)

    #ROOF
    pygame.draw.polygon(screen, BROWN, [(290, 400), (510, 400), (400, 300)], 0)

    #MOVING CIRCLE
    x_circle += 1
    if x_circle > 800:
        x_circle = 0
    
    y_circle += 0.1
    pygame.draw.circle(screen, YELLOW, [x_circle, (300 * math.cos(0.0769*y_circle)+300)], 20)

    # Font, size, bold, italics
    font = pygame.font.SysFont('Palatino', 20, False, True)

    # "True" = anti-aliased.
    # Creates image only.

    text = font.render("Watch the Sun rise and fall!", True, SILVER)
    screen.blit(text, [280, 30])

    font = pygame.font.SysFont('Palatino', 20, True, True)
    text = font.render("!! SO AMAZING !!", True, SILVER)
    screen.blit(text, [320, 60])

    # Update screen
    pygame.display.flip()

    # 60 updates per second.
    clock.tick(60)

pygame.quit()

