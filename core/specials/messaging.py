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
                


class MessageMaker(object):
    """
    The message base class
    """

    def __init__(self):
        pass

    @staticmethod
    def tick_message(id, keys):
        """ Game tick message passed on every loop """
        message = Message("world", "all", {
            "keys": keys,
            "gamesettings": 1
            })
        return message


class Message(object):
    def __init__(self, sender, receiver, payload):
        """
        :param sender: str Name of the sender
        :param receiver: str Name of the receiver
        :param payload: dict The actual message
        """
        self.timestamp = time.time()
        self.sender = sender
        self.receiver = receiver
        self.payload = payload

    def __repr__(self):
        return f"<Message>\n"\
                f"Sender: {self.sender}\n"\
                f"Receiver: {self.receiver}\n"\
                f"Payload: {self.payload}\n"
