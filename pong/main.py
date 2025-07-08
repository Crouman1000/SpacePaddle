
import pygame
import game_constants as const
import mainMenu
import multiplayer



def main():

    # INITIALIZE PYGAME
    pygame.init()

    gameState = const.GameState.MainMenu

    while gameState != const.GameState.Off:

        
        if gameState == const.GameState.MainMenu:
            gameState = mainMenu.run_mainMenu()
        elif gameState == const.GameState.Multiplayer:
            gameState = multiplayer.run_multiplayer()

    # QUIT PYGAME
    pygame.quit()





main()

