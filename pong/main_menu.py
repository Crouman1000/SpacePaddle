"""This module defines the Menu class, which manages the main menu of the game."""

import pygame
import game_constants as const
import graphics
import audio


class Menu:
    """This class handles the main menu of the game, including rendering buttons."""

    def __init__(self):

        self.running = True
        self.clock = pygame.time.Clock()
        self.button_text_font = pygame.font.SysFont("Bank Gothic", 50, False, False)
        self.menu_surface = pygame.display.set_mode(
            (const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT)
        )
        self.background_surface = pygame.transform.scale(
            graphics.ImageTools.images.get(const.ImageChoice.BACKGROUND_MENU),
            (const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT),
        )

        self.single_player_rect = pygame.Rect(
            const.SINGLEPLAYER_BUTTON_COORDS[0],
            const.SINGLEPLAYER_BUTTON_COORDS[1],
            const.MENU_BUTTON_SIZE[0],
            const.MENU_BUTTON_SIZE[1],
        )
        self.single_player_text_surface = self.button_text_font.render(
            "SINGLE PLAYER", False, (0, 0, 0)
        )

        self.multi_player_rect = pygame.Rect(
            const.MULTIPLAYER_BUTTON_COORDS[0],
            const.MULTIPLAYER_BUTTON_COORDS[1],
            const.MENU_BUTTON_SIZE[0],
            const.MENU_BUTTON_SIZE[1],
        )
        self.multi_player_text_surface = self.button_text_font.render(
            "MULTIPLAYER", False, (0, 0, 0)
        )

        self.options_rect = pygame.Rect(
            const.OPTIONS_BUTTON_COORDS[0],
            const.OPTIONS_BUTTON_COORDS[1],
            const.MENU_BUTTON_SIZE[0],
            const.MENU_BUTTON_SIZE[1],
        )
        self.option_text_surface = self.button_text_font.render(
            "OPTIONS", False, (0, 0, 0)
        )

    def run_main_menu(self, p_game_state: const.GameState) -> const.GameState:
        """Run the main menu loop, handling button clicks and transitions to other states."""
        game_state = p_game_state
        self.running = True

        audio.SoundTools.play_music(const.MusicChoice.GAME_MENU)

        self.menu_surface.blit(self.background_surface, (0, 0))

        pygame.draw.rect(
            self.menu_surface,
            "gray",
            self.single_player_rect,
            border_radius=const.MENU_BUTTON_BORDER_RAD,
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
            "gray",
            self.multi_player_rect,
            border_radius=const.MENU_BUTTON_BORDER_RAD,
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
            "gray",
            self.options_rect,
            border_radius=const.MENU_BUTTON_BORDER_RAD,
        )
        self.menu_surface.blit(
            self.option_text_surface,
            (
                self.options_rect.centerx - self.option_text_surface.get_width() / 2,
                self.options_rect.centery - self.option_text_surface.get_height() / 2,
            ),
        )

        while self.running:
            # Poll for events
            for event in pygame.event.get():
                # print(f"event: {event}")
                if event.type == pygame.QUIT:  # pylint: disable=no-member
                    self.running = False
                    game_state = const.GameState.OFF
                if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
                    mouse_clicked_coords_tuple = pygame.mouse.get_pos()

                    if self.single_player_rect.collidepoint(
                        mouse_clicked_coords_tuple[0], mouse_clicked_coords_tuple[1]
                    ):
                        self.running = False
                        game_state = const.GameState.SINGLE_PLAYER

                    elif self.multi_player_rect.collidepoint(
                        mouse_clicked_coords_tuple[0], mouse_clicked_coords_tuple[1]
                    ):
                        self.running = False
                        game_state = const.GameState.MULTIPLAYER

                    elif self.options_rect.collidepoint(
                        mouse_clicked_coords_tuple[0], mouse_clicked_coords_tuple[1]
                    ):
                        self.running = False
                        game_state = const.GameState.OPTIONS

            # menu_surface.fill("black")

            pygame.display.flip()

            self.clock.tick(120)  # limits FPS

        return game_state
