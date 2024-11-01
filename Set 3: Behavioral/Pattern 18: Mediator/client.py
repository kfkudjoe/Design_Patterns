"""
Mediator Pattern Use Case Example.
"""

from game_engine import GameEngine
from game_client import GameClient
from player import Player
from scheduler import Scheduler

# The concrete GameEngine process that would run on a dedicated server
GAMEENGINE = GameEngine()

# 3 Hypothetical game clients, all running externally on mobile phones
# calling the GAMEENGINE mediator across a network proxy
MOBILECLIENT1 = GameClient(GAMEENGINE)
PLAYER1 = Player("Sean", 100)

MOBILECLIENT1.add_player(PLAYER)

MOBILECLIENT2 = GameClient(GAMEENGINE)
PLAYER2 = Player("Cosmo", 100)

MOBILECLIENT2.add_player(PLAYER2)

MOBILECLIENT3 = GameClient(GAMEENGINE)
PLAYER3 = Player("Emmy", 300)

MOBILECLIENT3.add_player(PLAYER3)

#  A Scheduler is a separate process that manages game rounds and triggers
# game events at time intervals
SCHEDULER = Scheduler(GAMEENGINE)
SCHEDULER.new_game()

# 3 Hypothetical game clients have received notifications of new game, they
# now place their bets
PLAYER1.place_bets([1, 2, 3])
PLAYER2.place_bets([4, 5, 6, 7])
PLAYER3.place_bets([10, 11])

# The Scheduler closes the round, and triggers the result and winnings notifications
SCHEDULER.calculate_winners()
SCHEDULER.notify_winners()