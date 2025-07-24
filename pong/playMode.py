import pygame
import game_constants as const
import audio
import gameText
import paddle
import ball




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

        gameState = p_gameState
        self.running = True
        self.startGame = False
        
        audio.soundTools.playMusic(const.MusicChoice.gamePlay)

        while self.running:
            
            gameState = self.__pollEvents(gameState)
                    
            ## Start the game
            if self.startGame:

                ## Wipe away last frames
                self.game_surface.fill("black")
                ## Move the ball
                self.game_ball.travel()        
                
                ## P1 paddle
                self.p1_paddle.controlPaddle_Player()            
                ## P2 paddle
                self.p2_paddle.controlPaddle_Player()      
                ## Handle P1 paddle collisions
                self.p1_paddle.handleHitBall(self.game_ball)
                ## Handle P2 paddle collisions
                self.p2_paddle.handleHitBall(self.game_ball)    
                ## Handle floor and ceiling bounce
                self.__handleWallBounce()
                ## Handle goal
                self.__handleGoal()
                ## Blit the score on the screen
                self.game_scoreboard.showScore(self.game_surface)
            else:
                self.game_scoreboard.showWinner(self.game_surface)
                self.game_scoreboard.showStart(self.game_surface)
                
            ## Render elements
            
            pygame.draw.rect(self.game_surface,"red",self.p1_paddle)
            pygame.draw.rect(self.game_surface,"green",self.p2_paddle)
            pygame.draw.rect(self.game_surface,"white",self.game_ball)

            pygame.display.flip()

            ## limit FPS
            self.clock.tick(120)  

        return gameState

    def run_singleplayer(self,p_gameState: const.GameState):
        
        gameState = p_gameState
        self.running = True
        self.startGame = False
        
        audio.soundTools.playMusic(const.MusicChoice.gamePlay)

        while self.running:
            
            gameState = self.__pollEvents(gameState)
                    
            ## Start the game
            if self.startGame:

                ## Wipe away last frames
                self.game_surface.fill("black")
                ## Move the ball
                self.game_ball.travel()        
                
                ## P1 paddle
                self.p1_paddle.controlPaddle_Player()                  
                ## Handle P1 paddle collisions
                p1HitOccured = self.p1_paddle.handleHitBall(self.game_ball)
                if p1HitOccured:
                    self.p2_paddle.calculateTarget_AI(self.game_ball)
                ## AI paddle
                self.p2_paddle.controlPaddle_AI(self.game_ball)
                ## Handle P2 paddle collisions
                self.p2_paddle.handleHitBall(self.game_ball)    
                ## Handle floor and ceiling bounce
                self.__handleWallBounce()
                ## Handle goal
                self.__handleGoal()
                ## Blit the score on the screen
                self.game_scoreboard.showScore(self.game_surface)
            else:
                self.game_scoreboard.showWinner(self.game_surface)
                self.game_scoreboard.showStart(self.game_surface)
                
            ## Render elements
            
            pygame.draw.rect(self.game_surface,"red",self.p1_paddle)
            pygame.draw.rect(self.game_surface,"green",self.p2_paddle)
            pygame.draw.rect(self.game_surface,"white",self.game_ball)

            pygame.display.flip()

            ## limit FPS
            self.clock.tick(120)  

        return gameState

    def __pollEvents(self,p_gameState: const.GameState) -> const.GameState:

        gameState = p_gameState
        ## Poll for events
        for event in pygame.event.get():
            
            ## Close the game window
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

        return gameState

    def __handleGoal(self) -> None:

        if self.game_ball.x <= 0 or self.game_ball.x >= const.GAME_SURFACE_WIDTH: 

            ## Calculate score
            if self.game_ball.x <= 0:
                #print("P2 Scored!")
                self.game_scoreboard.increaseScore(const.Player.P2)
                self.game_ball.reset(const.Player.P2)
                
            else:
                #print("P1 Scored!")
                self.game_scoreboard.increaseScore(const.Player.P1)
                self.game_ball.reset(const.Player.P1)   
            
            paddle.PaddleTools.resetAllPaddles(self.p1_paddle,self.p2_paddle)
            self.startGame = False
    
    def __handleWallBounce(self) -> None:

        if self.game_ball.y <= 0 or self.game_ball.y + self.game_ball.height >= const.GAME_SURFACE_HEIGHT: 
            audio.soundTools.playSound(const.SoundChoice.yWallHit,1000)
            self.game_ball.reverseY()



