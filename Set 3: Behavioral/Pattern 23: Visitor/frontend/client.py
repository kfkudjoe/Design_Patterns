"""
The Visitor Pattern Use Case.
"""

from ..backend.car import Car
from print_parts_visitor import PrintPartsVisitor
from total_price_visitor import TotalPriceVisitor

# Instantiate the object
CAR = Car("DeLorean")

# Print out the part name and sku using the PrintPartsVisitor
CAR.accept(PrintPartsVisitor())

# Calculate the total price of the parts using the TotalPriceVisitor
TOTAL_PRICE_VISITOR = TotalPriceVisitor()

CAR.accept(TOTAL_PRICE_VISITOR)
print(f"Total Price = {TOTAL_PRICE_VISITOR.total_price}")