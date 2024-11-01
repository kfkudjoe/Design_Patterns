"""
An interface that custom Visitors should implement.
"""

from abc import ABCMeta, abstractmethod



class IVisitor(metaclass = ABCMeta):
    """
    An interface that custom Visitors should implement.
    """

    @staticmethod
    @abstractmethod
    def visit(element):
        # Visitors visit Elements/Objects within the application