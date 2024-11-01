"""
Aggregate Interface.
"""

from abc import ABCMeta, abstractmethod



class IAggregate(metaclass = ABCMeta):
    """
    An interface that the aggregates should implement.
    """

    @staticmethod
    @abstractmethod
    def method():
        # A Method to implement