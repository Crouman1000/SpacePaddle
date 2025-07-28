"""This module contains the Paddle class and its movement, rebound and AI methods for the game."""

import math
import random as rnd
import pygame
import game_constants as const
import audio
import ball


class Paddle(pygame.Rect):
    """This class represents a paddle in the game, handling its position,
    movement, and interactions with the ball."""

    def __init__(self, p_player: const.Player):

        width_ = const.PADDLE_WIDTH
        height_ = const.PADDLE_HEIGHT
        offset_x = (
            const.PADDLE1_OFFSET
            if p_player == const.Player.P1
            else const.PADDLE2_OFFSET
        )
        left_ = offset_x
        top_ = (const.GAME_SURFACE_HEIGHT - height_) / 2

        super().__init__(left_, top_, width_, height_)

        self.speed_y = 0
        self.player = p_player
        self.predict_pos_y = None

    def control_paddle_player(self) -> None:
        """Control the paddle movement based on player input."""
        # @@@ optimize with a Protocol
        keys_list = pygame.key.get_pressed()
        y = self.y  ## pylint: disable=no-member
        up_key = (
            pygame.K_w  ## pylint: disable=no-member
            if self.player == const.Player.P1
            else pygame.K_UP  ## pylint: disable=no-member
        )
        down_key = (
            pygame.K_s  ## pylint: disable=no-member
            if self.player == const.Player.P1
            else pygame.K_DOWN  ## pylint: disable=no-member
        )

        if y > 0:
            if keys_list[up_key]:
                self.__stir(-1 * const.PADDLE_SPEED)
        if y < const.GAME_SURFACE_HEIGHT - self.height:
            if keys_list[down_key]:
                self.__stir(1 * const.PADDLE_SPEED)

    def control_paddle_ai(self, p_ball: ball.Ball) -> None:
        """Control the paddle movement for AI, predicting the ball's position."""
        ## AI V3

        target_pos_y = p_ball.centery
        ## If the AI has a predicted position, use it
        if self.predict_pos_y:
            target_pos_y = self.predict_pos_y

        # variance_x = self.centerx - p_ball.centerx
        # variance_y = self.centery - p_ball.centery

        ## If the paddle is too far from the target position,
        ## move towards it without going out of bounds
        y = self.y  ## pylint: disable=no-member
        if y > 0:
            if target_pos_y < self.centery:
                self.speed_y = -1 * const.PADDLE_SPEED
                # if variance_x < 50 and abs(variance_y) < const.PADDLE_HEIGHT / 2:
                #    self.speed_y *= rnd.random()
                self.__stir(self.speed_y)

        if y < const.GAME_SURFACE_HEIGHT - self.height:
            if target_pos_y > self.centery:
                self.speed_y = const.PADDLE_SPEED
                # if variance_x < 50 and abs(variance_y) < const.PADDLE_HEIGHT / 2:
                #    self.speed_y *= rnd.random()
                self.__stir(self.speed_y)

        ##DEBUG
        # if(p_ball.centerx < const.PADDLE2_OFFSET):
        # print(f"self.predictPosY: {self.predictPosY}")
        # print(f"self.centery: {self.centery}")
        # print(f"p_ball.centery: {p_ball.centery}")
        # else:
        #    pass

    def calculate_target_ai(self, p_ball: ball.Ball) -> None:
        """Calculate the target position for the AI paddle based on the ball's trajectory."""
        ball_speed_x = p_ball.speed_x
        ball_speed_y = p_ball.speed_y
        # ballCenterNewX = float(p_ball.centerx)
        ball_center_new_y = float(p_ball.centery)
        ball_width = float(p_ball.width)
        ## Calculate the frames until the ball reaches the paddle
        frames_until_collision = (
            const.PADDLE2_OFFSET - (p_ball.x_f + p_ball.width)
        ) / ball_speed_x
        # while ballCenterNewX < const.PADDLE2_OFFSET:
        ## Calculate the new Y position of the ball after the frames until collision
        while frames_until_collision > 0:
            ball_center_new_y = ball_center_new_y + ball_speed_y

            if ball_center_new_y - ball_width / 2 <= 0:
                ball_speed_y *= -1

            elif ball_center_new_y + ball_width / 2 >= const.GAME_SURFACE_HEIGHT:
                ball_speed_y *= -1

            # ballCenterNewX = ballCenterNewX + ballSpeedX
            frames_until_collision = frames_until_collision - 1

        ## Calculate the AI feint
        feint_y = (rnd.random() * const.PADDLE_HEIGHT) - const.PADDLE_HEIGHT / 2
        if feint_y <= 0 and feint_y >= const.GAME_SURFACE_HEIGHT:
            feint_y = 0

        self.predict_pos_y = ball_center_new_y + feint_y

    def handle_hit_ball(self, p_ball: ball.Ball) -> bool:
        """Handle the interaction when the paddle hits the ball."""
        hit_occured = False
        ## Check if the paddle collides with the ball
        if self.colliderect(p_ball):
            audio.SoundTools.play_sound(const.SoundChoice.PADDLE_HIT)
            p_ball.increase_speed()
            self.__reflect_ball(p_ball)

            if self.player == const.Player.P1:
                hit_occured = True
            if self.player == const.Player.P2:
                self.predict_pos_y = None

        return hit_occured

    def reset(self, p_player: const.Player) -> None:
        """Reset the paddle's position and speed."""
        height_ = const.PADDLE_HEIGHT
        offset_x = (
            const.PADDLE1_OFFSET
            if p_player == const.Player.P1
            else const.PADDLE2_OFFSET
        )
        self.left = offset_x  ## pylint: disable=attribute-defined-outside-init
        self.top = (  ## pylint: disable=attribute-defined-outside-init
            const.GAME_SURFACE_HEIGHT - height_
        ) / 2
        self.speed_y = 0
        self.predict_pos_y = None

    def __stir(self, p_speed_y: float) -> None:
        """Move the paddle vertically by a given speed."""
        self.y += p_speed_y  ## pylint: disable=no-member

    def __reflect_ball(self, p_ball: ball.Ball) -> None:
        """Reflect the ball's in a vector based on the paddle's position."""
        if self.player == const.Player.P2:

            reflect_angle = 225 - 90 * (
                (p_ball.y - self.topleft[1]) / const.PADDLE_HEIGHT
            )
            p_ball.speed_x, p_ball.speed_y = self.__calculate_new_direction_ball(
                p_ball.speed_x, p_ball.speed_y, reflect_angle
            )

        elif self.player == const.Player.P1:

            reflect_angle = 315 + 90 * (
                (p_ball.y - self.topright[1]) / const.PADDLE_HEIGHT
            )
            p_ball.speed_x, p_ball.speed_y = self.__calculate_new_direction_ball(
                p_ball.speed_x, p_ball.speed_y, reflect_angle
            )

    def __calculate_new_direction_ball(self, p_speed_x, p_speed_y, p_angle) -> tuple:
        """Calculate the new vector of the ball after it hits the paddle."""
        hypot = math.hypot(p_speed_x, p_speed_y)
        speed_x = math.cos(math.radians(p_angle)) * hypot
        speed_y = math.sin(math.radians(p_angle)) * hypot
        return speed_x, speed_y


class PaddleTools:
    """Utility class for Paddle operations."""

    @staticmethod
    def reset_all_paddles(*p_paddles: Paddle) -> None:
        """Reset all paddles to their initial positions."""
        for p in p_paddles:
            p.reset(p.player)
