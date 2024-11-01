"""
Memento Pattern example use case.
"""

from game_character import GameCharacter
from care_taker import CareTaker

# Instantiate the objects
GAME_CHARACTER = GameCharacter()
CARE_TAKER = CareTaker(GAME_CHARACTER)

# Start the game
GAME_CHARACTER.register_kill()
GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.add_inventory("sword")
GAME_CHARACTER.register_kill()
GAME_CHARACTER.add_inventory("rifle")
GAME_CHARACTER.move_forward(1)
print(GAME_CHARACTER)

# Save progress
CARE_TAKER.save()

GAME_CHARACTER.register_kill()
GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.progress_to_next_level()
GAME_CHARACTER.register_kill()
GAME_CHARACTER.add_inventory("motorbike")
GAME_CHARACTER.move_forward(10)
GAME_CHARACTER.register_kill()
print(GAME_CHARACTER)

# Save progress
CARE_TAKER.save()

GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.progress_to_next_level()
GAME_CHARACTER.register_kill()
print(GAME_CHARACTER)

# Decide you made a mistake, go back to first save
CARE_TAKER.restore(0)

# Continue
GAME_CHARACTER.register_kill()