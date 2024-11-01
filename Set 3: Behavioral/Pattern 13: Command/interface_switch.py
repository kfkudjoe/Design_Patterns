"""
The Switch Interface, that all commands will implement.
"""

from abc import ABCMeta, abstractmethod



class ISwitch(metaclass = ABCMeta):
    """
    The Switch Interface, that all commands will implement.
    """

    @staticmethod
    @abstractmethod
    def execute():
        # The required execute method that all command objects will use