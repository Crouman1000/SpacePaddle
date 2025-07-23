
import pygame
import game_constants as const
import audio
import image
import mainMenu as main_menu
import optionsMenu as options_menu
import playMode


def main() -> None:

    # Initialize modules
    pygame.init()
    image.imageTools.loadImages()
    audio.soundTools.loadSounds()
    
    mainMenu = main_menu.Menu()
    gameState = const.GameState.MainMenu

    while gameState != const.GameState.Off:
 
        if gameState == const.GameState.MainMenu:
            gameState = mainMenu.run_mainMenu(gameState)
        elif gameState == const.GameState.Singleplayer:
            gamePlay = playMode.gamePlay()
            gameState = gamePlay.run_singleplayer(gameState)
            del gamePlay
        elif gameState == const.GameState.Multiplayer:
            gamePlay = playMode.gamePlay()
            gameState = gamePlay.run_multiplayer(gameState)
            del gamePlay
        elif gameState == const.GameState.Options:
            optionsMenu = options_menu.Menu()
            gameState = optionsMenu.run_options(gameState)
            del optionsMenu

    # QUIT
    
    image.imageTools.unloadImages()
    audio.soundTools.unloadAudio()

    pygame.quit()


# EXECUTION

main()

