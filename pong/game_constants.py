from enum import Enum

# CONSTANTS

GAME_SURFACE_WIDTH = 1280
GAME_SURFACE_HEIGHT = 720
GAME_MAXSCORE = 5
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 150
PADDLE1_OFFSET = 100
PADDLE2_OFFSET = GAME_SURFACE_WIDTH - 100
PADDLE_SPEED = 5
BALL_RADIUS = 20
BALL_SPEED = 5



class Player(Enum):
    P1 = 1
    P2 = 2

class GameState(Enum):
    MainMenu = 0
    Singleplayer = 1
    Multiplayer = 2
    Options = 3
    