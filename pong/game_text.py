"""This module defines the GameText class and Scoreboard class
for rendering text and holding the score in the game."""

from typing import Iterable, Union, Literal, Tuple
import pygame
import audio
import game_constants as const


ColorType = Union[Tuple[int, int, int], Tuple[int, int, int, int], str, pygame.Color]


class GameText:
    """Base class for rendering text in the game."""

    def __init__(
        self,
        p_font_name: Union[str, bytes, Iterable[Union[str, bytes]], None],
        p_font_size: int,
        p_is_font_bold: bool = False,
        p_is_font_italic: bool = False,
    ):

        self.font = pygame.font.SysFont(
            p_font_name, p_font_size, p_is_font_bold, p_is_font_italic
        )
        self.coord_xy = None

    def render_(
        self,
        p_text: str | bytes | None,
        p_antialias: bool | Literal[0, 1],
        p_color: ColorType = (255, 255, 255),
        p_background: ColorType | None = None,
    ) -> pygame.Surface:
        """Render text to a surface with the specified color and background."""
        return self.font.render(p_text, p_antialias, p_color, p_background)


class ScoreBoard(GameText):
    """Class for managing and displaying the game score."""

    def __init__(self, p_name, p_size, p_bold, p_italic):
        super().__init__(p_name, p_size, p_bold, p_italic)
        self.score_p1 = 0
        self.score_p2 = 0
        self.last_winner = None
        self.game_over = False

        self.score_surface = self.render_(
            f"SCORE: P1 {self.score_p1} | P2 {self.score_p2}", 0, (255, 255, 255)
        )
        self.start_surface = self.render_("PRESS SPACEBAR TO START", 0, (255, 255, 255))
        self.control_surface_p1 = self.render_(
            " P1 CONTROLS  |   Move up: W     Move down: S ", 0, (255, 255, 0)
        )
        self.control_surface_p2 = self.render_(
            " P2 CONTROLS  |   Move up: ↑      Move down: ↓ ", 0, (255, 255, 0)
        )
        self.escape_surface = self.render_("PRESS ESC TO QUIT", 0, (255, 255, 0))
        self.who_scored_surface = None
        self.winner_surface = None

    def increase_score(self, p_player: const.Player) -> None:
        """Increase the score for the player who scored."""
        self.last_winner = p_player.value
        match p_player:
            case const.Player.P1:
                self.score_p1 += 1
            case const.Player.P2:
                self.score_p2 += 1
        if self.score_p1 == const.GAME_MAXSCORE or self.score_p2 == const.GAME_MAXSCORE:
            self.game_over = True

        self.score_surface = self.render_(
            f"SCORE: P1 {self.score_p1} | P2 {self.score_p2}", 0, (255, 255, 255)
        )

    def show_score(self, p_canvas: pygame.Surface) -> None:
        """Display the current score on the given surface."""

        self.coord_xy = (
            (p_canvas.get_width() - self.score_surface.get_width()) / 2,
            p_canvas.get_height() / 12,
        )
        p_canvas.blit(self.score_surface, self.coord_xy)

    def show_winner(self, p_canvas: pygame.Surface) -> None:
        """Display the round or game winner message"""
        if self.last_winner:

            message_color_tuple = (255, 0, 0) if self.last_winner == 1 else (0, 255, 0)

            if self.game_over:
                ## If the game is over, display the final winner message
                audio.SoundTools.play_sound(const.SoundChoice.VICTORY)
                self.winner_surface = self.render_(
                    f"Player {self.last_winner} HAS WON THE GAME!",
                    0,
                    message_color_tuple,
                )
                self.coord_xy = (
                    (p_canvas.get_width() - self.winner_surface.get_width()) / 2,
                    3 * p_canvas.get_height() / 10,
                )
                p_canvas.blit(self.winner_surface, self.coord_xy)
                self.__reset_score()

            else:
                ## If the game is still ongoing, display who scored
                self.who_scored_surface = self.render_(
                    f"PLAYER {self.last_winner} SCORED !", 0, message_color_tuple
                )
                self.coord_xy = (
                    (p_canvas.get_width() - self.who_scored_surface.get_width()) / 2,
                    3 * p_canvas.get_height() / 10,
                )
                p_canvas.blit(self.who_scored_surface, self.coord_xy)

    def show_start(self, p_canvas: pygame.Surface) -> None:
        """Display the start message on the given surface."""
        self.coord_xy = (
            (p_canvas.get_width() - self.start_surface.get_width()) / 2,
            4 * p_canvas.get_height() / 10,
        )
        p_canvas.blit(self.start_surface, self.coord_xy)

    def show_controls(
        self, p_canvas: pygame.Surface, p_game_state: const.GameState
    ) -> None:
        """Display the controls for players."""

        self.coord_xy = (
            19 * (p_canvas.get_width() - self.escape_surface.get_width()) / 20,
            1 * p_canvas.get_height() / 20,
        )
        p_canvas.blit(self.escape_surface, self.coord_xy)
        self.coord_xy = (
            (p_canvas.get_width() - self.control_surface_p2.get_width()) / 2,
            17 * p_canvas.get_height() / 20,
        )
        p_canvas.blit(self.control_surface_p1, self.coord_xy)
        if p_game_state == const.GameState.MULTIPLAYER:
            self.coord_xy = (
                (p_canvas.get_width() - self.control_surface_p2.get_width()) / 2,
                18 * p_canvas.get_height() / 20,
            )
            p_canvas.blit(self.control_surface_p2, self.coord_xy)

    def __reset_score(self) -> None:
        """Reset the score for a new game."""
        self.last_winner = None
        self.game_over = False
        self.score_p1 = 0
        self.score_p2 = 0
        self.score_surface = self.render_(
            f"SCORE: P1 {self.score_p1} | P2 {self.score_p2}", 0, (255, 255, 255)
        )
