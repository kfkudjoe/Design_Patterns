"""
The Game API Facade.
"""

from decimal import Decimal
from users import Users
from wallets import Wallets
from game_engine import GameEngine
from reports import Reports



class GameAPI():
    """
    The Game API facade.
    """

    @staticmethod
    def get_balance(user_id: str) -> Decimal:
        # Get a player's balance
        return Wallets.get_balance(user_id)

    @staticmethod
    def game_state() -> dict:
        # Get the current game state
        return GameEngine().get_game_state()

    @staticmethod
    def get_history() -> dict:
        # Get the game history
        return Reports.get_history()

    @staticmethod
    def change_pwd(user_id: str, password: str) -> bool:
        # Change user's password
        return Users.change_pwd(user_id, password)

    @staticmethod
    def submit_entry(user_id: str, entry: Decimal) -> bool:
        # Submit a bet
        return GameEngine().submit_entry(user_id, entry)

    @staticmethod
    def register_user(value: dict[str, str]) -> str:
        # Register a new user and returns the new id
        return Users.register_user(value)