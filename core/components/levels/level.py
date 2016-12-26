"""
Base level class
"""
import pygame
from ..ships.ship import Ship
from ..ships.player import Player

class Level(object):
    """
    The base Level class
    - Number
    - Ships
    - Environment
    - Sound etc
    """
    _NAME = "Generic Level"
    _PLAYER = Player
    _SHIPS=[]
    _ENV={
            "bg": "res/backgrounds/level_generic.png",
            "objects": []
            }

    def __init__(self, name=_NAME, player=_PLAYER, ships=_SHIPS, environment=_ENV):
        """ 
        :param name: str The level name 
        :param player: `Player` Player ship
        :param ships: [`Ship`] list of enemy ships
        :param environment: dict The environment dictionary
        """
        self.name = name
        self.player = player
        self.ships = ships
        self.environment = environment
        self.bg = pygame.image.load(self.environment['bg']).convert_alpha()
        self.xx = 0
        self.yy = 0

    def render(self):
        """ Level render method """ #TODO
        if (self.yy <= 256): # A lil bit of parallax
            self.yy += 0.5
        else:
            self.yy = 0

        self.bgarray =  [(self.xx+0,self.yy-256),   (self.xx+256,self.yy-256),   (self.xx+512, self.yy-256),
                         (self.xx+0,self.yy+0),   (self.xx+256,self.yy+0),   (self.xx+512, self.yy+0),
                         (self.xx+0,self.yy+256), (self.xx+256,self.yy+256), (self.xx+512, self.yy+256),
                         (self.xx+0,self.yy+512), (self.xx+256,self.yy+512), (self.xx+512, self.yy+512)]

        return self.bg, self.bgarray

