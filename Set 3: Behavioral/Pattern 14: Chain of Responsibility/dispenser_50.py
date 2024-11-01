"""
A Dispenser of $50 Notes.
"""

from interface_dispenser import IDispenser



class Dispenser50(IDispenser):
    """
    Dispenses the $50s if applicable, otehrwise continues to next successor.
    """

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        # Set the next successor
        self._successor = successor

    def handle(self, amount):
        # Handle the dispensing of notes
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50

            print(f"Dispensing {num} $50 notes")

            if remainder != 0:
                self.successor.handle(remainder)

        else:
            self._succssor.handle(amount)