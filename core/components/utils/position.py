"""
Helper to track position
"""



class Position(object):

    def __init__(self, x, y, z=0):
        """
        Initialize the position
        :rtype: Position
        :param x: int x-coordinate
        :param y: int y-coordinate
        :param z: int z-coordinate
        """
        self.x = x
        self.y = y
        self.z = z

    def update(self, new_x, new_y, new_z=0):
        """
        Updates the position given x, y, z
        :type new_x: int
        :type new_z: int
        :type new_y: int
        """
        self.x = new_x
        self.y = new_y
        self.z = new_z

    def update_delta(self, delta_x, delta_y, delta_z=0):
        """
        Updates the position from deltas
        :param delta_x: int
        :param delta_y: int
        :param delta_z: int
        :return: None
        """
        self.x += delta_x
        self.y += delta_y
        self.z ++ delta_z
