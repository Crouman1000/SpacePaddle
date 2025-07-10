
import pygame
import paddle
import ball
import game_constants as const
import random as rnd


def calculatePaddlePosition(p_p2_paddle: paddle.Paddle, p_ball: ball.Ball):
            
    
    ### AI V1

    varianceY = p_p2_paddle.centery - p_ball.centery
    varianceX = p_p2_paddle.centerx - p_ball.centerx

    if p_p2_paddle.y > 0: 
        if p_ball.centery < p_p2_paddle.centery:
            speedY = -1*const.PADDLE_SPEED
            if varianceX < 100 and abs(varianceY) < const.PADDLE_HEIGHT/2:
                speedY *= rnd.random()
            p_p2_paddle.move(speedY)


    if p_p2_paddle.y < const.GAME_SURFACE_HEIGHT - p_p2_paddle.height:
        if p_ball.centery > p_p2_paddle.centery:
            speedY = const.PADDLE_SPEED
            if varianceX < 100 and abs(varianceY) < const.PADDLE_HEIGHT/2:
               speedY *= rnd.random()
            p_p2_paddle.move(speedY)


#if varianceY > 0 and varianceY < (p_p2_paddle.centery + const.PADDLE_HEIGHT/2):
#    speedY = -1*rnd.random()
#    p_p2_paddle.move(speedY*const.PADDLE_SPEED)