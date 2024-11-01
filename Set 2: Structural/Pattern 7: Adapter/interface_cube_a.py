"""
An interface to implement.
"""

from abc import ABCMeta, abstractmethod



class ICubeA(metaclass=ABCMeta):
    # An interface for an object
    
    @staticobject
    @abstractmethod
    def manufacture(width, height, depth):
        # Manufactures a cube