"""
An Observer
"""

from interface_data_view import IDataView



class TableView(IDataView):
    """
    The Concrete Observer
    """

    def __init(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, observable, data):
        print(f"TableView, id: {self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Table View using the data: {data}")

    def delete(self):
        self._observable.unsubscribe(self._id)