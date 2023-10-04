import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the window
WIDTH, HEIGHT = 400, 300
BG_COLOR = (0, 0, 0)  # Background color (black)
RECT_COLOR = (255, 0, 0)  # Red color

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw a red rectangle
    pygame.draw.rect(screen, RECT_COLOR, (100, 100, 200, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
