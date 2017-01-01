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
    def __init__(self):
        """ ${:TODO Docs} """
        self.name = None
        self.image = None
        self.ammo = None
        self.sound = None 
        self.position = None

        # Weapon spec
        self.damage = None 
        self.ammo_count = None
        self.velocity = None
        self.drag = None
        self.rotation = None
        self.target = None
        self.rate_of_fire = None
        self.time_last_fired = None
        self.offset_x = None
        self.offset_y = None
        self.offset_ammo_x = None
        self.offset_ammo_y = None
        self.anim_start = None
        self.anim_end = None

        # Internal State
        self.is_disabled = False


    def _fire(self, payload):
        """ 
        Fire the weapon 
        :required payload: Position
        """
        position = payload["position"]
        x, y = position.get()
        x = self.position.x + self.offset_ammo_x 
        y = self.position.y + self.offset_ammo_y 
        fire_position = Position((x,y))

        if self.is_disabled:
            return

        if self.ammo_count <= 0:
            self.is_disabled = True
            self.ammo_count = 0
            return

        if (time.time() - self.time_last_fired) > (1/self.rate_of_fire):
            self.time_last_fired = time.time()
            self.ammo_count -= 1 
            message = Message("weapon", "chaosmaker", {
                "type": "create",
                "name": "laser",
                "image": self.ammo,
                "position": fire_position,
                "damage": self.damage,
                "velocity": self.velocity,
                "drag": self.drag,
                "rotation": self.rotation,
                "target": self.target,
                "anim_start": self.anim_start,
                "anim_end": self.anim_end
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
            if message.payload["type"] == "position.update":
                self._move_to(message.payload["position"])
        if message.receiver == self.name:
            if message.payload["type"] == "fire":
                self._fire(message.payload)
        pass
