"""
Concrete Iterator Object.
"""

from interface_iterator import IIterator



class Iterable(IIterator):
    """
    The Concrete Iterator (Iterable).
    """

    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("AtEndofIteratorException", "At End of Iterator")


    def has_next(self):
        return self.index < len(self.aggregates)