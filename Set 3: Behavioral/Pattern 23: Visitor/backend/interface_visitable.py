"""
An interface that concerte objects should implement that allows
the visitor to traverse a hierarchical structure of objects
"""

from abc import ABCMeta, abstractmethod



class IVisitable(metaclass = abstractmethod):
    """
    An interface that concerte objects should implement that allows
    the visitor to traverse a hierarchical structure of objects
    """

    @staticmethod
    @abstractmethod
    def accept(visitor):
        # The Visitor traverses and access each object through its method
