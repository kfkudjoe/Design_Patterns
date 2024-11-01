"""
The Save/Restore Game functionality.
"""



class CareTaker():
    """
    Guardian. Provides a narrow interface to the mementos.
    """

    def __init__(self, originator):
        self._originator = originator
        self.mementos = []

    def save(self):
        # Store a new Memento of the Character's current state
        print("CareTaker: Game Save")
        
        memento = self._originator.memento
        self.mementos.append(mentor)

    def restore(self, index):
        # Replace the Character's current attributes with the state stored in the saved Memento
        print("CareTaker: Restoring Character's attributes form Memento")

        memento = self._mementos[index]
        self._originator.memento = memento