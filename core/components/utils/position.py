"""
Helper to track position
"""



class Position(object):

    def __init__(self, coordinates):
        """
        Initialize the position
        :param coordinates: tuple(int,int,int) coordinates
        """
        self.x, self.y, self.z = coordinates

    def __repr__(self):
        return f"<Position>\n"\
                f"({self.x}, {self.y}, {self.z})\n"

    def get(self):
        """ 
        Return 2-d the position tuple 
        :return: tuple(int x, int y) 
        """
        return self.x, self.y

    def set_to(self, new_x, new_y, new_z=0):
        """
        Updates the position given x, y, z
        :type new_x: int
        :type new_z: int
        :type new_y: int
        """
        self.x = new_x
        self.y = new_y
        self.z = new_z

    def update_by(self, delta_x, delta_y):
        """
        Updates the position from deltas
        :param delta_x: int
        :param delta_y: int
        :return: None
        """
        self.x += delta_x
        self.y += delta_y

