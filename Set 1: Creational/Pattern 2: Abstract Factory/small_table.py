"""
A Class of Table.
"""

from interface_table import Table



class SmallTable(ITable):
    """
    The Small Table Concrete Class implements the ITable interface.
    """

    def __init__(self):
        self._height = 60
        self._width = 100
        self._depth = 60

    def get_dimensions(self):
        return {
            "height": self._height,
            "width": self._width,
            "depth": self._depth
        }