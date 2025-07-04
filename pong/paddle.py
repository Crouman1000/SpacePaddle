import pygame
import game_constants as const


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


def resetAllPaddles(*p_paddles: Paddle) -> None:
    for p in p_paddles:
        p.reset(p.player)

