"""
A dispenser of $20 notes.
"""

from interface_dispenser import IDispenser



class Dispenser20(IDispenser):
    """
    Dispenses $20s if applicable, otherwise continues to the next successor.
    """

    def __init__(self):
        self._succssor = None

    def next_successor(self, successor):
        # Set the next successor
        self._succssor = successor

    def handle(self, amount):
        # Handle the dispensing of notes
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20

            print(f"Dispensig {num} $20 note(s)")

            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)