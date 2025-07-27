"""This module handles the gameplay mechanics for
both singleplayer and multiplayer modes."""

import pygame
import game_constants as const
import audio
import ball
import paddle
import game_text


class GamePlay:
    """Manage the game play, including player controls,
    ball movement and scoring."""

    def __init__(self):

        self.running = True
        self.start_game = False
        self.clock = pygame.time.Clock()
        self.game_surface = pygame.display.set_mode(
            (const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT)
        )
        self.p1_paddle = paddle.Paddle(const.Player.P1)
        self.p2_paddle = paddle.Paddle(const.Player.P2)
        self.game_ball = ball.Ball()
        self.game_scoreboard = game_text.ScoreBoard("Arial", 25, True, False)

    def run_multiplayer(self, p_game_state: const.GameState):
        """Run the multiplayer game loop, handling player controls,
        ball movement and scoring."""

        game_state = p_game_state
        self.running = True
        self.start_game = False

        audio.SoundTools.play_music(const.MusicChoice.GAME_PLAY)

        while self.running:

            game_state = self.__poll_events(game_state)

            ## Start the game
            if self.start_game:

                ## Wipe away last frames
                self.game_surface.fill("black")
                ## Move the ball
                self.game_ball.travel()
                ## P1 paddle
                self.p1_paddle.control_paddle_player()
                ## P2 paddle
                self.p2_paddle.control_paddle_player()
                ## Handle P1 paddle collisions
                self.p1_paddle.handle_hit_ball(self.game_ball)
                ## Handle P2 paddle collisions
                self.p2_paddle.handle_hit_ball(self.game_ball)
                ## Handle floor and ceiling bounce
                self.__handle_wall_bounce()
                ## Handle goal
                self.__handle_goal()
                ## Blit the score on the screen
                self.game_scoreboard.show_score(self.game_surface)
            else:
                ## Blit texts on the screen
                self.game_scoreboard.show_winner(self.game_surface)
                self.game_scoreboard.show_start(self.game_surface)
                self.game_scoreboard.show_controls(self.game_surface, game_state)

            ## Render game objects
            pygame.draw.rect(self.game_surface, "red", self.p1_paddle)
            pygame.draw.rect(self.game_surface, "green", self.p2_paddle)
            pygame.draw.rect(self.game_surface, "white", self.game_ball)

            ## Blit the game surface
            pygame.display.flip()

            ## Limit FPS
            self.clock.tick(120)

        return game_state

    def run_singleplayer(self, p_game_state: const.GameState):
        """Run the single player game loop, handling player and AI controls,
        ball movement and scoring."""

        game_state = p_game_state
        self.running = True
        self.start_game = False

        audio.SoundTools.play_music(const.MusicChoice.GAME_PLAY)

        while self.running:

            game_state = self.__poll_events(game_state)

            ## Start the game
            if self.start_game:

                ## Wipe away last frames
                self.game_surface.fill("black")
                ## Move the ball
                self.game_ball.travel()
                ## P1 paddle
                self.p1_paddle.control_paddle_player()
                ## Handle P1 paddle collisions
                p1_hit_occured = self.p1_paddle.handle_hit_ball(self.game_ball)
                if p1_hit_occured:
                    self.p2_paddle.calculate_target_ai(self.game_ball)
                ## AI paddle
                self.p2_paddle.control_paddle_ai(self.game_ball)
                ## Handle P2 paddle collisions
                self.p2_paddle.handle_hit_ball(self.game_ball)
                ## Handle floor and ceiling bounce
                self.__handle_wall_bounce()
                ## Handle goal
                self.__handle_goal()
                ## Blit the score on the screen
                self.game_scoreboard.show_score(self.game_surface)
            else:
                ## Blit texts on the screen
                self.game_scoreboard.show_winner(self.game_surface)
                self.game_scoreboard.show_start(self.game_surface)
                self.game_scoreboard.show_controls(self.game_surface, game_state)

            ## Render game objects
            pygame.draw.rect(self.game_surface, "red", self.p1_paddle)
            pygame.draw.rect(self.game_surface, "green", self.p2_paddle)
            pygame.draw.rect(self.game_surface, "white", self.game_ball)

            ## Blit the game surface
            pygame.display.flip()

            ## limit FPS
            self.clock.tick(120)

        return game_state

    def __poll_events(self, p_game_state: const.GameState) -> const.GameState:
        """Polls for events and handles game state transitions."""

        game_state = p_game_state
        ## Poll for events
        for event in pygame.event.get():

            ## Close the game window
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                self.start_game = False
                self.running = False
                game_state = const.GameState.OFF

            elif event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                # print(f"{event.key}=?={pygame.K_ESCAPE}")
                # if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                ### Return to game menu
                if event.key == pygame.K_ESCAPE:  # pylint: disable=no-member
                    self.start_game = False
                    self.running = False
                    game_state = const.GameState.MAIN_MENU
                elif event.key == pygame.K_SPACE:  # pylint: disable=no-member
                    ### Start game
                    self.start_game = True

        return game_state

    def __handle_goal(self) -> None:

        if self.game_ball.x <= 0 or self.game_ball.x >= const.GAME_SURFACE_WIDTH:

            ## Calculate score
            if self.game_ball.x <= 0:
                # print("P2 Scored!")
                self.game_scoreboard.increase_score(const.Player.P2)
                self.game_ball.reset(const.Player.P2)

            else:
                # print("P1 Scored!")
                self.game_scoreboard.increase_score(const.Player.P1)
                self.game_ball.reset(const.Player.P1)

            paddle.PaddleTools.reset_all_paddles(self.p1_paddle, self.p2_paddle)
            self.start_game = False

    def __handle_wall_bounce(self) -> None:

        if (
            self.game_ball.y <= 0
            or self.game_ball.y + self.game_ball.height >= const.GAME_SURFACE_HEIGHT
        ):
            audio.SoundTools.play_sound(const.SoundChoice.Y_WALL_HIT, 1000)
            self.game_ball.reverse_y()
