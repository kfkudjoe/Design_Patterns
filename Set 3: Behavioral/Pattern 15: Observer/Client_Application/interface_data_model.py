"""
A Data Model Interface.
"""

from abc import ABCMeta, abstractmethod



class IDataModel(metaclass = Meta):
    """
    A Subject Interface.
    """

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        # The subscribe method

    @staticmethod
    @abstractmethod
    def unsubcribe(observer):
        # The unsubscribe method

    @staticmethod
    @abstractmethod
    def notify(data):
        # The notify method