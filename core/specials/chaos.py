"""
The projectile/destruction handler
"""
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

    def __init__(self, limit=10):
        """ 
        Manages all the chaos on the screen 
        :param limit: int maximum number of objects on the screen
        """
        self.limit = limit
        self.refs = []
        self.refnames = []

    def on_message(self, message):
        if message.receiver == "chaosmaker":
            self.create_chaos(message.payload)

    def render(self, screen):
        """ Render every object """
        for ref in self.refs:
            screen.blit(*ref.render())
        
    def create_chaos(self, spec):
        """ Create chaos according to spec """
        # if len(self.refs) > self.limit:
            # pass
        # if spec["name"] in self.refnames: 
            # print("duplicate")
        # else:
        if True:
            self.refs.append(Chaos(spec)) 
            self.refnames.append(spec["name"])
        pass

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
        self.position = Position(specs["position"])
        self.velocity = specs["velocity"]
        self.drag = specs["drag"]
        self.rotation = specs["rotation"]
        self.target = specs["target"]
        self.anim_start = specs["anim_start"]
        self.anim_end = specs["anim_end"]
    
    def render(self):
        self.position.update_by(*self.velocity)
        return self.image, self.position.get()

    def on_message(self, message):
        if message.receiver == "all":
            pass

    def _destruct(self):
        """ Self destruct """
        pass
