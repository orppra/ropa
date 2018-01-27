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

        for gadget in gadgets:
            cell = gadget['address'] + '\n'
            cell += '\n'.join(gadget['instructions']) + '\n'
            item = qg.QListWidgetItem(qc.QString(cell), self.widget)
            item.setFont(font)
            self.widget.insertItem(self.widget.count(), item)
