"""
Context Class.
"""



class Context():
    """
    This is the object whose behavior will change.
    """

    def __init__(self):
        self.state_handles = [
            Started(),
            Running(),
            Finished()
        ]
        self._handle = iter(self.state_handles)

    def request(self):
        # Each time the request is called, a new class will handle it
        try:
            self._handle._next__()()
        except StopIteration:
            # resetting so it loops
            self._handle = iter(self.state_handles)