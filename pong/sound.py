
import pygame
import game_constants as const
import os
import typing
import settings


# This file is treated like a singleton

AnyPath = typing.Union[str, bytes, os.PathLike[str], os.PathLike[bytes]]
FileArg = typing.Union[AnyPath, typing.IO[bytes], typing.IO[str]]

pygame.mixer.init()

paddleHit_sound = pygame.mixer.Sound("pong/assets/sounds/paddle_hit.mp3")
YwallHit_sound = pygame.mixer.Sound("pong/assets/sounds/yWall_hit.mp3")
victory_sound = pygame.mixer.Sound("pong/assets/sounds/victory.mp3")


#def controlSound(p_sound: pygame.mixer.,p_state: const.SoundState) -> None:
#    if not p_sound.get_busy():
#        if p_state == const.SoundState.On:
#            p_sound.play(-1,0,0)
#        elif p_state == const.SoundState.On:
#            p_sound.stop()

def playMusic(p_song:const.MusicChoice):
    
    if settings.enableMusic:

        match p_song:

            case const.MusicChoice.gameMenu:       
                
                if settings.currentSong != const.MusicChoice.gameMenu:
                    pygame.mixer.music.load(const.MusicChoice.gameMenu.value)
                    pygame.mixer.music.play(-1)
                    settings.currentSong = const.MusicChoice.gameMenu

            case const.MusicChoice.gamePlay:

                if settings.currentSong != const.MusicChoice.gamePlay:
                    pygame.mixer.music.load(const.MusicChoice.gamePlay.value)
                    pygame.mixer.music.play(-1)
                    settings.currentSong = const.MusicChoice.gamePlay
            
def disableMusic() -> None:

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    settings.currentSong = None
    settings.enableMusic = False

def enableMusic() -> None:

    settings.enableMusic = True