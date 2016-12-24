"""
The main loop of the game 
"""
import sys
import time
import pygame
from .CONFIG import CONFIG

from .components.ships.ship import Ship

def start_game():
    """
    Initialize pygame, check saved files, and run the main loop
    """
    pygame.init()
    screen = pygame.display.set_mode(CONFIG.window_size)
    ship = Ship("resources/ships/playership.png", (50,0,0), "hero")


    while 1:
        for event in pygame.event.get():
            print event
            if event.type == pygame.QUIT: sys.exit()

        #TODO Make an independent render method

        screen.blit(ship.pimg(), ship.get_position())
        ship.move(0.1,0)
        pygame.display.flip()
        screen.fill((0,0,0))

        ship.move(0, 0.12)
        screen.blit(ship.pimg(), ship.get_position())
        pygame.display.flip()
        time.sleep(0.012)

    pass
