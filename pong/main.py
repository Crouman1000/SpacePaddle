"""This is the main module which handles game states and the main game loop"""

import pygame
import game_constants as const
import audio
import graphics
import main_menu as mm
import options_menu as om
import play_mode


def main() -> None:
    """Initialize all necessary modules, loads resources, and manages the
    main game loop. It handles transitions between different game states.
    Upon exiting the main loop, it unloads resources and quits the game."""

    # Initialize modules
    pygame.init()  # pylint: disable=no-member
    graphics.ImageTools.load_images()
    audio.SoundTools.load_sounds()

    main_menu = mm.Menu()
    game_state = const.GameState.MAIN_MENU

    # Main game loop, switching between game states
    while game_state != const.GameState.OFF:

        if game_state == const.GameState.MAIN_MENU:
            game_state = main_menu.run_main_menu(game_state)
        elif game_state == const.GameState.SINGLE_PLAYER:
            game_play = play_mode.GamePlay()
            game_state = game_play.run_singleplayer(game_state)
            del game_play
        elif game_state == const.GameState.MULTIPLAYER:
            game_play = play_mode.GamePlay()
            game_state = game_play.run_multiplayer(game_state)
            del game_play
        elif game_state == const.GameState.OPTIONS:
            options_menu = om.Menu()
            game_state = options_menu.run_options(game_state)
            del options_menu

    # Unload resources and quit the game
    graphics.ImageTools.unload_images()
    audio.SoundTools.unload_audio()

    pygame.quit()  # pylint: disable=no-member


# EXECUTION

main()
