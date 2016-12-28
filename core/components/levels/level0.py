"""
The test level
"""

import pygame
from .level import Level
from ..ships.player import Player
from ..weapons.weapon import Weapon

class Level0(Level):
    """
    Level 0 for testing
    """
    _NAME = "Area 51"
    _SHIPS = []
    _ENV = {
            "bg": "../../resources/backgrounds/level0.png"
            }

    def __init__(self, Q):
        """ Level0 """
        Q.register(self.on_message)
        self.name = "Level0"
        self.player = Player(Q, "res/ships/ship_player.png", spawn_position=(0,0,0), health=100, weapon1=Weapon(image="res/weapons/gun_1.png", sound="Shinn!"))
        self.ships = []
        self.environment = {
                            "bg": "res/backgrounds/level_generic.png",
                            "objects": []
                            }
        self.bg = pygame.image.load(self.environment['bg']).convert_alpha()
        self.xx = 0
        self.yy = 0
        # super(Level0, self).__init__()

    def on_message(self, message):
        return
