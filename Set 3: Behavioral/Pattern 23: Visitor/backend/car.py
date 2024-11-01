"""
A car with parts.
"""

from interface_visitable import IVisitable
from abstract_car_part import AbstractCarPart
from body import Body
from engine import Engine
from wheel import Wheel


class Car(AbstractCarPart, IVisitable):
    """
    A car with parts.
    """

    def __init__(self):
        self._name = name
        self._parts = [
            Body("Utility", "ABC-123-21", 1001),
            Engine("V8 engine", "DEF-456-21", 2555),
            Wheel("FrontLeft", "GHI-789FL-21", 136)
            Wheel("FrontRight", "GHI-789FR-21", 136)
            Wheel("BackLeft", "GHI-789BL-21", 136)
            Wheel("BackRight", "GHI-789BR-21", 136)
        ]

    def accept(self, visitor):
        for parts in self._parts:
            parts.accept(visitor)
        visitor.visit(self)