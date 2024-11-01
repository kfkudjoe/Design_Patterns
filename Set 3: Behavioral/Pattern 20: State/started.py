"""
A Concrete State Subclass.
"""

from interface_state import IState



class Started(IState):
    """
    A Concrete State Subclass.
    """

    @staticmethod
    def method():
        # A task of this calss
        print("Task Started")

    __call__ = method