"""
A Shape Implementer Interface.
"""

from abc import ABCMeta, abstractmethod



class IShapeImplementer(metaclass = ABCMeta):
    """
    Shape Implementer.
    """

    @staticmethod
    @abstractmethod
    def draw_implementation():
        # The method that the refined abstractions will implement