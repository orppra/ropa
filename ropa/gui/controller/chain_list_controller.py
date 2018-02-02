from PyQt4 import QtCore as qc

from list_widget_controller import ListWidgetController
from ropa.ui import HTMLDelegate


class ChainListController(ListWidgetController):
    def __init__(self, widget):
        super(ChainListController, self).__init__(widget)
        self.widget.setDragEnabled(True)
        self.widget.setAcceptDrops(True)
        self.widget.setDropIndicatorShown(True)
        self.widget.setItemDelegate(
            HTMLDelegate(self.widget))

        self.control = False
        self.widget.keyPressEvent = self.key_press_event
        self.widget.keyReleaseEvent = self.key_release_event

    def key_press_event(self, e):
        if e.key() == qc.Qt.Key_Control:
            self.control = True
        if e.key() == qc.Qt.Key_Up:
            index = self.widget.currentRow()
            if index == 0:
                return
            if self.control:
                item = self.widget.takeItem(index)
                self.widget.insertItem(index - 1, item)
            self.widget.setCurrentRow(index - 1)
        if e.key() == qc.Qt.Key_Down:
            index = self.widget.currentRow()
            if index == self.widget.count() - 1:
                return
            if self.control:
                item = self.widget.takeItem(index)
                self.widget.insertItem(index + 1, item)
            self.widget.setCurrentRow(index + 1)
        if e.key() == qc.Qt.Key_Delete:
            # delete
            self.widget.takeItem(self.widget.selectedIndexes()[0].row())

    def key_release_event(self, e):
        if e.key() == qc.Qt.Key_Control:
            self.control = False
