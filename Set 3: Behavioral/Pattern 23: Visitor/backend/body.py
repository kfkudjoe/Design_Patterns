"""
A part of the car.
"""

from interface_visitable import IVisitable
from abstract_car_part import AbstractCarPart


class Body(AbstractCarPart, IVisitable):
    """
    A part of the car.
    """

    def __init__(self, name, sku, price):
        self._name = name
        self._sku = sku
        self._price = price

    def accept(self, visitor):
        visitor.visit(self)