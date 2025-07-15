
import pygame
import game_constants as const
import mainMenu as main_menu
import playMode
import optionsMenu as options_menu


def main() -> None:

    # INITIALIZE
    pygame.init()
    mainMenu = main_menu.Menu()
    gameState = const.GameState.MainMenu

    while gameState != const.GameState.Off:
 
        if gameState == const.GameState.MainMenu:
            gameState = mainMenu._run_mainMenu(gameState)
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
            gameState = optionsMenu._run_options(gameState)
            del optionsMenu

    # QUIT
    pygame.quit()


# EXECUTION

main()

