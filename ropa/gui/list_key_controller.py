from PyQt4 import QtCore as qc


class ListKeyController:
    def __init__(self, list_widget):
        self.control = False
        self.list_widget = list_widget

    def key_press_event(self, e):
        if e.key() == qc.Qt.Key_Control:
            self.control = True
        if e.key() == qc.Qt.Key_Up:
            index = self.list_widget.currentRow()
            if index == 0:
                return
            if self.control:
                item = self.list_widget.takeItem(index)
                self.list_widget.insertItem(index - 1, item)
            self.list_widget.setCurrentRow(index - 1)
        if e.key() == qc.Qt.Key_Down:
            index = self.list_widget.currentRow()
            if index == self.list_widget.count() - 1:
                return
            if self.control:
                item = self.list_widget.takeItem(index)
                self.list_widget.insertItem(index + 1, item)
            self.list_widget.setCurrentRow(index + 1)
        if e.key() == qc.Qt.Key_Delete:
            # delete
            self.list_widget.takeItem(self.list_widget
                                      .selectedIndexes()[0].row())

    def key_release_event(self, e):
        if e.key() == qc.Qt.Key_Control:
            self.control = False
