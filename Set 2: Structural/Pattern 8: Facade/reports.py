"""
A Singleton Dictionary of Reported Events.
"""

import time



class Reports():
    """
    A Singleton Dictionary of Reported Events.
    """

    _reports: dict[int, tuple[float, str]] = {}
    _row_id = 0


    def __new__(cls):
        return cls

    @classmethod
    def get_history(cls) -> dict:
        # A method to retrive all historic events
        return cls._reports

    @classmethod
    def log_event(cls, event: str) -> bool:
        # A method to add a new event to the record
        cls._reports[cls._row_id] = (time.time(), event)
        cls._row_id = cls._row_id + 1
        return True