"""
A Concrete Strategy Subclass.
"""

from interface_move import IMove



class Walking(IMove):
    """
    A Concrete Strategy Subclass.
    """

    @staticmethod
    def walk():
        # A walk algorithm
        print("I am Walking")

    __call__ = walk