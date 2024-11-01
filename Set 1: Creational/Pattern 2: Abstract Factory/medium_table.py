"""
A Class of Table.
"""

from interface_table import ITable



class MediumTable(ITable):
    """
    The Medium Table Concrete Class implements the ITable interface.
    """

    def __init__(self):
        self._height = 60
        self._width = 110
        self._depth = 70

    def get_dimensions(self):
        return {
            "height": self._height,
            "width": self._width,
            "depth": self._depth
        }