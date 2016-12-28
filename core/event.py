"""
The global event
"""
import time
import pygame
import sys

class EventMaker(object):
    """
    The event base class
    """

    def __init__(self):
        pass

    @staticmethod
    def tick_event(id, keys):
        event = {
                "id": id,
                "timestamp": time.time(),
                "metadata": {
                    "settings": False
                    },
                "gamesettings": {
                    "1": 1,
                    "2": 2,
                    "difficulty": "easy" 
                    },
                "gamestate": {
                    },
                "keys": keys
                }
        return event

    def make_game_event(self):
        pass
