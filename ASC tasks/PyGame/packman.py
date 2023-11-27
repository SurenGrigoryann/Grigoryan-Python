import pygame



BLUE = (0, 0, 255)



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

class title(pygame.sprite.Sprite):

    def __init__(self,color,width,height, x_ref, y_ref):

        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x_ref
        self.rect.y = y_ref

all_sprites_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

for y in range(10):
    for x in range(10):
        if map[x][y] == 1:
            my_wall = title(BLUE,20,20,x*20,y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)


            


        