"""
A Concrete State Subclass.
"""

from interface_state import IState



class Running(IState):
    """
    A Concrete State Subclass.
    """

    @staticmethod
    def method():
        # A task of this class
        print("Task Running")

    __call__ = method