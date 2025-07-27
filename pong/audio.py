"""This module handles audio management for the game,
including loading, playing, and unloading sounds and music."""

import os
import typing
import pygame
import game_constants as const
import settings


AnyPath = typing.Union[str, bytes, os.PathLike[str], os.PathLike[bytes]]
FileArg = typing.Union[AnyPath, typing.IO[bytes], typing.IO[str]]


# @final
class SoundTools:
    """This class handles loading, unloading, and playing sounds and music."""

    sounds = {}
    musics = {}

    @classmethod
    def load_sounds(cls):
        """Load all sound effects used in the game."""
        pygame.mixer.init()
        # Sound
        cls.sounds[const.SoundChoice.PADDLE_HIT] = pygame.mixer.Sound(
            const.SoundChoice.PADDLE_HIT.value
        )
        cls.sounds[const.SoundChoice.Y_WALL_HIT] = pygame.mixer.Sound(
            const.SoundChoice.Y_WALL_HIT.value
        )
        cls.sounds[const.SoundChoice.VICTORY] = pygame.mixer.Sound(
            const.SoundChoice.VICTORY.value
        )

    @classmethod
    def unload_audio(cls) -> None:
        """Unload all loaded sounds and music."""
        cls.sounds.clear()
        cls.musics.clear()

    @classmethod
    def play_sound(cls, p_sound_choice: const.SoundChoice, p_max_time=None) -> None:
        """Play a sound effect based on the provided choice."""
        sound: typing.Optional[pygame.mixer.Sound] = cls.sounds.get(p_sound_choice)
        if sound:
            if p_max_time:
                sound.play(maxtime=p_max_time)
            else:
                sound.play()

    @staticmethod
    def play_music(p_song: const.MusicChoice) -> None:
        """Play background music based on the provided choice."""
        if settings.ENABLE_MUSIC:

            match p_song:

                case const.MusicChoice.GAME_MENU:

                    if settings.CURRENT_SONG != const.MusicChoice.GAME_MENU:
                        pygame.mixer.music.load(const.MusicChoice.GAME_MENU.value)
                        pygame.mixer.music.play(-1)
                        settings.CURRENT_SONG = const.MusicChoice.GAME_MENU

                case const.MusicChoice.GAME_PLAY:

                    if settings.CURRENT_SONG != const.MusicChoice.GAME_PLAY:
                        pygame.mixer.music.load(const.MusicChoice.GAME_PLAY.value)
                        pygame.mixer.music.play(-1)
                        settings.CURRENT_SONG = const.MusicChoice.GAME_PLAY

    @staticmethod
    def disable_music() -> None:
        """Stop and unload the currently playing music."""
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        settings.CURRENT_SONG = None
        settings.ENABLE_MUSIC = False

    @staticmethod
    def enable_music() -> None:
        """Enable music playback."""
        settings.ENABLE_MUSIC = True

    # def controlSound(p_sound: pygame.mixer.,p_state: const.SoundState) -> None:

    #    if not p_sound.get_busy():
    #        if p_state == const.SoundState.On:
    #            p_sound.play(-1,0,0)
    #        elif p_state == const.SoundState.On:
    #            p_sound.stop()
