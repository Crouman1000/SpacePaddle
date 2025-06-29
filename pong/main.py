
import pygame
import random

# CONSTANTS

SURFACE_WIDTH = 1280
SURFACE_HEIGHT = 720
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 150
BALL_RADIUS = 20

# pygame setup
pygame.init()

# GAME VARIABLES
surface = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
clock = pygame.time.Clock()
running = True
p1_posY = SURFACE_HEIGHT/2
p2_posY = SURFACE_HEIGHT/2
p1_paddle = pygame.Rect(100,p1_posY,PADDLE_WIDTH,PADDLE_HEIGHT)
p2_paddle = pygame.Rect(SURFACE_WIDTH - 100,p2_posY,PADDLE_WIDTH,PADDLE_HEIGHT)
ball_posX = SURFACE_WIDTH/2
ball_posY = SURFACE_HEIGHT/2

ball = pygame.Rect(ball_posX,ball_posY,BALL_RADIUS,BALL_RADIUS)
ball_move_X = 5*random.choice([-1,1])
ball_move_Y = 5*random.choice([-1,1])

while running:
    # Poll for events
    for event in pygame.event.get():
        #print(f"event: {event}")
        if event.type == pygame.QUIT:
            running = False

    # Wipe away last frames
    surface.fill("black")

    # Calculate paddle's positions
    keys_list = pygame.key.get_pressed()
    if p1_posY > 0: 
        if keys_list[pygame.K_w]:
            p1_posY = p1_posY - 6
            p1_paddle.y = p1_posY
    if p1_posY < SURFACE_HEIGHT - PADDLE_HEIGHT:
        if keys_list[pygame.K_s]:
            p1_posY = p1_posY + 6
            p1_paddle.y = p1_posY
    
    if p2_posY > 0: 
        if keys_list[pygame.K_UP]:
            p2_posY = p2_posY - 6
            p2_paddle.y = p2_posY
    if p2_posY < SURFACE_HEIGHT - PADDLE_HEIGHT:
        if keys_list[pygame.K_DOWN]:
            p2_posY = p2_posY + 6
            p2_paddle.y = p2_posY



    # Calculate ball position
    
    if ball_posY <= 0 or ball_posY >= SURFACE_HEIGHT: 
        ball_move_Y *= -1
    if ball_posX <= 0 or ball_posX >= SURFACE_WIDTH: 
        ball_move_X *= -1

    # Handle collisions
    
    if p1_paddle.colliderect(ball):
        ball_move_X *= -1
        #ball_move_Y *= -1
    elif p2_paddle.colliderect(ball):
        ball_move_X *= -1
        #ball_move_Y *= -1

    ball_posX = ball_posX + ball_move_X
    ball_posY = ball_posY + ball_move_Y
        
    ball.x = ball_posX
    ball.y = ball_posY
        
    # Calculate score

    # EXPERIMENTAL

    # Render
    pygame.draw.rect(surface,"red",p1_paddle)
    pygame.draw.rect(surface,"green",p2_paddle)
    pygame.draw.rect(surface,"white",ball)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

