"""
The Iterator Pattern.
"""

from abc import ABCMeta, abstractmethod



class IIterator(metaclass = ABCMeta):
    """
    An Iterator Interface.
    """

    @staticmethod
    @abstractmethod
    def has_next():
        # Return Boolean whether at end of collection or not

    @staticmethod
    @abstractmethod
    def next():
        # Return the object in collection