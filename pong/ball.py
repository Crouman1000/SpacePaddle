import pygame
import random
import game_constants as const

class Ball(pygame.Rect):

    
    def __init__(self):

        width_ = const.BALL_RADIUS
        height_ = const.BALL_RADIUS
        left_ = (const.GAME_SURFACE_WIDTH - width_)/2 
        top_ = (const.GAME_SURFACE_HEIGHT - height_)/2 

        
        super().__init__(left_,top_,width_,height_)
        self.speedX = const.BALL_SPEED*random.choice([-1,1])
        self.speedY = const.BALL_SPEED*random.choice([-1,1])
       
    def reset(self,p_player: const.Player) -> None:

        self.x = (const.GAME_SURFACE_WIDTH - const.BALL_RADIUS)/2 
        self.y = (const.GAME_SURFACE_HEIGHT - const.BALL_RADIUS)/2 

        self.speedX = const.BALL_SPEED if p_player == const.Player.P1 else -1*const.BALL_SPEED
        self.speedY = const.BALL_SPEED*random.choice([-1,1])

    def reverseX(self) -> None:
        self.speedX *= -1

    def reverseY(self) -> None:
        self.speedY *= -1

    def move(self) -> None:
        self.x = self.x + self.speedX
        self.y = self.y + self.speedY

    def increaseSpeed(self) -> None:

        determineSpeed = lambda speed: speed - 0.5 if speed < 0 and speed > -9 else speed + 0.5 if speed > 0 and speed < 9 else speed  
        self.speedX = determineSpeed(self.speedX)
        self.speedY = determineSpeed(self.speedY)


   