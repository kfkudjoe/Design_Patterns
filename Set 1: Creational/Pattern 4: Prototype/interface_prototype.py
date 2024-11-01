"""
Prototype Concept Sample Code.
"""

from abc import ABCMeta, abstractmethod



class IProtoType(metaclass = ABCMeta):
    """
    Interface with cloe method.
    """

    @staticmethod
    @abstractmethod
    def clone(mode):
        # The clone, deep or shallow
        # It is up to the programmer how to implement the details in their concrete class