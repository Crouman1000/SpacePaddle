"""This module defines the Ball class for the game, inheriting from pygame.Rect."""

import random
import pygame
import game_constants as gconst


class Ball(pygame.Rect):
    """This class represents the ball in the game, handling its position and movement."""

    def __init__(self):

        width_ = gconst.BALL_RADIUS
        height_ = gconst.BALL_RADIUS
        left_ = (gconst.GAME_SURFACE_WIDTH - width_) / 2
        top_ = (gconst.GAME_SURFACE_HEIGHT - height_) / 2

        super().__init__(left_, top_, width_, height_)
        self.speed_x = gconst.BALL_SPEED * random.choice([-1, 1])
        self.speed_y = 0
        self.x_f = float(self.x)
        self.y_f = float(self.y)

    def reset(self, p_player: gconst.Player) -> None:
        """Reset the ball's position and speed based on who scored."""
        self.x_f = (gconst.GAME_SURFACE_WIDTH - gconst.BALL_RADIUS) / 2
        self.y_f = (gconst.GAME_SURFACE_HEIGHT - gconst.BALL_RADIUS) / 2
        self.x = int(self.x_f)  # pylint: disable=attribute-defined-outside-init
        self.y = int(self.y_f)  # pylint: disable=attribute-defined-outside-init

        self.speed_x = (
            gconst.BALL_SPEED
            if p_player == gconst.Player.P1
            else -1 * gconst.BALL_SPEED
        )
        self.speed_y = 0

        # def reverseX(self) -> None:
        #    self.speedX *= -1

    def reverse_y(self) -> None:
        """Reverse the vertical speed of the ball."""
        self.speed_y *= -1

    def travel(self) -> None:
        """Update the ball's position based on its speed."""
        self.x_f = self.x_f + self.speed_x
        self.y_f = self.y_f + self.speed_y
        self.x = int(self.x_f)  # pylint: disable=attribute-defined-outside-init
        self.y = int(self.y_f)  # pylint: disable=attribute-defined-outside-init

    def increase_speed(self) -> None:
        """Increase the speed of the ball."""
        # determineSpeed = lambda speed: speed - 0.5 if speed < 0 and speed > -9
        # else speed + 0.5 if speed > 0 and speed < 9 else speed
        self.speed_x = self.__determine_speed(self.speed_x)
        self.speed_y = self.__determine_speed(self.speed_y)

    def __determine_speed(self, p_speed: float) -> float:
        """Adjust the speed of the ball according to its sign,
        ensuring it does not exceed maximum limits."""
        if p_speed < 0 and p_speed > -1 * gconst.BALL_MAX_SPEED:
            p_speed -= gconst.BALL_INCREASE_SPEED
        elif p_speed > 0 and p_speed < gconst.BALL_MAX_SPEED:
            p_speed += gconst.BALL_INCREASE_SPEED
        return p_speed
