"""
LaserBlasters
"""
import time
import pygame
from .weapon import Weapon
from ...managers.messaging import Message
from ..utils.position import Position

class LaserBlasterBlue(Weapon):
    """
    Blue-laser blaster
    """
    _IMAGE = "res/weapons/laserBlasterBlue.png"
    _AMMO = "res/ammo/laserBlue01.png"
    _SOUND = "blue bizz"
    def __init__(self, Q, ammo_count=1000):
        """ ${:TODO Docs} """
        Q.register(self.on_message)
        self._send_message = Q.send_message

        self.name = "laser.blaster.blue"
        self.image = pygame.image.load(self._IMAGE).convert_alpha() 
        self.ammo = self._AMMO
        self.sound =  self._SOUND
        self.position = Position((10, 10))

        # Weapon spec
        self.damage = 1
        self.ammo_count = ammo_count
        self.velocity = (0, -20)
        self.drag = (0,0)
        self.rotation = 0
        self.target = None
        self.rate_of_fire = 5 
        self.time_last_fired = time.time()
        self.offset_x = 10
        self.offset_y = 9 
        self.offset_ammo_x = 5 
        self.offset_ammo_y = -50 
        self.anim_start = None
        self.anim_end = None
        
        # State
        self.is_disabled = False

class LaserBlasterRed(Weapon):
    """
    Red-laser blaster
    """
    _IMAGE = "res/weapons/laserBlasterRed.png"
    _AMMO = "res/ammo/laserRed01.png"
    _SOUND = "red bizz"
    def __init__(self, Q, ammo_count=1000):
        """ ${:TODO Docs} """
        Q.register(self.on_message)
        self._send_message = Q.send_message

        self.name = "laser.blaster.red"
        self.image = pygame.image.load(self._IMAGE).convert_alpha() 
        self.ammo = self._AMMO
        self.sound =  self._SOUND
        self.position = Position((0, 0)) #Starting position

        # Weapon spec
        self.damage = 2
        self.ammo_count = ammo_count
        self.velocity = (0, -20)
        self.drag = (0,0)
        self.rotation = 0
        self.target = None
        self.rate_of_fire = 8 
        self.time_last_fired = time.time()
        self.offset_x = 70
        self.offset_y = 9 
        self.offset_ammo_x = 4 
        self.offset_ammo_y = -50 
        self.anim_start = None
        self.anim_end = None
        
        # State
        self.is_disabled = False


