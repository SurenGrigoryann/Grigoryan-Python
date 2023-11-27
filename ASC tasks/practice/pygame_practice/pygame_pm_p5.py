# importing libraries
import pygame
import random
 

 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0) 
PINK = (255, 192, 203)
BROWN = (150,75,0)


Ghost_colors = [PINK,BROWN,WHITE]
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
# creating the class for the player
class Player(pygame.sprite.Sprite):
    
    # Constructor function
    def __init__(self, x, y):
        
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(YELLOW)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
    # end procedure

    def changespeed(self, x, y):
        # changing the speed of the player
        self.change_x += x
        self.change_y += y
    # end procedure


    def update(self):
        # updating player's position
        # Move left/right
        self.rect.x += self.change_x
 
        # Checking if we hit anything horizontally
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            # end if
        # next block
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Checking if we hit anything vertically
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
            # end if
        # next block
# end class Player
 
class Block(pygame.sprite.Sprite):
    # Creating a class block in which player cannot collide to
    def __init__(self, x, y):
        # Creating cunstructor function
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue block with 40 heigth and 40 width
        self.image = pygame.Surface([40,40])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    # end procedure
    
 
# Creating ghost class
class Ghost(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y,color):
        
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
    # end procedure

    def changespeed(self, x, y):
        # changing the speed of the player
        self.change_x += x
        self.change_y += y
    # end procedure


    #def update(self):

# end class



# Initializing pygame
pygame.init()
 
# Create the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Seting the title of the window
pygame.display.set_caption('Packman')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
wall_list = pygame.sprite.Group()

# creating the map
map = [[1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,1],
       [1,1,0,1,1,1,1,1,0,1],
       [1,0,0,0,0,0,1,0,0,1],
       [1,0,1,1,1,0,1,0,0,1],
       [1,0,1,1,1,0,1,0,0,1],
       [1,0,1,1,1,0,1,0,0,1],
       [1,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1]]
# starting coordinates for wall
x = 0
y = 0
for i in map:
    for j in i:
        if j == 1:
            wall = Block(x, y)
            wall_list.add(wall)
            all_sprite_list.add(wall)
            
        x += 40
    x = 0
    y += 40


# creating the player
player = Player(50, 50)
player.walls = wall_list
all_sprite_list.add(player)
 

# creating 3 ghosts spreaded in the map
ghost = Ghost(50, 350, PINK)
all_sprite_list.add(ghost)

ghost = Ghost(200, 200, PINK)
all_sprite_list.add(ghost)

ghost = Ghost(300, 50, PINK)
all_sprite_list.add(ghost)
# and adding everything to the all_sprite_list

all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False

# Main loop
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
 
    # updating all of the objects
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
    # drawing everything
    pygame.display.flip()
    # fliping the display
    clock.tick(60)
 
pygame.quit()
# quiting the pygame

