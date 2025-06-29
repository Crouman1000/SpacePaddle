
import pygame
import random
import pong.game_constants as const
import pong.ball as ball


# METHODS



# PYGAME INITIALIZE
pygame.init()


# GAME VARIABLES
running = True
game_surface = pygame.display.set_mode((const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT))
clock = pygame.time.Clock()
p1_posY = const.GAME_SURFACE_HEIGHT/2
p2_posY = const.GAME_SURFACE_HEIGHT/2
p1_paddle = pygame.Rect(100,p1_posY,const.PADDLE_WIDTH,const.PADDLE_HEIGHT)
p2_paddle = pygame.Rect(const.GAME_SURFACE_WIDTH - 100,p2_posY,const.PADDLE_WIDTH,const.PADDLE_HEIGHT)

game_ball = ball.Ball()

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
        if p1_posY < const.GAME_SURFACE_HEIGHT - const.PADDLE_HEIGHT:
            if keys_list[pygame.K_s]:
                p1_posY = p1_posY + 6
                p1_paddle.y = p1_posY
        
        if p2_posY > 0: 
            if keys_list[pygame.K_UP]:
                p2_posY = p2_posY - 6
                p2_paddle.y = p2_posY
        if p2_posY < const.GAME_SURFACE_HEIGHT - const.PADDLE_HEIGHT:
            if keys_list[pygame.K_DOWN]:
                p2_posY = p2_posY + 6
                p2_paddle.y = p2_posY



        # Calculate ball position
        
        if game_ball.y <= 0 or game_ball.y >= game_surface.get_height(): 
            game_ball.reverseY()
        if game_ball.x <= 0 or game_ball.x >= game_surface.get_width(): 
            game_ball.reverseX()

            if game_ball.x <= 0:
                print("P2 Scored!")
                scoreP2 += 1
            else:
                print("P1 Scored!")
                scoreP1 += 1       
            startGame = False
            game_ball.reset()



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

    else:
        startGameMessage_surface = score_font.render(f"PRESS ANY KEY TO START",0,(255,255,255))
        game_surface.blit(startGameMessage_surface,(GAME_SURFACE_WIDTH/2 - startGameMessage_surface.get_width()/2,4*GAME_SURFACE_HEIGHT/10))

    # Render
    score_surface = score_font.render(f"SCORE: P1 {scoreP1} | P2 {scoreP2}",0,(255,255,255))
    game_surface.blit(score_surface,(GAME_SURFACE_WIDTH/2 - score_surface.get_width()/2,GAME_SURFACE_HEIGHT/12))

    pygame.draw.rect(game_surface,"red",p1_paddle)
    pygame.draw.rect(game_surface,"green",p2_paddle)
    pygame.draw.rect(game_surface,"white",ball)
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()





