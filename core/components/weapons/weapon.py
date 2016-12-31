"""
The Weapon base class
"""
import time
import pygame
from ...managers.messaging import Message

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
        Q.register(self.on_message)
        self.image = pygame.image.load(image).convert_alpha() 
        self.ammo_count = ammo_count
        self.sound = sound 
        self.position = 10,10
        self._send_message = Q.send_message
        self.rate_of_fire = 10 
        self.time_last_fired = time.time()

    def _fire(self, payload):
        """ 
        Fire the weapon 
        :param position: tup Coordinate to fire from
        """
        position = payload["position"]
        x, y , _= position
        x = x + self.position[0] + 5
        position = (x, y, _)

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
                "position": position,
                "velocity": (0, -20),
                "drag": (0,0),
                "rotation": 0,
                "target": None,
                "anim_start": None,
                "anim_end": None,
                })
            self._send_message(message)
            return 

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
            if message.payload["type"] == "fire":
                self._fire(message.payload)
        pass
