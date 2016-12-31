"""
The Weapon base class
"""
import time
import pygame
from ...managers.messaging import Message
from ..utils.position import Position

class Weapon(object):
    """
    Weapon base class
    A weapon is a self contained entity consisting of
        - Damage
        - Ammo
    """
    def __init__(self, Q, image, ammo_count=1000, sound=None):
        """ ${:TODO Docs} """
        Q.register(self.on_message)
        self.image = pygame.image.load(image).convert_alpha() 
        self.ammo_count = ammo_count
        self.sound = sound 
        self.position = Position((10, 10))
        self._send_message = Q.send_message

        # Weapon specs
        self.rate_of_fire = 5 
        self.time_last_fired = time.time()
        self.offset_x = 10
        self.offset_y = 9 
        self.offset_ammo_x = 5 
        self.offset_ammo_y = -50 

    def _fire(self, payload):
        """ 
        Fire the weapon 
        :param position: tup Coordinate to fire from
        """
        position = payload["position"]
        x, y = position.get()
        x = self.position.x + self.offset_ammo_x 
        y = self.position.y + self.offset_ammo_y 
        new_position = Position((x,y))

        if self.ammo_count <= 0:
            self.ammo_count = 0
            return
        elif (time.time() - self.time_last_fired) > (1/self.rate_of_fire):
            self.time_last_fired = time.time()
            self.ammo_count -= 1 
            message = Message("weapon", "chaosmaker", {
                "type": "create",
                "name": "laser",
                "image": "res/weapons/laser_red.png",
                "position": new_position,
                "velocity": (0, -20),
                "drag": (0,0),
                "rotation": 0,
                "target": None,
                "anim_start": None,
                "anim_end": None,
                })
            self._send_message(message)
            return 
    
    def _move_to(self, position):
        """
        move to a position
        :param position: tuple(x, y)
        """
        x, y = position.get()
        x = x + self.offset_x
        y = y + self.offset_y
        self.position.set_to((x,y))

    def _render(self):
        """ Render the weapon """
        message = Message("weapon", "renderer", {
            "type": "render",
            "image": self.image,
            "position": self.position
            })
        self._send_message(message)

    def on_message(self, message):
        if message.receiver == "all":
            if message.payload["type"] == "render":
                self._render()
        if message.receiver == "weapon":
            if message.payload["type"] == "update_position":
                self._move_to(message.payload["position"])
            if message.payload["type"] == "fire":
                self._fire(message.payload)
        pass
