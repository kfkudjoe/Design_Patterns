"""
A Concrete State Subclass.
"""

from interface_state import IState



class Finished(IState):
    """
    A Concrete State Subclass.
    """

    @staticmethod
    def method():
        # A task of this class
        print("Task finished")

    __call__ = method