
import pygame
import game_constants as const
import mainMenu
import playMode
import optionsMenu as options


def main() -> None:

    # INITIALIZE PYGAME
    pygame.init()

    

    gameState = const.GameState.MainMenu

    while gameState != const.GameState.Off:
 
        if gameState == const.GameState.MainMenu:
            gameState = mainMenu.run_mainMenu(gameState)
        elif gameState == const.GameState.Singleplayer:
            gameState = playMode.run_singleplayer(gameState)
        elif gameState == const.GameState.Multiplayer:
            gameState = playMode.run_multiplayer(gameState)
        elif gameState == const.GameState.Options:
            optionsMenu = options.Menu()
            gameState = optionsMenu.run_options(gameState)
            del optionsMenu

    # QUIT PYGAME
    pygame.quit()



# EXECUTION

main()

