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

    def __init__(self, Q):
        """ Level0 """
        Q.register(self.on_message)
        super(Level0, self).__init__(
                name="Level0",
                player=Player(Q, "res/ships/ship_player.png", spawn_position=(0,0,0), health=100, weapon1=Weapon(Q, image="res/weapons/gun_1.png", sound="Shinn!")),
                ships = [],
                environment = {
                    "bg": "res/backgrounds/level_generic.png",
                    "objects": []
                    },
                )

    def on_message(self, message):
        return
