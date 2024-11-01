"""
The Game Character whose state changes.
"""

from memento import Memento


class GameCharacter():
    """
    A Game Character whose state changes.
    """

    def __init__(self):
        self._score = 0
        self._inventory = set()
        self._level = 0
        self._location = {"x": 0, "y": 0, "z": 0}
        # self._memento = Memento()

    @property
    def score(self):
        # A `getter` for the object's score
        return self._score

    def register_kill(self):
        # The character kills its enemies as it progresses
        self._score += 100

    def add_inventory(self, item):
        # The character finds objects in the game
        self._inventory.add(item)

    def progress_to_next_level(self):
        # The character progresses to the next level
        self._level += 1

    def move_forward(self):
        # The chareacter moves around the environment
        self._location["z"] += amount

    def __str__(self):
        return (
            f"Score: {self._score}, "
            f"Level: {self._level}, "
            f"Location: {self._location},\n"
            f"Inventory: {self._inventory}\n"
        )

    @property
    def memento(self):
        # A Getter for the character's attributes as a Memento
        return Memento(
            self._score,
            self._inventory.copy(),
            self._low_level,
            self._location.copy()
        )

    @mement.setter
    def memento(self, memento):
        self.score = memento.score
        self._inventory = memento.inventory
        self._level = memento.level
        self._location = memento.location