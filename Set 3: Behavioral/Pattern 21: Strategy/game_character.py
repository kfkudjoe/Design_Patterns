"""
Context whose strategy will change.
"""



class GameCharacter():
    """
    This is the context whose strategy will change.
    """

    @staticmethod
    def move(movement_style):
        # The movement algorithm has been decided by the client
        movement_style()