
import pygame
import game_constants as const
import mainMenu
import playMode as playMode



def main() -> None:

    # INITIALIZE PYGAME
    pygame.init()

    gameState = const.GameState.MainMenu

    while gameState != const.GameState.Off:

        if gameState == const.GameState.MainMenu:
            gameState = mainMenu.run_mainMenu()
        if gameState == const.GameState.Singleplayer:
            gameState = playMode.run_singleplayer()
        elif gameState == const.GameState.Multiplayer:
            gameState = playMode.run_multiplayer()

    # QUIT PYGAME
    pygame.quit()



# EXECUTION

main()

