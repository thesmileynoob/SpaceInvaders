"""
Base class ship
"""

import pygame
from ..utils.position import Position
from ..utils.health import Health
from ...managers.messaging import Message


class Ship(object):
    """
    Base ship class
    A ship is composed of the following components
        - Helath
        - Weapons
    """

    # Generic Ship defaults
    _IMAGE = "res/ships/ship_generic.png"
    _SPAWNPOSITION = (0,0,0)

    def __init__(self, name, image, spawn_position, health, weapon1):
        """
        :param name: str Name of the ship
        :param image: str image name
        :param spawn_position: tuple(int x, int y, int z)
        :param health: tuple(int health, int shield, int max_health, int max_shield)
        """
        self.image = pygame.image.load(image).convert_alpha()
        self.position = Position(spawn_position)
        self.name = name
        self.health = Health(health)
        self.weapon1 = weapon1


    def __repr__(self):
        return f"<Ship>\n"\
                f"Name: {self.name}\n" \
                f"Health: {self.health}\n" \
                f"Weapon1: {self.weapon1}\n"\
                f"Position: {self.position}\n"

    def _move_by(self, deltas):
        """
        Manipulate the Position of the ship and announce
        :param vel_x: int change in x coordinate
        :param vel_y: int change in y coordinate
        :return: None
        """
        self.position.update_by(deltas)
        message = Message("ship", "weapon", {
            "type": "update_position",
            "position": self.position
            })
        self._send_message(message)
        return

    def render(self):
        """
        Ship render method
        :return: (pygame.Surface, (x,y)) tuple
        """
        return self.image, self._get_position()

    def _tick(self, payload):
        self._move_by(self.drag)
        self._on_input(payload["keys"])

    def _get_position(self):
        """ Return a position tuple """
        return self.position.get()

    def _rotate_by(self, degrees):
        """ 
        Rotate the ship by degrees 
        :param degrees: int rotation angle change
        """
        self.angle += degrees
        return 

    def _fire_weapon(self):
        """ Fire weapons if present """
        if(self.weapon1):
            message = Message("player", "weapon", {
                "type": "fire",
                "position": self.position
                })
            self._send_message(message)
        else:
            print("pew pew pew")
        return 

