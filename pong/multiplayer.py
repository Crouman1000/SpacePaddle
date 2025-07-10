import pygame
import game_constants as const
import ball
import paddle
import gameText
import sound

def run_multiplayer():

    
    
    clock = pygame.time.Clock()
    #sound.gameplay_sound.play(-1,0,500)

    # GAME VARIABLES
    
    game_surface = pygame.display.set_mode((const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT))
    game_width_surface = game_surface.get_width()
    game_height_surface = game_surface.get_height()


    p1_paddle = paddle.Paddle(const.Player.P1)
    p2_paddle = paddle.Paddle(const.Player.P2)

    game_ball = ball.Ball()

    game_scoreboard = gameText.ScoreBoard("Arial",30,True,False)

    
    running = True
    startGame = False
    while running:
        # Poll for events
        for event in pygame.event.get():
            #print(f"event: {event}")
            if event.type == pygame.QUIT:
                running = False
                startGame = False
                gameState = const.GameState.Off

            elif event.type == pygame.KEYDOWN:
                #print(f"{event.key}=?={pygame.K_ESCAPE}")
                #if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    startGame = False
                    gameState = const.GameState.MainMenu
                else:
                    startGame = True
                
        
        if startGame:

            game_ball.move()

            # Wipe away last frames
            game_surface.fill("black")

            # Calculate paddle's positions
            keys_list = pygame.key.get_pressed()
            if p1_paddle.y > 0: 
                if keys_list[pygame.K_w]:
                    p1_paddle.move(-1*const.PADDLE_SPEED)
            if p1_paddle.y < game_height_surface - p1_paddle.height:
                if keys_list[pygame.K_s]:
                    p1_paddle.move(1*const.PADDLE_SPEED)
            

            if p2_paddle.y > 0: 
                if keys_list[pygame.K_UP]:
                    p2_paddle.move(-1*const.PADDLE_SPEED)
            if p2_paddle.y < game_height_surface - p2_paddle.height:
                if keys_list[pygame.K_DOWN]:
                    p2_paddle.move(1*const.PADDLE_SPEED)

            
            # Handle collisions
            
            if p1_paddle.colliderect(game_ball):
                sound.paddleHit_sound.play()
                p1_paddle.reflectBall(game_ball)
                game_ball.increaseSpeed()
    
            elif p2_paddle.colliderect(game_ball):
                sound.paddleHit_sound.play(0)
                p2_paddle.reflectBall(game_ball)
                game_ball.increaseSpeed()



            # Calculate ball position
            
            if game_ball.y <= 0 or game_ball.y >= game_height_surface: 
                sound.YwallHit_sound.play(0,1000)
                game_ball.reverseY()
            if game_ball.x <= 0 or game_ball.x >= game_width_surface: 
                #game_ball.reverseX()s

                # Calculate score
                if game_ball.x <= 0:
                    print("P2 Scored!")
                    game_scoreboard.increaseScore(const.Player.P2)
                    game_ball.reset(const.Player.P2)
                    
                else:
                    print("P1 Scored!")
                    game_scoreboard.increaseScore(const.Player.P1)
                    game_ball.reset(const.Player.P1)
                
                
                paddle.resetAllPaddles(p1_paddle,p2_paddle)
                startGame = False
                      
            game_scoreboard.showScore(game_surface)
        else:
            game_scoreboard.showWinner(game_surface)
            game_scoreboard.showStart(game_surface)
            
            
            
        # Render
        
        pygame.draw.rect(game_surface,"red",p1_paddle)
        pygame.draw.rect(game_surface,"green",p2_paddle)
        pygame.draw.rect(game_surface,"white",game_ball)
        

        pygame.display.flip()

        clock.tick(120)  # limits FPS

    
    return gameState
