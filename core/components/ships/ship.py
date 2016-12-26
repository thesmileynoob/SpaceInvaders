"""
Base class ship
"""

import pygame
from ..utils.position import Position
from ..utils.health import Health


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

    def __init__(self, name='Generic', image=_IMAGE, spawn_position=_SPAWNPOSITION, health=None):
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


    def __repr__(self):
        return f"<Ship>\n"\
                "Name: {self.name}\n" \
                "Health: {self.health}\n" \
                "Position: {self.position}\n"

    def move_by(self, vel_x, vel_y):
        """
        Manipulate the Position of the ship
        :param vel_x: int change in x coordinate
        :param vel_y: int change in y coordinate
        :return: None
        """
        self.position.update_by(vel_x, vel_y)
        return

    def get_position(self):
        """ Return a position tuple """
        return self.position.get()

    def rotate_by(self, degrees):
        """ 
        Rotate the ship by degrees 
        :param degrees: int rotation angle change
        """
        self.angle += degrees
        return 

    def fire1(self):
        """ Fire weapon1 if present """
        if(self.weapon1):
            weapon1.fire1()
        else:
            print("pew pew pew")
        return 

    def render(self):
        """
        Ship render method
        :return: (pygame.Surface, (x,y)) tuple
        """
        return self.image, self.get_position()

