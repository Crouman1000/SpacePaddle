import math
import random as rnd
import pygame
import game_constants as const
import audio
import ball


class Paddle(pygame.Rect):

    def __init__(self,p_player: const.Player):

        width_ = const.PADDLE_WIDTH
        height_ = const.PADDLE_HEIGHT
        offsetX = const.PADDLE1_OFFSET if p_player == const.Player.P1 else const.PADDLE2_OFFSET
        left_ = offsetX
        top_ = (const.GAME_SURFACE_HEIGHT - height_)/2 

        
        super().__init__(left_,top_,width_,height_)
       
       
        self.speedY = 0
        self.player = p_player
        self.predictPosY = None

    

    def controlPaddle_Player(self) -> None:
        #@@@ optimize with a Protocol
        keys_list = pygame.key.get_pressed()

        upKey = pygame.K_w if self.player == const.Player.P1 else pygame.K_UP
        downKey = pygame.K_s if self.player == const.Player.P1 else pygame.K_DOWN

        if self.y > 0: 
            if keys_list[upKey]:
                self.__stir(-1*const.PADDLE_SPEED)
        if self.y < const.GAME_SURFACE_HEIGHT - self.height:
            if keys_list[downKey]:
                self.__stir(1*const.PADDLE_SPEED)


    def controlPaddle_AI(self, p_ball: ball.Ball) -> None:

        #@@@ Improve AI    
        ## AI V2

        ## trigger this code when player1 hits
        
        targetPosY = p_ball.centery
        ## distance chunks of speedX until collision
        if self.predictPosY:
            targetPosY = self.predictPosY


        if self.y > 0: 
            if targetPosY < self.centery:
                self.speedY = -1*const.PADDLE_SPEED
                #if varianceX < 50 and abs(varianceY) < const.PADDLE_HEIGHT/2:
                #    self.speedY *= rnd.random()
                self.__stir(self.speedY)

        if self.y < const.GAME_SURFACE_HEIGHT - self.height:
            if targetPosY > self.centery:
                self.speedY = const.PADDLE_SPEED
                #if varianceX < 50 and abs(varianceY) < const.PADDLE_HEIGHT/2:
                #    self.speedY *= rnd.random()
                self.__stir(self.speedY)

        if(p_ball.centerx < const.PADDLE2_OFFSET):
            print(f"self.predictPosY: {self.predictPosY}")
            print(f"self.centery: {self.centery}")   
            print(f"p_ball.centery: {p_ball.centery}")
        else:
            pass

    def calculateTarget_AI(self,p_ball: ball.Ball) -> None:

        ballSpeedX = p_ball.speedX
        ballSpeedY = p_ball.speedY
        ballCenterNewX = p_ball.centerx
        ballCenterNewY = p_ball.centery       
        ballWidth = p_ball.width

        #framesUntilCollision = (const.PADDLE2_OFFSET - (p_ball.x + p_ball.width))/ballSpeedX
        while ballCenterNewX < const.PADDLE2_OFFSET:
    
            ballCenterNewY = ballCenterNewY + ballSpeedY

            if ballCenterNewY - ballWidth/2 <= 0:
                #overflow = -(ballCenterNewY - ballWidth/2)
                #ballCenterNewY = ballWidth/2 + overflow
                ballSpeedY *= -1 

            elif ballCenterNewY + ballWidth/2 >= const.GAME_SURFACE_HEIGHT:
                #overflow = (ballCenterNewY + ballWidth/2) - const.GAME_SURFACE_HEIGHT
                #ballCenterNewY = const.GAME_SURFACE_HEIGHT - ballWidth/2 - overflow
                ballSpeedY *= -1 

            ballCenterNewX = ballCenterNewX + ballSpeedX
            #framesUntilCollision = framesUntilCollision - 1
        
        self.predictPosY = ballCenterNewY
    

    def handleHitBall(self, p_ball: ball.Ball) -> bool:

        hit_occured = False
        if self.colliderect(p_ball):
            audio.soundTools.playSound(const.SoundChoice.paddleHit)
            p_ball.increaseSpeed()
            self.__reflectBall(p_ball)
            
            
            if self.player == const.Player.P1:
                hit_occured = True
            if self.player == const.Player.P2:
                self.predictPosY = None

        return hit_occured

    def _reset(self,p_player: const.Player) -> None:

        height_ = const.PADDLE_HEIGHT
        offsetX = const.PADDLE1_OFFSET if p_player == const.Player.P1 else const.PADDLE2_OFFSET
        self.left = offsetX
        self.top = (const.GAME_SURFACE_HEIGHT - height_)/2 
        self.speedY = 0
        self.predictPosY = None

    def __stir(self,p_speedY: float) -> None:
        self.y = self.y + p_speedY

    def __reflectBall(self,p_ball: ball.Ball) -> None:
        
        if self.player == const.Player.P2:

            reflectAngle = 225 - 90*((p_ball.y - self.topleft[1])/const.PADDLE_HEIGHT)
            p_ball.speedX,p_ball.speedY = self.__calculateNewDirectionBall(p_ball.speedX,p_ball.speedY,reflectAngle)

        elif self.player == const.Player.P1:
           
            reflectAngle = 315 + 90*((p_ball.y - self.topright[1])/const.PADDLE_HEIGHT)
            p_ball.speedX,p_ball.speedY = self.__calculateNewDirectionBall(p_ball.speedX,p_ball.speedY,reflectAngle)

    def __calculateNewDirectionBall(self,p_speedX,p_speedY,p_angle) -> tuple:

        hypot = math.hypot(p_speedX,p_speedY)
        speedX = math.cos(math.radians(p_angle))*hypot
        speedY = math.sin(math.radians(p_angle))*hypot
        return speedX,speedY

class PaddleTools():
    @staticmethod
    def resetAllPaddles(*p_paddles: Paddle) -> None:
        for p in p_paddles:
            p._reset(p.player)

