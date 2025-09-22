"""This module contains all the game constants used in the game."""

from enum import Enum
import os
import sys

### CONSTANTS

## PATHING


# Assist in finding paths when using PyInstaller
_MEIPASS_DIR = getattr(sys, "_MEIPASS", None)

BASE_DIR = _MEIPASS_DIR or os.path.dirname(os.path.abspath(__file__))


## SOUND
class SoundState(Enum):
    """Enum for sound states."""

    OFF = 0
    ON = 1


class SoundChoice(Enum):
    """Enum for sound choices."""

    PADDLE_HIT = os.path.join(BASE_DIR, "assets", "sounds", "paddle_hit.mp3")
    Y_WALL_HIT = os.path.join(BASE_DIR, "assets", "sounds", "yWall_hit.mp3")
    VICTORY = os.path.join(BASE_DIR, "assets", "sounds", "victory.mp3")


## MUSIC
class MusicChoice(Enum):
    """Enum for music choices."""

    GAME_MENU = os.path.join(BASE_DIR, "assets", "sounds", "gameMenu.mp3")
    GAME_PLAY = os.path.join(BASE_DIR, "assets", "sounds", "gameplay.mp3")


## IMAGE
class ImageChoice(Enum):
    """Enum for image choices."""

    BACKGROUND_MENU = os.path.join(BASE_DIR, "assets", "images", "menu_background3.png")


## GAMESTATE
class GameState(Enum):
    """Enum for game states."""

    OFF = -1
    MAIN_MENU = 0
    SINGLE_PLAYER = 1
    MULTIPLAYER = 2
    OPTIONS = 3


## GAMEWIDE
GAME_SURFACE_WIDTH = 1280
GAME_SURFACE_HEIGHT = 720


## MAIN MENU
MENU_BUTTON_HEIGHT = GAME_SURFACE_HEIGHT / 8
MENU_BUTTON_WIDTH = GAME_SURFACE_WIDTH / 3
MENU_BUTTON_SIZE = (MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
MENU_BUTTON_BORDER_RAD = 20
SINGLEPLAYER_BUTTON_COORDS = ((GAME_SURFACE_WIDTH - MENU_BUTTON_WIDTH) / 2, 100)
MULTIPLAYER_BUTTON_COORDS = (
    (GAME_SURFACE_WIDTH - MENU_BUTTON_WIDTH) / 2,
    100 + 2 * MENU_BUTTON_HEIGHT,
)

## OPTIONS MENU
OPTIONS_BUTTON_COORDS = (
    (GAME_SURFACE_WIDTH - MENU_BUTTON_WIDTH) / 2,
    100 + 4 * MENU_BUTTON_HEIGHT,
)

## COLORS


class Color(Enum):
    """Enum for colors used in the game."""

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (165, 165, 165)


## SINGLE PLAYER, MULTIPLAYER
class Player(Enum):
    """Enum for players."""

    P1 = 1
    P2 = 2


GAME_MAXSCORE = 5
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE1_OFFSET = 100
PADDLE2_OFFSET = GAME_SURFACE_WIDTH - PADDLE1_OFFSET - PADDLE_WIDTH
PADDLE_SPEED = 5.0
BALL_RADIUS = 20.0
BALL_SPEED = 6.0
BALL_MAX_SPEED = 10.0
BALL_MIN_SPEED = 0.0
BALL_INCREASE_SPEED = 0.5
