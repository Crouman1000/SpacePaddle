"""Settings for the game."""

from typing import Optional
import game_constants as gconst


# Game music and sound settings
enable_music: bool = True  # Enable or disable background music
current_song: Optional[gconst.MusicChoice] = None  # Current song being played
music_volume: float = 0.6  # Volume for music playback
