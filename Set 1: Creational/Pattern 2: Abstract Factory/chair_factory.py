"""
The Factory Class.
"""

from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair



class ChairFactory:
    """
    The Factory Class.
    """

    @staticmethod
    def get_chair(chair):
        # A static method to get a chair
        try:
            if chair == "BigChair":
                return BigChair()
            if chair == "MediumChair":
                return MediumChair()
            if chair == "SmallChair":
                return SmallChair()
            raise Exception("Chair not Found")
        except Exception as _e:
            print(_e)
        return None