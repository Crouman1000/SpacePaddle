import os
import typing
import pygame
import game_constants as const
import settings


AnyPath = typing.Union[str, bytes, os.PathLike[str], os.PathLike[bytes]]
FileArg = typing.Union[AnyPath, typing.IO[bytes], typing.IO[str]]


#@final
class soundTools():

    sounds = {}
    musics = {}

    @classmethod
    def loadSounds(cls):

        pygame.mixer.init()
        # Sound
        cls.sounds[const.SoundChoice.paddleHit] = pygame.mixer.Sound(const.SoundChoice.paddleHit.value)
        cls.sounds[const.SoundChoice.yWallHit] = pygame.mixer.Sound(const.SoundChoice.yWallHit.value)
        cls.sounds[const.SoundChoice.victory] = pygame.mixer.Sound(const.SoundChoice.victory.value)  

    @classmethod
    def unloadAudio(cls) -> None:
        cls.sounds.clear()
        cls.musics.clear()

    @classmethod
    def playSound(cls,p_soundChoice: const.SoundChoice, p_maxTime=None) -> None:
        
        sound: typing.Optional[pygame.mixer.Sound] = cls.sounds.get(p_soundChoice)
        if sound:
            if p_maxTime:
                sound.play(maxtime=p_maxTime)
            else:
                sound.play()

    @staticmethod
    def playMusic(p_song: const.MusicChoice) -> None:
        
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

    @staticmethod    
    def disableMusic() -> None:

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        settings.currentSong = None
        settings.enableMusic = False

    @staticmethod
    def enableMusic() -> None:

        settings.enableMusic = True

    

    #def controlSound(p_sound: pygame.mixer.,p_state: const.SoundState) -> None:
#    if not p_sound.get_busy():
#        if p_state == const.SoundState.On:
#            p_sound.play(-1,0,0)
#        elif p_state == const.SoundState.On:
#            p_sound.stop()