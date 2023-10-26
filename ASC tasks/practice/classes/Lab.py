import pygame
import random

pygame.init()

GREEN = (0, 128, 0)
NAVY = (0, 0, 128)

size = (1200, 800)
screen = pygame.display.set_mode(size)

class Rectangle():
    def __init__ (self):
        self.x = random.randrange(1,1200)
        self.y = random.randrange(1,800)
        self.height = random.randrange(20,70)
        self.width = random.randrange(20,70)
        self.change_x = random.randrange(-3,3)
        self.change_y = random.randrange(-3,3)
        


    def draw(self,draw_screen,color):
        pygame.draw.rect(draw_screen,color,[self.x,self.y, self.height,self.width], 0)
    
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

class Ellipse(Rectangle):
    def draw(self,draw_screen,color):
        pygame.draw.ellipse(draw_screen,color,[self.x,self.y, self.height,self.width], 0)
my_list = []
for i in range(1000):
    my_object = Rectangle()
    my_list.append(my_object)

for i in range(1000):
    my_object = Ellipse()
    my_list.append(my_object)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(NAVY)

    for i in my_list:
        r = random.randrange(0,255)
        g = random.randrange(0,255)
        b = random.randrange(0,255)
        Color = (r,g,b)
        i.draw(screen,Color)
   # my_object.draw(screen)
   # my_object.move()
    pygame.display.flip()

pygame.quit()