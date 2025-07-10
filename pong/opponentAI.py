
import pygame
import paddle
import ball
import game_constants as const



def calculatePaddlePosition(p_p2_paddle: paddle.Paddle, p_ball: ball.Ball):
            
    ### AI V1
    if p_p2_paddle.y > 0: 
        if p_ball.centery < p_p2_paddle.centery:
            p_p2_paddle.move(-1*const.PADDLE_SPEED)
    if p_p2_paddle.y < const.GAME_SURFACE_HEIGHT - p_p2_paddle.height:
        if p_ball.centery > p_p2_paddle.centery:
            p_p2_paddle.move(const.PADDLE_SPEED)