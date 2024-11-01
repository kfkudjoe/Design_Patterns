"""
The Abstract Factory Interface.
"""

from abc import ABCMeta, abstractmethod


class IFurnitureFactory(metaclass=ABCMeta):
    """
    Abstract Furniture Factory Interace.
    """

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        # The static Abstract Factory Interface method.