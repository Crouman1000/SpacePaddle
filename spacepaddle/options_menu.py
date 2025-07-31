"""This module defines the options menu for the game, allowing user to toggle settings."""

from typing import Tuple, Any
import pygame
import PygameUtils as pu  # type: ignore
import settings
import graphics
import audio
import game_constants as gconst
import game_text


class Menu:
    """This class handles the options menu of the game, allowing users to change settings."""

    def __init__(self):

        self.running = True
        self.clock = pygame.time.Clock()
        self.menu_surface = pygame.display.set_mode(
            (gconst.GAME_SURFACE_WIDTH, gconst.GAME_SURFACE_HEIGHT)
        )
        self.background_surface = pygame.transform.scale(
            graphics.ImageTools.images[gconst.ImageChoice.BACKGROUND_MENU],
            (gconst.GAME_SURFACE_WIDTH, gconst.GAME_SURFACE_HEIGHT),
        )

        self.game_text = game_text.GameText("Arial", 25, True, False)
        self.escape_surface = self.game_text.render_(
            "PRESS ESC TO QUIT", 0, gconst.Color.YELLOW.value
        )
        self.music_checkbox = Menu.CheckboxOverriden(
            "red",
            100,
            100,
            50,
            50,
            outline=0,
            check=settings.enable_music,
            text="MUSIC",
        )

    def run_options(self, p_game_state: gconst.GameState) -> gconst.GameState:
        """Run the options menu loop, allowing users to change settings."""
        game_state = p_game_state
        self.running = True

        ## Main loop of the menu
        while self.running:

            ## Render the background
            self.menu_surface.blit(self.background_surface, (0, 0))
            coord_xy = (
                19
                * (self.menu_surface.get_width() - self.escape_surface.get_width())
                / 20,
                1 * self.menu_surface.get_height() / 20,
            )
            self.menu_surface.blit(self.escape_surface, coord_xy)

            ## Poll for events
            for event in pygame.event.get():
                # print(f"event: {event}")
                if event.type == pygame.QUIT:  # pylint: disable=no-member
                    self.running = False
                    game_state = gconst.GameState.OFF
                elif event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                    if event.key == pygame.K_ESCAPE:  # pylint: disable=no-member
                        self.running = False
                        game_state = gconst.GameState.MAIN_MENU
                elif event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
                    ## Check which button was clicked
                    mouse_clicked_coords_tuple = pygame.mouse.get_pos()
                    if self.music_checkbox.is_over_(mouse_clicked_coords_tuple):
                        self.music_checkbox.convert()
                        if self.music_checkbox.isChecked():
                            audio.SoundTools.enable_music()
                            audio.SoundTools.play_music(gconst.MusicChoice.GAME_MENU)
                        else:
                            audio.SoundTools.disable_music()

            self.music_checkbox.draw_(self.menu_surface)

            ## Update the display on the screen
            pygame.display.flip()

            ## Limit FPS
            self.clock.tick(120)

        return game_state

    # Overridden Checkbox class of the untyped PygameUtils library
    class CheckboxOverriden(pu.checkbox):
        """Overridden PygameUtils Checkbox class."""

        # @override
        def __init__(self, *args: Any, **kwargs: Any):
            super().__init__(*args, **kwargs)  # type: ignore

        # @override
        def is_over_(self, pos: Tuple[int, int]) -> bool:
            """Check if the given position is over the checkbox."""
            return super().isOver(pos)  # type: ignore

        # @override
        def draw_(self, win: pygame.Surface) -> None:
            """Draw the checkbox with custom text and check state."""

            checkbox_text_color = gconst.Color.WHITE.value
            checkbox_x_color = gconst.Color.WHITE.value
            button = pu.button(
                self.color,  # type: ignore
                self.x,  # type: ignore
                self.y,  # type: ignore
                self.width,  # type: ignore
                self.height,  # type: ignore
                outline=self.outline,
            )
            button.draw(win)  # type: ignore

            if self.text != "":
                text = self.font.render(self.text, 1, checkbox_text_color)
                win.blit(
                    text,
                    (
                        self.x + self.width + self.textGap,  # type: ignore
                        self.y + (self.height / 2 - text.get_height() / 2),
                    ),
                )

            if self.check:
                pygame.draw.line(
                    win,
                    checkbox_x_color,
                    (self.x, self.y),
                    (
                        self.x + self.width - self.outline,  # type: ignore
                        self.y + self.height - self.outline,
                    ),
                    3,
                )
                pygame.draw.line(
                    win,
                    checkbox_x_color,
                    (self.x - self.outline + self.width, self.y),  # type: ignore
                    (self.x, self.y + self.height - self.outline),  # type: ignore
                    3,
                )
