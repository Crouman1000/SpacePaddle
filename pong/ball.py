import pygame
import random
import game_constants as const

class Ball():

    def __init__(self):
        self.x = const.GAME_SURFACE_WIDTH/2
        self.y = const.GAME_SURFACE_HEIGHT/2   
        self.speedX = const.BALL_SPEED*random.choice([-1,1])
        self.speedY = const.BALL_SPEED*random.choice([-1,1])
        self.ball_rect = pygame.Rect(self.x,self.y,const.BALL_RADIUS,const.BALL_RADIUS)

    def reset(self):
        self.x = const.GAME_SURFACE_WIDTH/2
        self.y = const.GAME_SURFACE_HEIGHT/2   
        self.speedX = const.BALL_SPEED*random.choice([-1,1])
        self.speedY = const.BALL_SPEED*random.choice([-1,1])
        self.ball_rect.x = self.x
        self.ball_rect.y = self.y

    def reverseX(self):
        self.speedX *= -1

    def reverseY(self):
        self.speedY *= -1

    def move(self,speedX,speedY):
        self.x = self.x + speedX
        self.y = self.y + speedY
        self.ball_rect.x = self.x
        self.ball_rect.y = self.y