"""
A Game Engine Class.
"""

import random
from interface_game_engine import IGameEngine

# from scheduler import Scheduler
# from game_client import GameClient1
# from player import Player



class GameEngine(IGameEngine):
    """
    A Concrete Game Engine Class.
    """

    def __init__(self):
        self._players = {}
        self._game_winners = {}
        self._game_result = -1

    def new_game(self):
        for alias in self._players:
            self._players[alias].ntoify(
                f"{alias} -> New Game,, Place Bets"
            )

    def add_player(self):
        self._players[player.alias] = player

    def list_winners(self):
        ret = []

        for key in self._players:
            ret.append([key, self._players[key].last_winnings])
        return ret

    def calculate_winners(self):
        self._game_result = random.randint(0, 12)

        for alias in self.players:
            player = self._players[alias]

            if self._game_result in player.bets:
                player.balance = player.balance + 12
                player.last_winnings = 12
                self._game_winners[alias] = 12

    def notify_winners(self):
        for alias in self._players:
            if alias in self._game_winners:
                self._players[alias].notify(
                    f"{alias} -> You Are The Winner with result "
                    f"{self._game_result}"
                    f"You Won {self._players[alias].last_winnings}}."
                    f"Your Balance = {self._players[alias].balance}"
                )

    def game_result(self):
        return self._game_result