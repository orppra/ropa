from list_widget_controller import ListWidgetController
from ropa.ui import HTMLDelegate
from PyQt4 import QtGui as qg


class SearchListController(ListWidgetController):
    def __init__(self, widget):
        super(SearchListController, self).__init__(widget)
        self.widget.setDragEnabled(True)
        self.widget.setAcceptDrops(False)
        self.widget.setDropIndicatorShown(False)
        self.widget.setVerticalScrollMode(
            qg.QAbstractItemView.ScrollPerPixel)
        self.widget.setItemDelegate(
            HTMLDelegate(self.widget))
