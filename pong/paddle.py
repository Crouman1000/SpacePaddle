import pygame
import game_constants as const
import ball
import math
import random as rnd
import sound

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
       
    def reset(self,p_player: const.Player) -> None:

        height_ = const.PADDLE_HEIGHT
        offsetX = const.PADDLE1_OFFSET if p_player == const.Player.P1 else const.PADDLE2_OFFSET
        self.left = offsetX
        self.top = (const.GAME_SURFACE_HEIGHT - height_)/2 
        self.speedY = 0

    def move(self,p_speedY: int) -> None:
        self.y = self.y + p_speedY

    def reflectBall(self,p_ball: ball.Ball) -> None:
        
        if self.player == const.Player.P2:

            reflectAngle = 225 - 90*((p_ball.y - self.topleft[1])/const.PADDLE_HEIGHT)
            p_ball.speedX,p_ball.speedY = self.calculateNewVector(p_ball.speedX,p_ball.speedY,reflectAngle)

        elif self.player == const.Player.P1:
           
            reflectAngle = 315 + 90*((p_ball.y - self.topright[1])/const.PADDLE_HEIGHT)
            p_ball.speedX,p_ball.speedY = self.calculateNewVector(p_ball.speedX,p_ball.speedY,reflectAngle)

    def calculateNewVector(self,p_speedX,p_speedY,p_angle) -> tuple:

        hypot = math.hypot(p_speedX,p_speedY)
        speedX = math.cos(math.radians(p_angle))*hypot
        speedY = math.sin(math.radians(p_angle))*hypot
        return speedX,speedY
    

    def controlPaddle_Player(self) -> None:
        #@@@ optimize with a Protocol
        keys_list = pygame.key.get_pressed()

        upKey = pygame.K_w if self.player == const.Player.P1 else pygame.K_UP
        downKey = pygame.K_s if self.player == const.Player.P1 else pygame.K_DOWN

        if self.y > 0: 
            if keys_list[upKey]:
                self.move(-1*const.PADDLE_SPEED)
        if self.y < const.GAME_SURFACE_HEIGHT - self.height:
            if keys_list[downKey]:
                self.move(1*const.PADDLE_SPEED)


    def controlPaddle_AI(self, p_ball: ball.Ball) -> None:
        #@@@ Improve AI    
        ## AI V1
        varianceY = self.centery - p_ball.centery
        varianceX = self.centerx - p_ball.centerx

        if self.y > 0: 
            if p_ball.centery < self.centery:
                self.speedY = -1*const.PADDLE_SPEED
                if varianceX < 50 and abs(varianceY) < const.PADDLE_HEIGHT/2:
                    self.speedY *= rnd.random()
                self.move(self.speedY)

        if self.y < const.GAME_SURFACE_HEIGHT - self.height:
            if p_ball.centery > self.centery:
                self.speedY = const.PADDLE_SPEED
                if varianceX < 50 and abs(varianceY) < const.PADDLE_HEIGHT/2:
                    self.speedY *= rnd.random()
                self.move(self.speedY)

    def handleHitBounce(self, p_ball: ball.Ball) -> None:

        if self.colliderect(p_ball):
            sound.paddleHit_sound.play()
            self.reflectBall(p_ball)
            p_ball.increaseSpeed()


def resetAllPaddles(*p_paddles: Paddle) -> None:
    for p in p_paddles:
        p.reset(p.player)

