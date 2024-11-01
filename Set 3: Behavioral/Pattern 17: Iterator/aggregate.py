"""
A Concrete Aggregate Object.
"""

from interface_aggregate import IAggregate



class Aggregate(IAggregate):
    """
    A Concrete object.
    """

    @staticmethod
    def method():
        print("This method has been invoked")