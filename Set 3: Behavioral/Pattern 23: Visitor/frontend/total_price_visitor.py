"""
Print out the total cost of the parts in the car.
"""

from interface_visitor import IVisitor



class TotalPriceVisitor(IVisitor):
    """
    Print out the total cost of the parts in the car.
    """
    total_price = 0

    @classmethod
    def visit(cls, element):
        if hasattr(element, "price"):
            cls.total_price += element.price
        return cls.total_price