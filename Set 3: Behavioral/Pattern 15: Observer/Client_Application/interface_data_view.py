"""
The Data View Interface.
"""

from abc import ABCMeta, abstractmethod



class IDataView(meta = ABCMeta):
    """
    The Data View Interface.
    """

    @staticmethod
    @abstractmethod
    def notify(data):
        # Receive notifications

    @staticmethod
    @abstractmethod
    def draw():
        # Draw the view

    @staticmethod
    @abstractmethod
    def delete():
        # A delete method to remove observer specific resources