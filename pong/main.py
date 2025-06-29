
import pygame
import random

# METHODS

def resetBallPosition():

    global ball
    global ball_posX
    global ball_posY
    global ball_move_X
    global ball_move_Y

    
    ball_posX = GAME_SURFACE_WIDTH/2
    ball_posY = GAME_SURFACE_HEIGHT/2   
    ball_move_X = 5*random.choice([-1,1])
    ball_move_Y = 5*random.choice([-1,1])
    ball = pygame.Rect(ball_posX,ball_posY,BALL_RADIUS,BALL_RADIUS)



# CONSTANTS

GAME_SURFACE_WIDTH = 1280
GAME_SURFACE_HEIGHT = 720
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 150
BALL_RADIUS = 20

# pygame setup
pygame.init()

# GAME VARIABLES
game_surface = pygame.display.set_mode((GAME_SURFACE_WIDTH, GAME_SURFACE_HEIGHT))
clock = pygame.time.Clock()
running = True
p1_posY = GAME_SURFACE_HEIGHT/2
p2_posY = GAME_SURFACE_HEIGHT/2
p1_paddle = pygame.Rect(100,p1_posY,PADDLE_WIDTH,PADDLE_HEIGHT)
p2_paddle = pygame.Rect(GAME_SURFACE_WIDTH - 100,p2_posY,PADDLE_WIDTH,PADDLE_HEIGHT)
ball_posX = GAME_SURFACE_WIDTH/2
ball_posY = GAME_SURFACE_HEIGHT/2   
ball_move_X = 5*random.choice([-1,1])
ball_move_Y = 5*random.choice([-1,1])
ball = pygame.Rect(ball_posX,ball_posY,BALL_RADIUS,BALL_RADIUS)



scoreP1 = 0
scoreP2 = 0
score_font = pygame.font.SysFont("Arial",30,True,False)

startGame = False

while running:
    # Poll for events
    for event in pygame.event.get():
        #print(f"event: {event}")
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            startGame = True
            

    if startGame:

        # Wipe away last frames
        game_surface.fill("black")

        # Calculate paddle's positions
        keys_list = pygame.key.get_pressed()
        if p1_posY > 0: 
            if keys_list[pygame.K_w]:
                p1_posY = p1_posY - 6
                p1_paddle.y = p1_posY
        if p1_posY < GAME_SURFACE_HEIGHT - PADDLE_HEIGHT:
            if keys_list[pygame.K_s]:
                p1_posY = p1_posY + 6
                p1_paddle.y = p1_posY
        
        if p2_posY > 0: 
            if keys_list[pygame.K_UP]:
                p2_posY = p2_posY - 6
                p2_paddle.y = p2_posY
        if p2_posY < GAME_SURFACE_HEIGHT - PADDLE_HEIGHT:
            if keys_list[pygame.K_DOWN]:
                p2_posY = p2_posY + 6
                p2_paddle.y = p2_posY



        # Calculate ball position
        
        if ball_posY <= 0 or ball_posY >= GAME_SURFACE_HEIGHT: 
            ball_move_Y *= -1
        if ball_posX <= 0 or ball_posX >= GAME_SURFACE_WIDTH: 
            ball_move_X *= -1
            if ball_posX <= 0:
                print("P2 Scored!")
                scoreP2 += 1
                startGame = False
                resetBallPosition()

            else:
                print("P1 Scored!")
                scoreP1 += 1
                startGame = False
                resetBallPosition()



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
            

        pygame.draw.rect(game_surface,"white",ball)

        # Calculate score

        

    else:
        startGameMessage_surface = score_font.render(f"PRESS ANY KEY TO START",0,(255,255,255))
        game_surface.blit(startGameMessage_surface,(GAME_SURFACE_WIDTH/2 - startGameMessage_surface.get_width()/2,GAME_SURFACE_HEIGHT/2))

    # Render
    score_surface = score_font.render(f"SCORE: P1 {scoreP1} | P2 {scoreP2}",0,(255,255,255))
    game_surface.blit(score_surface,(GAME_SURFACE_WIDTH/2 - score_surface.get_width()/2,GAME_SURFACE_HEIGHT/12))

    pygame.draw.rect(game_surface,"red",p1_paddle)
    pygame.draw.rect(game_surface,"green",p2_paddle)

    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()





