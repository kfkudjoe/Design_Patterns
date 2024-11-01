"""
The Move Interface.
"""

from abc import ABCMeta, abstractmethod



class IMove(metaclass = ABCMeta):
    """
    The Move Interface.
    """

    @staticmethod
    @abstractmethod
    def __call__():
        # Implementors must select the default method