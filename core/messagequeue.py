"""
The MessageQueue class
"""

import time
import pygame
import sys

class MessageQueue(object):
    """
    MessageQueue class
    """

    def __init__(self):
        self.observers = []  # Hold all the refs
        self.queue = [] # The message queue
    
    def register(self, observer):
        """
        Register all observers/listeners
        :param observer: any object with an on_message method
        """
        self.observers.append(observer)
    
    def send_message(self, message):
        """
        Add a message to the queue
        """
        self.queue.append(message)

    def dispatch(self, category=None):
        """
        Dispatch the messages to refs
        """
        if not category:
            for message in self.queue:
                for observer in self.observers:
                    observer(message)
            self.queue = [] # Empty the queue
                

