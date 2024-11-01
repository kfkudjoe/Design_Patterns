"""
Print out the part name and sku
"""

from interface_visitor import IVisitor



class PrintPartsVisitor(IVisitor):
    """
    Print out the part name and sku
    """

    @staticmethod
    def visit(element):
        if hasattr(element, "sku"):
            print(f"{element.name}\t: {element.sku}".expandtabs(6))