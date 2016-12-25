"""
The main loop of the game 
"""
import sys
import time
import pygame
from .CONFIG import CONFIG
import pdb

from .components.ships.ship import Ship


def setup_window():
    pygame.init()
    pygame.display.set_caption(CONFIG.window_title)




def start_game():
    """
    Initialize pygame, check saved files, and run the main loop
    """
    clock = pygame.time.Clock()
    setup_window()
    screen = pygame.display.set_mode(CONFIG.window_size)
    ship = Ship()

    ship.get_position()
    def reset():
        return Ship("resources/ships/playership.png", (140, 400, 0), "hero")
    quit = False
    while not quit:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT: quit = True
            if event.type == 3:
                if event.key == 27: quit = True  # "Esc" -> quit
                if event.key == 114: ship = reset() # "R" -> reset level
        # Ship movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                ship.move_by(-3, -5)
            elif keys[pygame.K_DOWN]:
                ship.move_by(-3, 5)
            else:
                ship.move_by(-5, 0)

        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_UP]:
                ship.move_by(3, -5)
            elif keys[pygame.K_DOWN]:
                ship.move_by(3, 5)
            else:
                ship.move_by(5, 0)
        elif keys[pygame.K_UP]:
            if keys[pygame.K_LEFT]:
                ship.move_by(-3, -5)
            elif keys[pygame.K_RIGHT]:
                ship.move_by(3, -5)
            else:
                ship.move_by(0, -5)
        elif keys[pygame.K_DOWN]:
            if keys[pygame.K_LEFT]:
                ship.move_by(-3, 5)
            elif keys[pygame.K_RIGHT]:
                ship.move_by(3, 5)
            else:
                ship.move_by(0, 5)
        if keys[pygame.K_SPACE]:
            print("Pew pew pew..")

        ship.move_by(0,0.1)
        screen.fill((0,0,0))
        screen.blit(ship.render(), ship.get_position())
        pygame.display.flip()

        pygame.display.flip()
        clock.tick(60)
    pass
