
import pygame
import game_constants as const
import ball
import paddle


# METHODS



# PYGAME INITIALIZE
pygame.init()


# GAME VARIABLES
running = True
game_surface = pygame.display.set_mode((const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT))
game_width_surface = game_surface.get_width()
game_height_surface = game_surface.get_height()
clock = pygame.time.Clock()

p1_paddle = paddle.Paddle(1)
p2_paddle = paddle.Paddle(3)

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
        if p1_paddle.y > 0: 
            if keys_list[pygame.K_w]:
                p1_paddle.move(-6)
        if p1_paddle.y < game_height_surface - p1_paddle.height:
            if keys_list[pygame.K_s]:
                p1_paddle.move(6)
        

        if p2_paddle.y > 0: 
            if keys_list[pygame.K_UP]:
                p2_paddle.move(-6)
        if p2_paddle.y < game_height_surface - p2_paddle.height:
            if keys_list[pygame.K_DOWN]:
                p2_paddle.move(6)



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
        
        if p1_paddle.colliderect(game_ball):
            game_ball.reverseX()
            #ball_move_Y *= -1
        elif p2_paddle.colliderect(game_ball):
            game_ball.reverseX()
            #ball_move_Y *= -1

        game_ball.move(game_ball.speedX,game_ball.speedY)

        # Calculate score

    else:
        startGameMessage_surface = score_font.render(f"PRESS ANY KEY TO START",0,(255,255,255))
        game_surface.blit(startGameMessage_surface,(game_width_surface/2 - startGameMessage_surface.get_width()/2,4*game_height_surface/10))

    # Render
    score_surface = score_font.render(f"SCORE: P1 {scoreP1} | P2 {scoreP2}",0,(255,255,255))
    game_surface.blit(score_surface,(game_width_surface/2 - score_surface.get_width()/2,game_height_surface/12))

    pygame.draw.rect(game_surface,"red",p1_paddle)
    pygame.draw.rect(game_surface,"green",p2_paddle)
    pygame.draw.rect(game_surface,"white",game_ball)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()





