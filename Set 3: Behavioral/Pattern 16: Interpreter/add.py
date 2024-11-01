"""
Add Expression. This is a non-terminal expression.
"""

from abstract_expression import AbstractExpression



class Add(AbstractExpression):
    """
    Non-Terminal expression.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} Add {self.right})"