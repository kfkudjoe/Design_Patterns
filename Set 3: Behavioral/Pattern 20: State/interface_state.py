"""
State Interface Object.
"""

from abc import ABCMeta, abstractmethod



class IState(metaclass = ABCMeta):
    """
    A State Interface.
    """

    @staticmethod
    @abstractmethod
    def __call__():
        # Set the default method