"""
Abstract Car Part Object.
"""


class AbstractCarPart():
    """
    Abstract Car Part Object.
    """

    @property
    def name(self):
        # A name for the part
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def sku(self):
        # The Stock Keeping Unit (SKU)
        return self._sku

    @sku.setter
    def sku(self, value):
        self._sku = value

    @property
    def price(self):
        # The price per unit
        return self._price

    @price.setter
    def price(self, value):
        self._price = value