"""
A Leaderboard Singleton Class.
"""



class Leaderboard():
    """
    The Leaderboad as a Singleton.
    """

    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        # A class level method
        print("------------Leaderboard------------")
        for key, value in sorted(cls.__table.items()):
            print(f"|\t{key}\t|\t{value}\t|")
        print()
    
    @classmethod
    def add_winner(cls, position, name):
        # A class level method
        cls._table[position] = name