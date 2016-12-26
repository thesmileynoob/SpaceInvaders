"""
The test level
"""

import pygame
from .level import Level
from ..ships.player import Player

class Level0(Level):
    """
    Level 0 for testing
    """
    _NAME = "Area 51"
    _SHIPS = []
    _ENV = {
            "bg": "../../resources/backgrounds/level0.png"
            }

    def __init__(self):
        """ Level0 """
        super(Level0, self).__init__(player=Player())
