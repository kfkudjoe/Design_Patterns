"""
The Shape Abstraction Interface.
"""

from abc import ABCMeta, abstractmethod



class IShape(metaclass = ABCMeta):
    """
    The Shape Abstraction Interface.
    """

    @staticmethod
    @abstractmethod
    def draw():
        # The method that will be handled at the shape's imlementer.
        