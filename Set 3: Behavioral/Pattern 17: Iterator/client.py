"""
The Iterator Use Case.
"""

from iterable import Iterable

# AGGREGATES is a python list that is already iterable by default
AGGREGATES = [Aggregate(), Aggregate(), Aggregate(), Aggregate()]

# But we can create our own iterator atop it
ITERABLE = Iterable(AGGREGATES)

while ITERABLE.has_next():
    ITERABLE.next().method()