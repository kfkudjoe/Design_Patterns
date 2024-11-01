"""
A Game Client.
"""

from interface_game_engine import IGameEngine



class GameClient(IGameEngine):
    """
    A Game Client.
    """
    
    def __init__(self, game_engine):
        self._alias = ""
        self._player = {}
        self._game_engine = game_engine

    def new_game(self):
        # Not implemented in the game client.

    def add_player(self, player):
        self._player = player
        self._game_engine.add_player(player)

    def list_winners():
        # Not implemented in the game client.

    def calculate_winners():
        # Not implemented in the game client.

    def notify_winners():
        # Not implemented in the game client.

    def game_result():
        # Not implemented in the game client.