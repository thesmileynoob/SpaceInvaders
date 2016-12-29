"""
The Weapon base class
"""
import pygame
from ...specials.messaging import Message

class Weapon(object):
    """
    Weapon base class
    A weapon is a self contained entity consisting of
        - Damage
        - Ammo
    """
    _IMAGE="res/weapons/laser_red.png"
    def __init__(self, Q, image=_IMAGE, ammo_count=1000, sound=None):
        """ ${:TODO Docs} """
        self.image = pygame.image.load(image).convert_alpha() 
        self.ammo_count = ammo_count
        self.sound = sound 
        self.position = 10,10
        self.send_message = Q.send_message

    def fire(self, position):
        """ Fire the weapon 
        from position 
        """
        if self.ammo_count <= 0:
            self.ammo_count = 0
            return
        else:
            self.ammo_count -= 1 
            message = Message("weapon", "chaosmaker", {
                "name": "laser",
                "image": "res/weapons/laser_red.png",
                "position": position,
                "velocity": (0, -2),
                "drag": (0,0),
                "rotation": 0,
                "target": None,
                "anim_start": None,
                "anim_end": None,
                })
            self.send_message(message)
            print(self.sound)
            return 

    def render(self):
        """ Render the weapon """
        return self.image, self.position

