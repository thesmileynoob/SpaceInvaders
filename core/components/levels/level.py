"""
Base level class
"""
import pygame
from ships.ship import Ship

class Level(object):
    """
    The base Level class
    - Number
    - Ships
    - Environment
    - Sound etc
    """
    _NAME="Generic Level"
    _SHIPS=[]
    _ENV={
            "bg": "../../../resources/backgrounds/level_generic.png",
            "objects": []
            }

    def __init__(self, name=_NAME, ships=_SHIPS, environment=_ENV):
        """ 
        :param name: str The level name 
        :param ships: [`Ship`] list of ships
        :param environment: dict The environment dictionary
        """
        self.number = number
        self.ships = ship
        self.environment = environment
        return 

    def render(self):
        """ Level render method """
         
        return 

