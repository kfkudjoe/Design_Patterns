"""
A Singleton Dictionary of Users.
"""

from decimal import Decimal
from wallets import Wallets
from reports import Reports



class Users():
    """
    A Singleton Dictionary of Users.
    """
    
    _users: dict[str, dict[str, str]] = {}

    
    def __new__(cls):
        return cls

    @classmethod
    def register_user(cls, new_user: dict[str, str]) -> str:
        # Register a user
        if not new_user["user_name"] in cls._users:
            # Generate a really complicated unique user_id.
            # Using the existing user_name as the id for simplicity.
            user_id = new_user["user_name"]
            cls.users[user_id] = new_user
            Reports.log_event(f"New user `{user_id}` created")

            # Create a wallet for the new user
            Wallets().create_wallet(user_id)

            # Give the user a sign up bonus
            Reports.log_event(
                f"Give new user `{user_id}` sign up bonus of 10"
            )
            Wallets().adjust_balance(user_id, Decimal(10))
            
            return user_id
        return ""

    @classmethod
    def edit_user(cls, user_id: str, user: dict):
        # Do nothing
        print(user_id)
        print(user)
        return False

    @classmethod
    def change_pwd(cls, user_id: str, password: str):
        # Do nothing
        print(user_id)
        print(password)
        return False