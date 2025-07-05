import pygame
import game_constants as const
import ball
import math

class Paddle(pygame.Rect):

    def __init__(self,p_player: const.Player):

        width_ = const.PADDLE_WIDTH
        height_ = const.PADDLE_HEIGHT
        offsetX = 100 if p_player == const.Player.P1 else const.GAME_SURFACE_WIDTH - 100
        left_ = offsetX
        top_ = (const.GAME_SURFACE_HEIGHT - height_)/2 
        
        super().__init__(left_,top_,width_,height_)
       
        self.speedY = 0
        self.player = p_player
       
    def reset(self,p_player: const.Player) -> None:

        height_ = const.PADDLE_HEIGHT
        offsetX = 100 if p_player == const.Player.P1 else const.GAME_SURFACE_WIDTH - 100
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


def resetAllPaddles(*p_paddles: Paddle) -> None:
    for p in p_paddles:
        p.reset(p.player)

