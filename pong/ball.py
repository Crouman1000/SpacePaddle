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
       
    def reset(self) -> None:

        self.x = (const.GAME_SURFACE_WIDTH - const.BALL_RADIUS)/2 
        self.y = (const.GAME_SURFACE_HEIGHT - const.BALL_RADIUS)/2 
        self.speedX = const.BALL_SPEED*random.choice([-1,1])
        self.speedY = const.BALL_SPEED*random.choice([-1,1])

    def reverseX(self) -> None:
        self.speedX *= -1

    def reverseY(self) -> None:
        self.speedY *= -1

    def move(self,p_speedX: int,p_speedY: int) -> None:
        self.x = self.x + p_speedX
        self.y = self.y + p_speedY