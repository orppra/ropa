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
        for gadget in gadgets:
            cell = '<pre>'
            cell += '<b>%s</b>\n' % gadget['address']
            for instruction in gadget['instructions']:
                cell += '%s\n' % instruction
            cell += '</pre>'
            cell = qc.QString(cell)

            item = qg.QListWidgetItem(cell, self.widget)
            self.widget.insertItem(self.widget.count(), item)
