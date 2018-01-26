from PyQt4 import QtGui as qg, QtCore as qc

try:
    _fromUtf8 = qc.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ListWidgetController:
    def __init__(self, widget):
        self.widget = widget

    def show_in_gadgets_list(self, gadgets):
        self.widget.clear()
        font = qg.QFont()
        font.setFamily(_fromUtf8('Courier new'))
        # model = qg.QStandardItemModel(gadgets_list)
        for gadget in gadgets:
            cell = gadget['address'] + '\n'
            # cell += '-' * 2 * len(str(gadget['address'])) + '\n'
            cell += '\n'.join(gadget['instructions']) + '\n'
            # item = qg.QStandardItem(cell)
            item = qg.QListWidgetItem(qc.QString(cell), self.widget)
            item.setFont(font)
            # item.setStatusTip(qc.QString(gadget['info']))
            # item.setDragDropMode('InternalMove')
            # model.appendRow(item)
            self.widget.insertItem(self.widget.count(), item)

        # gadgets_list.setModel(model)
        self.widget.setDragEnabled(True)
        self.widget.viewport().setAcceptDrops(True)
        self.widget.setDropIndicatorShown(True)
