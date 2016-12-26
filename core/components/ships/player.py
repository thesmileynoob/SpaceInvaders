"""
The player ship
"""

import pygame
from .ship import Ship
# from .utils.position import Position
# from .utils.health import Health

class Player(Ship):
    """
    The Player ship
    """
    _IMG = "res/ships/ship_player.png"
    _SPAWNPOSITION = (0,0,0)
    _DRAG = (0, 0.1) # Drag velocity delta

    def __init__(self, image=_IMG, spawn_position=_SPAWNPOSITION, health=100, weapon1=None, weapon2=None, weapon3=None, boost=None, drag=_DRAG):
        """
        :param image: str player ship image
        :param spawn_position: `Position` of the ship
        :param health: `Health` of the ship
        :param weapon1: `Weapon` Primary weapon
        :param weapon2: `Weapon` Secondary weapon
        :param weapon3: `Weapon` Special weapon
        :param boost: `Boost` Turbo boost!
        """
        super(Player, self).__init__('Player', image, spawn_position, health=health)
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.weapon3 = weapon3
        self.drag = drag

    def render(self):
        self.move_by(*self.drag) # Always apply drag movement
        return super(Player, self).render()
