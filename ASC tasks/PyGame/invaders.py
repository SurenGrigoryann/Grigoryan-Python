# importing libraries
import pygame
import random
import math

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = 	(128, 128, 128)

# classes

class Block(pygame.sprite.Sprite):
    # block_speed needed
    # constructor function
    def __init__(self,color):

        super().__init__()

        self.image = pygame.Surface([16,16])
        self.image.fill(color)

        self.rect = self.image.get_rect()
    # end constructor function

    def update(self):
        self.rect.y += 0.5
    # end function
# end class

class Player(pygame.sprite.Sprite):
    # constructor function
    def __init__(self):

        super().__init__()

        self.image = pygame.Surface([16,16])
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
    # end constructor function
# end class


 #   def change(self,change_speed):
  #      self.rect.x += change_speed

class Bullet(pygame.sprite.Sprite):
    # constructor function
    def __init__(self):
        
        super().__init__()

        self.image = pygame.Surface([4,4])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
    # end constructor function

    def update(self):
        self.rect.y -= 3
    # end function
# end class


# Initialize Pygame

pygame.init()

# screen parametrs
screen_width = 900
screen_length = 600
screen = pygame.display.set_mode([screen_width, screen_length])

# lists
all_sprite_list = pygame.sprite.Group()

block_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()

lose_life_list = pygame.sprite.Group()



for i in range(20):
    block = Block(BLUE)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_length//2)

    block_list.add(block)
    all_sprite_list.add(block)
# next i

player = Player()
all_sprite_list.add(player)

done = False

clock = pygame.time.Clock()
lives = 20
score = 0

player.rect.y = 550
player.rect.x = 400
speed = 0
bullets = 100  

font = pygame.font.Font(None,25)

# main loop
while not done:
    
    player.rect.x += speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed += 4
            if event.key == pygame.K_LEFT:
                speed -= 4
            #player.change(speed)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed  -= 4
            if event.key == pygame.K_LEFT:
                speed += 4
            #player.change(speed)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()

            bullet.rect.x = player.rect.x + 8
            bullet.rect.y = player.rect.y

            all_sprite_list.add(bullet)
            bullet_list.add(bullet)
            bullets -= 1

    all_sprite_list.update()
    
    if lives <= 0:
        done = True
        print('You lost!')


    for bullet in bullet_list:

        block_hit_list = pygame.sprite.spritecollide(bullet,block_list,True)

        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprite_list.remove(bullet)
            score += 1
        # next block 

        if bullet.rect.y <= -10:
            bullet_list.remove(bullet)
            all_sprite_list.remove(bullet)
        # end if
    # next bullet

    for block in block_list:
        
        if block.rect.y >= screen_length:
            block_list.remove(block)
            all_sprite_list.remove(block)
            block = Block(BLUE)

            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_length//2 - 250,screen_length//2 - 200)

            block_list.add(block)
            all_sprite_list.add(block)
                    
            lives -= 1
        
        # end if
    # next block
    
    


    screen.fill(BLACK)

    live_print = font.render(f'Lives: {lives}', True, WHITE)
    score_print = font.render(f'Score: {score}', True, WHITE)
    bullets_print = font.render(f'Bullets left: {bullets}', True, WHITE)
    screen.blit(live_print,[100,50])
    screen.blit(score_print,[100,100])
    screen.blit(bullets_print,[100,150])

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
# quiting pygame