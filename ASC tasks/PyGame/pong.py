import pygame
import random
import time
clock = pygame.time.Clock()
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
x_player1 = 20
y_player1 = 20
x_player2 = 780
y_player2 = 560
x_circle = 600
y_circle = 300

def ball_animation():
    global ball_speed_x,ball_speed_y,player1_score,player2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1 
    if ball.left <= 0:
        player1_score += 1
        ball_restart()
    if ball.right >= SCREEN_WIDTH:
        ball_restart()
        player2_score += 1
        


    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player1 = pygame.Rect((SCREEN_WIDTH - 20,SCREEN_HEIGHT/2 - 15,8,80))
player2 = pygame.Rect((10,SCREEN_HEIGHT/2 - 15,8,80))
ball = pygame.Rect((SCREEN_WIDTH/2 - 10,SCREEN_HEIGHT/2 - 10,20,20))
run = True


ball_speed_x = 4
ball_speed_y = 4
player1_speed = 0
player2_speed = 0 

player1_score = 0
player2_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

while run:

    screen.fill((255,255,255))

    pygame.draw.rect(screen, (255,0,0), player1)
    pygame.draw.rect(screen, (0,0,255), player2)
    pygame.draw.ellipse(screen,(0,255,0), ball)


    player1_txt = game_font.render(f'{player1_score}', False,(200,200,200))
    screen.blit(player1_txt,(420,300))
    player2_txt = game_font.render(f'{player2_score}', False,(200,200,200))
    screen.blit(player2_txt,(380,300))
    # key1 = pygame.key.get_pressed()
    # key2 = pygame.key.get_pressed()
    # if key1[pygame.K_w] == True:
    #     player1_speed += 7     
    # if key1[pygame.K_s] == True:
    #     player1_speed -= 7  
    
    # if key2[pygame.K_UP] == True:
    #   
    #   player2_speed += 7 
    # if key2[pygame.K_DOWN] == True:
    #     player2_speed += 7 
    

    ball_animation()
    player1.y += player1_speed
    player2.y += player2_speed


    if player1.top <= 0:
        player1.top = 0
    elif player1.bottom >= SCREEN_HEIGHT:
        player1.bottom = SCREEN_HEIGHT
    if player2.top <= 0:
        player2.top = 0
    elif player2.bottom >= SCREEN_HEIGHT:
        player2.bottom = SCREEN_HEIGHT




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 4
            if event.key == pygame.K_UP:
                player1_speed -= 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 4
            if event.key == pygame.K_UP:
                player1_speed += 4
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player2_speed += 4
            if event.key == pygame.K_w:
                player2_speed -= 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player2_speed -= 4
            if event.key == pygame.K_w:
                player2_speed += 4
        
    pygame.display.update()
    sec = 60
    clock.tick(sec)

pygame.quit()