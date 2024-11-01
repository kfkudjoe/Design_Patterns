"""
Bridge Pattern Example.
"""

from circle import Circle
from square import Square
from circle_implementer import CircleImplementer
from square_implementer import SquareImplementer

CIRCLE = Circle(CircleImplementer)
CIRCLE.draw()

SQUARE = Square(SquareImplementer)
SQUARE.draw()