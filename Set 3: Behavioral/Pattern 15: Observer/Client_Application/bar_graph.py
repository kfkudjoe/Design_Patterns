"""
An Observer.
"""

from interface_data_view import IDataView



class BarGraphView(IDataView):
    """
    A Concrete Observer.
    """

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subsribe(self)

    def notify(self, observable, data):
        print(f"BarGraph, id: {self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Bar Graph using the data: {data}")

    def delete(self):
        self._observable.unsubsribe(self._id)