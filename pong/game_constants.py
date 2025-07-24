from enum import Enum

### CONSTANTS


## SOUND
class SoundState(Enum):
    Off = 0
    On = 1
    
class SoundChoice(Enum):
    paddleHit = "pong/assets/sounds/paddle_hit.mp3"
    yWallHit = "pong/assets/sounds/yWall_hit.mp3"
    victory = "pong/assets/sounds/victory.mp3"

## MUSIC
class MusicChoice(Enum):
    gameMenu = "pong/assets/sounds/gameMenu.mp3"
    gamePlay = "pong/assets/sounds/gameplay.mp3"
    
## IMAGE

class imageChoice(Enum):
    backgroundMenu = "pong/assets/images/menu_background3.png"

## GAMESTATE
class GameState(Enum):
    Off = -1
    MainMenu = 0
    Singleplayer = 1
    Multiplayer = 2
    Options = 3

## GAMEWIDE

GAME_SURFACE_WIDTH = 1280
GAME_SURFACE_HEIGHT = 720


## MAIN MENU

MENU_BUTTON_HEIGHT = GAME_SURFACE_HEIGHT/8
MENU_BUTTON_WIDTH = GAME_SURFACE_WIDTH/3
MENU_BUTTON_SIZE = (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT)
MENU_BUTTON_BORDER_RAD = 20
SINGLEPLAYER_BUTTON_COORDS = ((GAME_SURFACE_WIDTH - MENU_BUTTON_WIDTH)/2 ,100)
MULTIPLAYER_BUTTON_COORDS = ((GAME_SURFACE_WIDTH - MENU_BUTTON_WIDTH)/2,100 + 2* MENU_BUTTON_HEIGHT)

## OPTIONS MENU

OPTIONS_BUTTON_COORDS = ((GAME_SURFACE_WIDTH-MENU_BUTTON_WIDTH)/2,100 + 4* MENU_BUTTON_HEIGHT)


## SINGLE PLAYER, MULTIPLAYER

GAME_MAXSCORE = 5
PADDLE_WIDTH = 20.0
PADDLE_HEIGHT = 100.0
PADDLE1_OFFSET = 100.0
PADDLE2_OFFSET = GAME_SURFACE_WIDTH - PADDLE1_OFFSET - PADDLE_WIDTH
PADDLE_SPEED = 5.0
BALL_RADIUS = 20.0
BALL_SPEED = 5.0
BALL_MAX_SPEED = 10.0
BALL_MIN_SPEED = 0.0
BALL_INCREASE_SPEED = 0.5

class Player(Enum):
    P1 = 1
    P2 = 2



    