"""
Strategy Pattern Use Case.
"""

from game_character import GameCharacter
from walking import Walking
from running import Running
from crawling import Crawling

# Instantiate the Objects
GAME_CHARACTER = GameCharacter()
GAME_CHARACTER.move(Walking())

# Character sees the enemy
GAME_CHARACTER.move(Running())

# Character finds a small cave to hide in
GAME_CHARACTER.move(Crawling())
