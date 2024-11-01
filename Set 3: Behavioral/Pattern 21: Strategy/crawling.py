"""
A Concrete Strategy Subclass.
"""

from interface_move import IMove



class Crawling(IMove):
    """
    A Concrete Strategy Subclass.
    """

    @staticmethod
    def crawl():
        # A crawl algorithm
        print("I am crawling")

    __call__ = crawl