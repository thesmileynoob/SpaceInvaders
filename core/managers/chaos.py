"""
The projectile/destruction handler
"""
import time
import pygame
from ..components.utils.position import Position

class ChaosMaker(object):
    """
    Every object handled by chaos must be have an 
    image: path/to/img
    origin position: (x, y)
    starting animation,
    initial velocity,
    drag,
    rotation,
    target
    """

    def __init__(self, Q, limit=10):
        """ 
        Manages all the chaos on the screen 
        :param Q: 
        :param limit: int maximum number of objects on the screen
        """
        Q.register(self.on_message)
        self.limit = limit
        self.refs = []

    def on_message(self, message):
        if message.receiver == "all":
            if message.payload["type"] == "tick":
                self._tick()
        if message.receiver == "chaosmaker":
            if message.payload["type"] == "create":
                self._create_chaos(message.payload)

    def _tick(self):
        """ Managers/makers dont tick"""
        if len(self.refs) == 0:
            return
        for ref in self.refs:
            ref.tick()
            if ref.position.y < 0:
                del self.refs[self.refs.index(ref)]
        return

    def render(self, screen):
        """ Render every object """
        for ref in self.refs:
            screen.blit(*ref.render())
        
    def _create_chaos(self, spec):
        """ Create chaos according to spec """
        self.refs.append(Chaos(spec)) 

class Chaos(object):
    """ The chaos object for creating chaos!
    image: path/to/img
    origin position: (x, y)
    starting animation,
    initial velocity,
    drag,
    rotation,
    target
    """
    def __init__(self, specs):
        self.image = pygame.image.load(specs["image"]).convert_alpha()
        self.position = Position(specs["position"].get())
        self.velocity = specs["velocity"]
        self.drag = specs["drag"]
        self.rotation = specs["rotation"]
        self.target = specs["target"]
        self.anim_start = specs["anim_start"]
        self.anim_end = specs["anim_end"]

    def tick(self):
        self.position.update_by(self.velocity)
    
    def render(self):
        return self.image, self.position.get()

    def on_message(self, message):
        if message.receiver == "world":
            if message.payload["type"] == "tick":
                self._tick()
        elif message.receiver == "chaosmaker":
            if message.payload["type"] == "create":
                self._create_chaos(message.payload)

    def __del__(self):
        """ Self destruct """
        pass
