
import pygame
import game_constants as const
import mainMenu
import playMode as playMode
import options



def main() -> None:

    # INITIALIZE PYGAME
    pygame.init()

    gameState = const.GameState.MainMenu

    while gameState != const.GameState.Off:

        if gameState == const.GameState.MainMenu:
            gameState = mainMenu.run_mainMenu()
        elif gameState == const.GameState.Singleplayer:
            gameState = playMode.run_singleplayer()
        elif gameState == const.GameState.Multiplayer:
            gameState = playMode.run_multiplayer()
        elif gameState == const.GameState.Options:
            gameState = options.run_options()

    # QUIT PYGAME
    pygame.quit()



# EXECUTION

main()

