""" 
Rendering engine
"""


class Renderer(object):
    """
    Render on screen when a message received
    :param image: pygame.Surface 
    :param position: tup(x, y) coordinates
    """

    def __init__(self, Q, screen):
        """
        :param Q: `MessageManager`
        :param screen: screen to render on
        """
        Q.register(self.on_message)
        self.screen = screen

    def on_message(self, message):
        if message.receiver == "renderer":
            self._render(message.payload)
        pass

    def _render(self, payload):
        """ Return the rendered screen """
        image = payload["image"]
        position = payload["position"]
        self.screen.blit(image, position)
        print(f"<Rendering> {payload}")
        pass

