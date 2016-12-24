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

    def __init__(self, image, spawn_position, name='Generic', health=100, shield=100, max_health=100,max_shield=100):
        """
        :param image: str image name
        :param spawn_position: tuple(int x, int y, int z)
        :param name: str Name of the ship
        """
        self.image = pygame.image.load(image).convert()

        self.position = Position(spawn_position[0], spawn_position[1], spawn_position[2])
        self.name = name
        self.health = Health(health, shield, max_health, max_shield)

    def __repr__(self):
        return "Ship: {name}\n" \
               "Health: {health}\n" \
               "Position: {x}\n".format(name=self.name, health=self.health.health,
                                           x=self.get_position())

    def pimg(self):
        """
        Get the pygame.Surface obj
        :return: pygame.Surface
        """
        return self.image

    def move(self, vel_x, vel_y):
        """
        Manipulate the Position of the ship
        :param vel_x: int change in x coordinate
        :param vel_y: int change in y coordinate
        :return: None
        """
        self.position.update_delta(vel_x, vel_y)
        return

    def get_position(self):
        return self.position.x, self.position.y

    def makesound(self):
        pass