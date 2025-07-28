"""This module contains the ImageTools class, which is responsible
for loading and unloading images used in the game."""

import pygame
import game_constants as const


# @final
class ImageTools:
    """This class handles loading and unloading images used in the game."""

    images = {}

    @classmethod
    def load_images(cls) -> None:
        """Load all images used in the game."""
        cls.images[const.ImageChoice.BACKGROUND_MENU] = pygame.image.load(
            const.ImageChoice.BACKGROUND_MENU.value
        )

    @classmethod
    def unload_images(cls) -> None:
        """Unload all loaded images."""
        cls.images.clear()
