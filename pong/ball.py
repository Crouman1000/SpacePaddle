import random
import pygame
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
        self.x_f = float(self.x)
        self.y_f = float(self.y)
       
    def reset(self,p_player: const.Player) -> None:

        
        self.x_f = (const.GAME_SURFACE_WIDTH - const.BALL_RADIUS)/2 
        self.y_f = (const.GAME_SURFACE_HEIGHT - const.BALL_RADIUS)/2 
        self.x = int(self.x_f)
        self.y = int(self.y_f)

        self.speedX = const.BALL_SPEED if p_player == const.Player.P1 else -1*const.BALL_SPEED
        self.speedY = const.BALL_SPEED*random.choice([-1,1])

    #def reverseX(self) -> None:
    #    self.speedX *= -1

    def reverseY(self) -> None:
        self.speedY *= -1

    def travel(self) -> None:

        self.x_f = self.x_f + self.speedX
        self.y_f = self.y_f + self.speedY
        self.x = int(self.x_f)
        self.y = int(self.y_f)

    def increaseSpeed(self) -> None:

        #determineSpeed = lambda speed: speed - 0.5 if speed < 0 and speed > -9 else speed + 0.5 if speed > 0 and speed < 9 else speed  
        self.speedX = self.__determineSpeed(self.speedX)
        self.speedY = self.__determineSpeed(self.speedY)

    def __determineSpeed(self,p_speed: float) -> float:
        if p_speed < 0 and p_speed > -1*const.BALL_MAX_SPEED:
            p_speed -= const.BALL_INCREASE_SPEED 
        elif p_speed > 0 and p_speed < const.BALL_MAX_SPEED:
            p_speed += const.BALL_INCREASE_SPEED 
        return p_speed
    

   