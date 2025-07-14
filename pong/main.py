
import pygame
import game_constants as const
import mainMenu as main_menu
import playMode
import optionsMenu as options_menu


def main() -> None:

    # INITIALIZE PYGAME
    pygame.init()

    mainMenu = main_menu.Menu()

    gameState = const.GameState.MainMenu
    while gameState != const.GameState.Off:
 
        if gameState == const.GameState.MainMenu:
            gameState = mainMenu.run_mainMenu(gameState)
        elif gameState == const.GameState.Singleplayer:
            gameState = playMode.run_singleplayer(gameState)
        elif gameState == const.GameState.Multiplayer:
            gameState = playMode.run_multiplayer(gameState)
        elif gameState == const.GameState.Options:
            optionsMenu = options_menu.Menu()
            gameState = optionsMenu.run_options(gameState)
            del optionsMenu

    # QUIT PYGAME
    pygame.quit()



# EXECUTION

main()

