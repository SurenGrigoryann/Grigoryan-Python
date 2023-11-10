# importing
import pygame
import random
 
# Initialize 
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [800, 600]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 

snow_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    snow_list.append([x, y])
 
clock = pygame.time.Clock()
 

done = False
while not done:
 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True   
 
    
    screen.fill(BLACK)
 
    
    for i in range(len(snow_list)):
 
        
        pygame.draw.circle(screen, WHITE, snow_list[i], 1)
 
        
        snow_list[i][1] += 10
 
        
        if snow_list[i][1] > 600:
            
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            
            x = random.randrange(0, 800)
            snow_list[i][0] = x
 
    
    pygame.display.flip()
    clock.tick(20)
 

pygame.quit()