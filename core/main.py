"""
The main loop of the game 
"""
import pdb
import sys
import time
import pygame

from .CONFIG import CONFIG
from .components.levels.level0 import Level0
from .components.ships.player import Player



def setup_window():
    pygame.init()
    pygame.display.set_caption(CONFIG.window_title)

def render(level):
    """ Render all items """
    level.render()


def start_game():
    """
    Initialize pygame, check saved files, and run the main loop
    """
    screen = pygame.display.set_mode(CONFIG.window_size)
    #########  GLOBAL SETUP
    clock = pygame.time.Clock()
    setup_window()
    #########

    ####### LEVEL Setup
    # ship = Player()
    level = Level0()
    ship = level.player
    #######

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
            ship.fire1()

        ship.move_by(0,0.1)
        screen.fill((0,0,0))
        x, y = level.render()
        for yy in y:
            screen.blit(x, yy)
        screen.blit(*ship.render())
        pygame.display.flip()
        clock.tick(60)
    pass
