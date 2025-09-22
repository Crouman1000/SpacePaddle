"""This module defines the Menu class, which manages the main menu of the game."""

import pygame
import game_constants as gconst
import graphics
import audio


class Menu:
    """This class handles the main menu of the game, including rendering buttons."""

    def __init__(self):

        self.running = True
        self.clock = pygame.time.Clock()
        self.button_text_font = pygame.font.SysFont("Bank Gothic", 50, False, False)
        self.menu_surface = pygame.display.set_mode(
            (gconst.GAME_SURFACE_WIDTH, gconst.GAME_SURFACE_HEIGHT)
        )
        self.background_surface = pygame.transform.scale(
            graphics.ImageTools.images[gconst.ImageChoice.BACKGROUND_MENU],
            (gconst.GAME_SURFACE_WIDTH, gconst.GAME_SURFACE_HEIGHT),
        )

        self.single_player_rect = pygame.Rect(
            gconst.SINGLEPLAYER_BUTTON_COORDS[0],
            gconst.SINGLEPLAYER_BUTTON_COORDS[1],
            gconst.MENU_BUTTON_SIZE[0],
            gconst.MENU_BUTTON_SIZE[1],
        )
        self.single_player_text_surface = self.button_text_font.render(
            "SINGLE PLAYER", False, gconst.Color.BLACK.value
        )

        self.multi_player_rect = pygame.Rect(
            gconst.MULTIPLAYER_BUTTON_COORDS[0],
            gconst.MULTIPLAYER_BUTTON_COORDS[1],
            gconst.MENU_BUTTON_SIZE[0],
            gconst.MENU_BUTTON_SIZE[1],
        )
        self.multi_player_text_surface = self.button_text_font.render(
            "MULTIPLAYER", False, gconst.Color.BLACK.value
        )

        self.options_rect = pygame.Rect(
            gconst.OPTIONS_BUTTON_COORDS[0],
            gconst.OPTIONS_BUTTON_COORDS[1],
            gconst.MENU_BUTTON_SIZE[0],
            gconst.MENU_BUTTON_SIZE[1],
        )
        self.option_text_surface = self.button_text_font.render(
            "OPTIONS", False, gconst.Color.BLACK.value
        )

    def run_main_menu(self, p_game_state: gconst.GameState) -> gconst.GameState:
        """Run the main menu loop, handling button clicks and transitions to other states."""
        game_state = p_game_state
        self.running = True
        ## Load the background image and play menu music
        audio.SoundTools.play_music(gconst.MusicChoice.GAME_MENU)
        ## Render the background
        self.menu_surface.blit(self.background_surface, (0, 0))
        ## Draw the buttons
        pygame.draw.rect(
            self.menu_surface,
            gconst.Color.LIGHT_GRAY.value,
            self.single_player_rect,
            border_radius=gconst.MENU_BUTTON_BORDER_RAD,
        )
        self.menu_surface.blit(
            self.single_player_text_surface,
            (
                self.single_player_rect.centerx
                - self.single_player_text_surface.get_width() / 2,
                self.single_player_rect.centery
                - self.single_player_text_surface.get_height() / 2,
            ),
        )

        pygame.draw.rect(
            self.menu_surface,
            gconst.Color.LIGHT_GRAY.value,
            self.multi_player_rect,
            border_radius=gconst.MENU_BUTTON_BORDER_RAD,
        )
        self.menu_surface.blit(
            self.multi_player_text_surface,
            (
                self.multi_player_rect.centerx
                - self.multi_player_text_surface.get_width() / 2,
                self.multi_player_rect.centery
                - self.multi_player_text_surface.get_height() / 2,
            ),
        )

        pygame.draw.rect(
            self.menu_surface,
            gconst.Color.LIGHT_GRAY.value,
            self.options_rect,
            border_radius=gconst.MENU_BUTTON_BORDER_RAD,
        )
        self.menu_surface.blit(
            self.option_text_surface,
            (
                self.options_rect.centerx - self.option_text_surface.get_width() / 2,
                self.options_rect.centery - self.option_text_surface.get_height() / 2,
            ),
        )
        ## Main loop of the menu
        while self.running:
            ## Poll for events
            for event in pygame.event.get():
                # print(f"event: {event}")
                if event.type == pygame.QUIT:  # pylint: disable=no-member
                    self.running = False
                    game_state = gconst.GameState.OFF
                if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
                    mouse_clicked_coords_tuple = pygame.mouse.get_pos()
                    ## Check which button was clicked
                    if self.single_player_rect.collidepoint(
                        mouse_clicked_coords_tuple[0], mouse_clicked_coords_tuple[1]
                    ):
                        self.running = False
                        game_state = gconst.GameState.SINGLE_PLAYER

                    elif self.multi_player_rect.collidepoint(
                        mouse_clicked_coords_tuple[0], mouse_clicked_coords_tuple[1]
                    ):
                        self.running = False
                        game_state = gconst.GameState.MULTIPLAYER

                    elif self.options_rect.collidepoint(
                        mouse_clicked_coords_tuple[0], mouse_clicked_coords_tuple[1]
                    ):
                        self.running = False
                        game_state = gconst.GameState.OPTIONS


                if event.type == pygame.MOUSEMOTION:  # pylint: disable=no-member

                    mouse_over_coords_tuple = pygame.mouse.get_pos()
                    singleplayer_button_color = gconst.Color.LIGHT_GRAY.value
                    multiplayer_button_color = gconst.Color.LIGHT_GRAY.value
                    option_button_color = gconst.Color.LIGHT_GRAY.value
                    if self.single_player_rect.collidepoint(
                        mouse_over_coords_tuple[0],mouse_over_coords_tuple[1]
                    ):
                        singleplayer_button_color = gconst.Color.YELLOW.value

                    elif self.multi_player_rect.collidepoint(
                        mouse_over_coords_tuple[0],mouse_over_coords_tuple[1]
                    ):
                        multiplayer_button_color = gconst.Color.YELLOW.value
                       
                    elif self.options_rect.collidepoint(
                        mouse_over_coords_tuple[0],mouse_over_coords_tuple[1]
                    ):
                        option_button_color = gconst.Color.YELLOW.value

                    ## Redraw the singleplayer button
                    pygame.draw.rect(
                        self.menu_surface,
                        singleplayer_button_color,
                        self.single_player_rect,
                        border_radius=gconst.MENU_BUTTON_BORDER_RAD,
                    )
                    self.menu_surface.blit(
                        self.single_player_text_surface,
                        (
                            self.single_player_rect.centerx
                            - self.single_player_text_surface.get_width() / 2,
                            self.single_player_rect.centery
                            - self.single_player_text_surface.get_height() / 2,
                        ),
                    )
                    ## Redraw the multiplayer button
                    pygame.draw.rect(
                        self.menu_surface,
                        multiplayer_button_color,
                        self.multi_player_rect,
                        border_radius=gconst.MENU_BUTTON_BORDER_RAD,
                    )
                    self.menu_surface.blit(
                        self.multi_player_text_surface,
                        (
                            self.multi_player_rect.centerx
                            - self.multi_player_text_surface.get_width() / 2,
                            self.multi_player_rect.centery
                            - self.multi_player_text_surface.get_height() / 2,
                        ),
                    )

                    ## Redraw the options button
                    pygame.draw.rect(
                        self.menu_surface,
                        option_button_color,
                        self.options_rect,
                        border_radius=gconst.MENU_BUTTON_BORDER_RAD,
                    )
                    self.menu_surface.blit(
                        self.option_text_surface,
                        (
                            self.options_rect.centerx
                            - self.option_text_surface.get_width() / 2,
                            self.options_rect.centery
                            - self.option_text_surface.get_height() / 2,
                        ),
                    )

            ## Update the display on the screen
            pygame.display.flip()

            ## limit FPS
            self.clock.tick(120)

        return game_state
