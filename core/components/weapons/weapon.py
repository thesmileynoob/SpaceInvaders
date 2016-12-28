"""
The Weapon base class
"""
import pygame
class Weapon(object):
    """
    Weapon base class
    A weapon is a self contained entity consisting of
        - Damage
        - Ammo
    """
    _IMAGE="res/weapons/laser_red.png"
    def __init__(self, image=_IMAGE, ammo_count=100, sound=None):
        """ ${:TODO Docs} """
        self.image = pygame.image.load(image).convert_alpha() 
        self.ammo_count = ammo_count
        self.sound = sound 
        self.position = 10,10

    def fire(self):
        """ Fire the weapon """
        if self.ammo_count <= 0:
            self.ammo_count = 0
            return
        else:
            self.ammo_count -= 1 
            print(self.sound)
            return 

    def render(self):
        """ Render the weapon """
        return self.image, self.position

