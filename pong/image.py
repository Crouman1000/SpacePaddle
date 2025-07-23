import pygame
import game_constants as const


#@final
class imageTools():

    images = {}

    @classmethod
    def loadImages(cls) -> None:
        cls.images[const.imageChoice.backgroundMenu] = pygame.image.load(const.imageChoice.backgroundMenu.value)

    @classmethod
    def unloadImages(cls) -> None:
        cls.images.clear()