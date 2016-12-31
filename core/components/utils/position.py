"""
Helper to track position
"""



class Position(object):

    def __init__(self, coordinates):
        """
        Initialize the position
        :param coordinates: tuple(int,int) coordinates
        """
        self.x, self.y = coordinates

    def __repr__(self):
        return f"<Position>\n"\
                f"({self.x}, {self.y}"

    def get(self):
        """ 
        Return 2-d the position tuple 
        :return: tuple(int x, int y) 
        """
        return self.x, self.y

    def set_to(self, coordinates):
        """
        Updates the position given x, y, z
        :type new_x: int
        :type new_z: int
        """
        self.x, self.y = coordinates

    def update_by(self, deltas):
        """
        Updates the position from deltas
        :param delta_x: int
        :param delta_y: int
        :return: None
        """
        dx, dy = deltas
        self.x += dx
        self.y += dy

