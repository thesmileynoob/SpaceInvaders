"""
The player ship
"""

import pygame
from .ship import Ship

class Player(Ship):
    """
    The Player ship
    """
    _IMG = "res/ships/ship_player.png"
    _SPAWNPOSITION = (0,0,0)
    _DRAG = (0, 0.1) # Drag velocity delta

    def __init__(self, Q, image=_IMG, spawn_position=_SPAWNPOSITION, health=100, weapon1=None, weapon2=None, weapon3=None, boost=None, drag=_DRAG):
        """
        :param Q: `MessageQueue` The message queue
        :param image: str player ship image
        :param spawn_position: `Position` of the ship
        :param health: `Health` of the ship
        :param weapon1: `Weapon` Primary weapon
        :param weapon2: `Weapon` Secondary weapon
        :param weapon3: `Weapon` Special weapon
        :param boost: `Boost` Turbo boost!
        """
        super(Player, self).__init__(name='Player', image=image, spawn_position=spawn_position, health=health)
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.weapon3 = weapon3
        self.drag = drag
        Q.register(self.on_message)
        self.send_message = Q.send_message

    def render(self):
        """ Public """
        self.move_by(*self.drag) # Always apply drag movement
        return super(Player, self).render()

    def on_message(self, message):
        """ React to the event """
        self._on_input(message["keys"])
        return

    def _on_input(self, keys):
        """ Handle input """
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                self.move_by(-3, -5)
            elif keys[pygame.K_DOWN]:
                self.move_by(-3, 5)
            else:
                self.move_by(-5, 0)

        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_UP]:
                self.move_by(3, -5)
            elif keys[pygame.K_DOWN]:
                self.move_by(3, 5)
            else:
                self.move_by(5, 0)
        elif keys[pygame.K_UP]:
            if keys[pygame.K_LEFT]:
                self.move_by(-3, -5)
            elif keys[pygame.K_RIGHT]:
                self.move_by(3, -5)
            else:
                self.move_by(0, -5)
        elif keys[pygame.K_DOWN]:
            if keys[pygame.K_LEFT]:
                self.move_by(-3, 5)
            elif keys[pygame.K_RIGHT]:
                self.move_by(3, 5)
            else:
                self.move_by(0, 5)
        if keys[pygame.K_SPACE]:
            self.fire1()
