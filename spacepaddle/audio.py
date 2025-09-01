"""This module handles audio management for the game,
including loading, playing, and unloading sounds and music."""

# import os
from typing import Optional
import pygame
import game_constants as gconst
import settings


# @final
class SoundTools:
    """This class handles loading, unloading, and playing sounds and music."""

    sounds: dict[gconst.SoundChoice, pygame.mixer.Sound] = {}
    musics: dict[gconst.SoundChoice, pygame.mixer.Sound] = {}

    @classmethod
    def load_sounds(cls):
        """Load all sound effects used in the game."""
        pygame.mixer.init()

        cls.sounds[gconst.SoundChoice.PADDLE_HIT] = pygame.mixer.Sound(
            gconst.SoundChoice.PADDLE_HIT.value
        )
        cls.sounds[gconst.SoundChoice.Y_WALL_HIT] = pygame.mixer.Sound(
            gconst.SoundChoice.Y_WALL_HIT.value
        )
        cls.sounds[gconst.SoundChoice.VICTORY] = pygame.mixer.Sound(
            gconst.SoundChoice.VICTORY.value
        )

    @classmethod
    def unload_audio(cls) -> None:
        """Unload all loaded sounds and music."""
        cls.sounds.clear()
        cls.musics.clear()

    @classmethod
    def play_sound(
        cls, p_sound_choice: gconst.SoundChoice, p_max_time: int = 0
    ) -> None:
        """Play a sound effect based on the provided choice."""
        sound: Optional[pygame.mixer.Sound] = cls.sounds.get(p_sound_choice)
        if sound:
            if p_max_time:
                sound.play(maxtime=p_max_time)
            else:
                sound.play()

    @staticmethod
    def play_music(p_song: gconst.MusicChoice) -> None:
        """Play background music based on the provided choice."""
        if settings.enable_music:

            match p_song:

                case gconst.MusicChoice.GAME_MENU:

                    if settings.current_song != gconst.MusicChoice.GAME_MENU:
                        pygame.mixer.music.load(gconst.MusicChoice.GAME_MENU.value)
                        pygame.mixer.music.set_volume(settings.music_volume)
                        pygame.mixer.music.play(loops=-1, start=3)
                        settings.current_song = gconst.MusicChoice.GAME_MENU

                case gconst.MusicChoice.GAME_PLAY:

                    if settings.current_song != gconst.MusicChoice.GAME_PLAY:
                        pygame.mixer.music.load(gconst.MusicChoice.GAME_PLAY.value)
                        pygame.mixer.music.set_volume(settings.music_volume)
                        pygame.mixer.music.play(-1)
                        settings.current_song = gconst.MusicChoice.GAME_PLAY

    @staticmethod
    def disable_music() -> None:
        """Stop and unload the currently playing music."""
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        settings.current_song = None
        settings.enable_music = False

    @staticmethod
    def enable_music() -> None:
        """Enable music playback."""
        settings.enable_music = True

    # def controlSound(p_sound: pygame.mixer.,p_state: const.SoundState) -> None:
    #    if not p_sound.get_busy():
    #        if p_state == const.SoundState.On:
    #            p_sound.play(-1,0,0)
    #        elif p_state == const.SoundState.On:
    #            p_sound.stop()
    #
