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
from .event import EventMaker
from .messagequeue import MessageQueue



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
    event_maker = EventMaker()
    Q = MessageQueue()
    EM = EventMaker()
    #########

    ####### LEVEL Setup
    # ship = Player()
    level = Level0(Q)
    ship = level.player
    #######

    ### Testing
    font = pygame.font.SysFont('ubuntu', 25)
    ###
    counter = 0
    count = 0
    time1 = time.time()
    def reset():
        return Ship("resources/ships/playership.png", (140, 400, 0), "hero")
    quit = False
    while not quit:
        counter += 1

        for event in pygame.event.get(): # Quit clause
            # print(event)
            if event.type == pygame.QUIT: quit = True
            if event.type == 3:
                if event.key == 27: quit = True  # "Esc" -> quit
                if event.key == 114: ship = reset() # "R" -> reset level
        # Messaging
        Q.send_message(EM.tick_event(1, pygame.key.get_pressed())) 
        Q.dispatch()

        screen.fill((0,0,0))
        x, y = level.render()
        for yy in y:
            screen.blit(x, yy)
        screen.blit(*ship.render())

        # FPS
        if time.time() - time1 >= 1: 
            # print(f"FPS: {counter}")
            time1 = time.time()
            count = counter
            counter = 0 
        screen.blit(font.render(f"{count}",True, (255,255,255)), (560,0))


        pygame.display.flip()
        clock.tick(60)
    pass
