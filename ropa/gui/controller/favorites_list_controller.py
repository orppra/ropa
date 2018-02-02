from list_widget_controller import ListWidgetController
from ropa.ui import HTMLDelegate


class FavoritesListController(ListWidgetController):
    def __init__(self, widget):
        super(FavoritesListController, self).__init__(widget)
        self.widget.setDragEnabled(True)
        self.widget.setAcceptDrops(True)
        self.widget.setDropIndicatorShown(True)
        self.widget.setItemDelegate(
            HTMLDelegate(self.widget))
