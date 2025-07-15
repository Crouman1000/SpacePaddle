import pygame
import game_constants as const
import ball
import paddle
import gameText
import sound

class gamePlay():

    def __init__(self):

        self.running = True
        self.startGame = False
        self.clock = pygame.time.Clock()
        self.game_surface = pygame.display.set_mode((const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT))
        self.p1_paddle = paddle.Paddle(const.Player.P1)
        self.p2_paddle = paddle.Paddle(const.Player.P2)
        self.game_ball = ball.Ball()
        self.game_scoreboard = gameText.ScoreBoard("Arial",30,True,False)

    def run_multiplayer(self,p_gameState: const.GameState):
        
        ### GAME VARIABLES

        gameState = p_gameState
        self.running = True
        self.startGame = False
        
        sound.playMusic(const.MusicChoice.gamePlay)

        while self.running:
            # Poll for events
            for event in pygame.event.get():
                
                ### Close the game window
                if event.type == pygame.QUIT:
                    self.startGame = False
                    self.running = False            
                    gameState = const.GameState.Off

                elif event.type == pygame.KEYDOWN:
                    #print(f"{event.key}=?={pygame.K_ESCAPE}")
                    #if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    ### Return to game menu
                    if event.key == pygame.K_ESCAPE:
                        self.startGame = False
                        self.running = False                     
                        gameState = const.GameState.MainMenu        
                    else:
                        ### Start game
                        self.startGame = True
                    
            ### Start the game
            if self.startGame:

                ### Wipe away last frames
                self.game_surface.fill("black")

                ### Move the ball
                self.game_ball.move()

                ### Calculate paddle's positions

                
                #keys_list = tuple(keys_list_scancodewrapper)
                
                ## P1 Paddle
                self.p1_paddle.controlPaddle_Player()            
                ## P2 Paddle
                self.p2_paddle.controlPaddle_Player()
                
                ### Handle collisions
                
                if self.p1_paddle.colliderect(self.game_ball):
                    sound.paddleHit_sound.play()
                    self.p1_paddle.reflectBall(self.game_ball)
                    self.game_ball.increaseSpeed()
        
                elif self.p2_paddle.colliderect(self.game_ball):
                    sound.paddleHit_sound.play()
                    self.p2_paddle.reflectBall(self.game_ball)
                    self.game_ball.increaseSpeed()


                ### Calculate ball position
                
                if self.game_ball.y <= 0 or self.game_ball.y >= const.GAME_SURFACE_HEIGHT: 
                    sound.YwallHit_sound.play(0,1000)
                    self.game_ball.reverseY()
                if self.game_ball.x <= 0 or self.game_ball.x >= const.GAME_SURFACE_WIDTH: 

                    ### Calculate score
                    if self.game_ball.x <= 0:
                        print("P2 Scored!")
                        self.game_scoreboard.increaseScore(const.Player.P2)
                        self.game_ball.reset(const.Player.P2)
                        
                    else:
                        print("P1 Scored!")
                        self.game_scoreboard.increaseScore(const.Player.P1)
                        self.game_ball.reset(const.Player.P1)
                    
                    
                    paddle.resetAllPaddles(self.p1_paddle,self.p2_paddle)
                    self.startGame = False
                        
                self.game_scoreboard.showScore(self.game_surface)
            else:
                self.game_scoreboard.showWinner(self.game_surface)
                self.game_scoreboard.showStart(self.game_surface)
                
                
            ### Render elements
            
            pygame.draw.rect(self.game_surface,"red",self.p1_paddle)
            pygame.draw.rect(self.game_surface,"green",self.p2_paddle)
            pygame.draw.rect(self.game_surface,"white",self.game_ball)

            pygame.display.flip()

            ### limit FPS
            self.clock.tick(120)  

        return gameState


    def run_singleplayer(self,p_gameState: const.GameState):
        
        ### GAME VARIABLES

        gameState = p_gameState
        self.running = True
        self.startGame = False
        
        sound.playMusic(const.MusicChoice.gamePlay)

        while self.running:
            # Poll for events
            for event in pygame.event.get():
                
                ### Close the game window
                if event.type == pygame.QUIT:
                    self.startGame = False
                    self.running = False            
                    gameState = const.GameState.Off

                elif event.type == pygame.KEYDOWN:
                    #print(f"{event.key}=?={pygame.K_ESCAPE}")
                    #if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    ### Return to game menu
                    if event.key == pygame.K_ESCAPE:
                        self.startGame = False
                        self.running = False                     
                        gameState = const.GameState.MainMenu        
                    else:
                        ### Start game
                        self.startGame = True
                    
            ### Start the game
            if self.startGame:

                ### Wipe away last frames
                self.game_surface.fill("black")

                ### Move the ball
                self.game_ball.move()

                ### Calculate paddle's positions

                keys_list = pygame.key.get_pressed()
                ## P1 Paddle
                
                if self.p1_paddle.y > 0: 
                    if keys_list[pygame.K_w]:
                        self.p1_paddle.move(-1*const.PADDLE_SPEED)
                if self.p1_paddle.y < const.GAME_SURFACE_HEIGHT - self.p1_paddle.height:
                    if keys_list[pygame.K_s]:
                        self.p1_paddle.move(1*const.PADDLE_SPEED)
                
                ## AI Paddle

                self.p2_paddle.controlPaddle_AI(self.game_ball)
                
                ### Handle collisions
                
                if self.p1_paddle.colliderect(self.game_ball):
                    sound.paddleHit_sound.play()
                    self.p1_paddle.reflectBall(self.game_ball)
                    self.game_ball.increaseSpeed()
        
                elif self.p2_paddle.colliderect(self.game_ball):
                    sound.paddleHit_sound.play()
                    self.p2_paddle.reflectBall(self.game_ball)
                    self.game_ball.increaseSpeed()


                ### Calculate ball position
                
                if self.game_ball.y <= 0 or self.game_ball.y >= const.GAME_SURFACE_HEIGHT: 
                    sound.YwallHit_sound.play(0,1000)
                    self.game_ball.reverseY()
                if self.game_ball.x <= 0 or self.game_ball.x >= const.GAME_SURFACE_WIDTH: 

                    ### Calculate score
                    if self.game_ball.x <= 0:
                        print("P2 Scored!")
                        self.game_scoreboard.increaseScore(const.Player.P2)
                        self.game_ball.reset(const.Player.P2)
                        
                    else:
                        print("P1 Scored!")
                        self.game_scoreboard.increaseScore(const.Player.P1)
                        self.game_ball.reset(const.Player.P1)
                    
                    
                    paddle.resetAllPaddles(self.p1_paddle,self.p2_paddle)
                    self.startGame = False
                        
                self.game_scoreboard.showScore(self.game_surface)
            else:
                self.game_scoreboard.showWinner(self.game_surface)
                self.game_scoreboard.showStart(self.game_surface)
                
                
            ### Render elements
            
            pygame.draw.rect(self.game_surface,"red",self.p1_paddle)
            pygame.draw.rect(self.game_surface,"green",self.p2_paddle)
            pygame.draw.rect(self.game_surface,"white",self.game_ball)

            pygame.display.flip()

            ### limit FPS
            self.clock.tick(120)  

        return gameState
    
    



