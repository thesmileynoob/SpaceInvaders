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
        super(Player, self).__init__(name='Player', image=image, spawn_position=spawn_position, health=health, weapon1=weapon1)
        self.weapon2 = weapon2
        self.weapon3 = weapon3
        self.drag = drag
        Q.register(self.on_message)
        self.send_message = Q.send_message
        self.equippedWeapon = weapon1
        print("initcled")


    def render(self):
        if self.equippedWeapon != None:
            self.image.blit(*self.weapon1.render())
            return self.image, self.get_position()
        else:
            return self.image, self.get_position()

    def on_message(self, message):
        """ React to the event """
        if message.sender == "world":
            if message.payload["type"] == "tick":
                self._tick(message.payload)
        else:
            pass

    def _on_input(self, keys):
        """ Handle input """
        VEL_X = 5
        VEL_Y = 5
        VEL_DIAG = 7
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                self.move_by(-VEL_X, -VEL_DIAG)
            elif keys[pygame.K_DOWN]:
                self.move_by(-VEL_X, VEL_DIAG)
            else:
                self.move_by(-VEL_X, 0)

        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_UP]:
                self.move_by(VEL_X, -VEL_DIAG)
            elif keys[pygame.K_DOWN]:
                self.move_by(VEL_X, VEL_DIAG)
            else:
                self.move_by(VEL_X, 0)

        elif keys[pygame.K_UP]:
            if keys[pygame.K_LEFT]:
                self.move_by(-VEL_DIAG, -VEL_Y)
            elif keys[pygame.K_RIGHT]:
                self.move_by(VEL_DIAG, -VEL_Y)
            else:
                self.move_by(0, -VEL_Y)

        elif keys[pygame.K_DOWN]:
            if keys[pygame.K_LEFT]:
                self.move_by(-VEL_DIAG, VEL_Y)
            elif keys[pygame.K_RIGHT]:
                self.move_by(VEL_DIAG, VEL_Y)
            else:
                self.move_by(0, VEL_Y)

        if keys[pygame.K_SPACE]:
            x, y = self.get_position()
            z = 0
            self.fire1((x, y, z))

        if keys[pygame.K_e]:
            print("removing weapon")
            self.equippedWeapon = None
            

