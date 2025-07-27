"""This module defines the options menu for the game, allowing user to toggle settings."""

import pygame
import PygameUtils as pu
import settings
import graphics
import audio
import game_constants as const
import game_text


class Menu:
    """This class handles the options menu of the game, allowing users to change settings."""

    def __init__(self):

        self.running = True
        self.clock = pygame.time.Clock()
        self.menu_surface = pygame.display.set_mode(
            (const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT)
        )
        self.background_surface = pygame.transform.scale(
            graphics.ImageTools.images.get(const.ImageChoice.BACKGROUND_MENU),
            (const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT),
        )

        self.game_text = game_text.GameText("Arial", 25, True, False)
        self.escape_surface = self.game_text.render_(
            "PRESS ESC TO QUIT", 0, (255, 255, 0)
        )
        self.music_checkbox = Menu.CheckboxOverriden(
            "red",
            100,
            100,
            50,
            50,
            outline=0,
            check=settings.ENABLE_MUSIC,
            text="MUSIC",
        )

    def run_options(self, p_game_state: const.GameState) -> const.GameState:
        """Run the options menu loop, allowing users to change settings."""
        game_state = p_game_state
        self.running = True

        self.menu_surface.blit(self.background_surface, (0, 0))

        while self.running:

            self.menu_surface.blit(self.background_surface, (0, 0))
            coord_xy = (
                19
                * (self.menu_surface.get_width() - self.escape_surface.get_width())
                / 20,
                1 * self.menu_surface.get_height() / 20,
            )
            self.menu_surface.blit(self.escape_surface, coord_xy)

            # Poll for events
            for event in pygame.event.get():
                # print(f"event: {event}")
                if event.type == pygame.QUIT:  # pylint: disable=no-member
                    self.running = False
                    game_state = const.GameState.OFF
                elif event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                    if event.key == pygame.K_ESCAPE:  # pylint: disable=no-member
                        self.running = False
                        game_state = const.GameState.MAIN_MENU
                elif event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
                    mouse_clicked_coords_tuple = pygame.mouse.get_pos()
                    if self.music_checkbox.isOver(mouse_clicked_coords_tuple):
                        self.music_checkbox.convert()
                        if self.music_checkbox.isChecked():
                            audio.SoundTools.enable_music()
                            audio.SoundTools.play_music(const.MusicChoice.GAME_MENU)
                        else:
                            audio.SoundTools.disable_music()

            self.music_checkbox.draw_(self.menu_surface)
            pygame.display.flip()

            # FPS
            self.clock.tick(120)

        return game_state

    class CheckboxOverriden(pu.checkbox):
        """Overridden PygameUtils Checkbox class."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        # @override
        def draw_(self, win):
            """Draw the checkbox with custom text and check state."""
            but = pu.button(
                self.color,
                self.x,
                self.y,
                self.width,
                self.height,
                outline=self.outline,
            )
            but.draw(win)

            if self.text != "":
                text = self.font.render(self.text, 1, (255, 255, 255))
                win.blit(
                    text,
                    (
                        self.x + self.width + self.textGap,
                        self.y + (self.height / 2 - text.get_height() / 2),
                    ),
                )

            if self.check:
                pygame.draw.line(
                    win,
                    (255, 255, 255),
                    (self.x, self.y),
                    (
                        self.x + self.width - self.outline,
                        self.y + self.height - self.outline,
                    ),
                    3,
                )
                pygame.draw.line(
                    win,
                    (255, 255, 255),
                    (self.x - self.outline + self.width, self.y),
                    (self.x, self.y + self.height - self.outline),
                    3,
                )
