"""
A Memento to store character attributes.
"""



class Memento():
    """
    A container of character attributes.
    """

    def __init__(self, score, inventory, level, location):
        self._score = score
        self._inventory = inventory
        self._level = level
        self._location = location
