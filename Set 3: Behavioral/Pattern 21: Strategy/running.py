"""
A Concrete Strategy Subclass.
"""

from interface_move import IMove



class Running(IMove):
    """
    A Concrete Strategy Subclass.
    """

    @staticmethod
    def run():
        # A run algorithm
        print("I am running")

    __call__ = run