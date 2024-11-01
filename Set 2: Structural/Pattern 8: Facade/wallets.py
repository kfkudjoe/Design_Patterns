"""
A Singleton Dictionary of User Modules.
"""

from decimal import Decimal
from reports import Reports



class Wallets():
    """
    A Singleton Dictionary of User Wallets.
    """

    _wallets: dict[str, Decimal] = {}

    def __new__(cls):
        return cls

    @classmethod
    def create_wallet(cls, user_id: str) -> bool:
        # A method to initialize a user's wallet.
        if not user_id in cls._wallets:
            cls._wallets[user_id] = Decimal('0')
            Reports.log_event(
                f"Wallet for `{user_id}` created and set to 0"
            )
            return True
        return False

    @classmethod
    def get_balance(cls, user_id: str) -> bool:
        # A method to check a user's balance.
        Reports.log_event(
            f"Balance check for `{user_id}` = {cls._wallets[user_id]}"
        )
        return cls._wallets[user_id]

    @classmethod
    def adjust_balance(cls, user_id: str, amount: Decimal) -> Decimal:
        # A method to adjust a user balance up or down.
        cls._wallets[user_id] = cls._wallets[user_id] + Decimal(amount)
        Reports.log_event(
            f"Balance adjustment for `{user_id}`. "
            f"New balance = {cls._wallets[user_id]}"
        )
        return cls._wallets[user_id]