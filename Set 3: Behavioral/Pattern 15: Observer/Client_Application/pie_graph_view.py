"""
An observer.
"""

from interface_data_view import IDataView



class PieGraphView(IDataView):
    """
    The Concrete Observer.
    """

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subsribe(self)

    def notify(self, data):
        print(f"PieGraph, id: {self._id}")

    def draw(self, data):
        print(f"Drawing a Pie Graph using the data: {data}")

    def delete(self):
        self._observable.unsubscribe(self._id)  