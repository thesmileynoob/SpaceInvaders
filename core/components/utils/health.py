"""
Health class
"""


class Health(object):
    """
    Base health class to track health of an object
    Health is a combination of Shield and native health.
    The object takes damage in that order.
    """

    def __init__(self, health=100, shield=0, max_health=100, max_shield=100):
        """
        :param health: int The health of an object (default 100)
        :param shield: int The total shield of an object (default 0)
        :param max_health: int The maximum health the object can have (default 100)
        :param max_shield: int The maximum shield the object can have (default 100)
        """
        self.health = health
        self.shield = shield
        self.max_health = max_health
        self.max_shield = max_shield
        self.shield_disabled = False

    def decrease_by(self, damage):
        """
        Decreases the health by delta
        :param damage: int
        :return: None
        """
        if self.shield - damage >= 0:
            # Shield damage
            self.shield -= damage
            return

        else:
            # Shield and health damage
            delta = damage - self.shield
            self.shield = 0
            self.health -= delta
            return

    def increase_health_by(self, boost):
        """
        Increase the health by boost
        :param boost: int
        :return:
        """
        if self.health + boost <= self.max_health:
            self.health += boost
            return
        else:
            self.health = self.max_health
            return

    def increase_shield_by(self, boost):
        """
        Increases the shield by boost
        :param boost: int
        :return: None
        """
        if self.shield_disabled:
            return

        if self.shield + boost <= self.max_shield:
            self.shield += boost
            return
        else:
            self.shield = self.max_shield
            return

    def destroy_shield(self):
        """
        Sets the shield to 0
        :return: None
        """
        self.shield = 0
        return

    def disable_shield(self):
        """
        Disables the shield
        :return:
        """
        self.shield_disabled = True
        return

