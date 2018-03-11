# ropa
# Copyright (C) 2017-2018 orppra

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui as qg, QtCore as qc

try:
    _fromUtf8 = qc.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ListWidgetController(object):
    def __init__(self, widget):
        self.widget = widget

    def count(self):
        return self.widget.count()

    def get_item(self, index):
        return self.widget.item(index)

    def create_item(self, block):
        item = qg.QListWidgetItem()
        item.setData(qc.Qt.UserRole, block)
        item.setData(qc.Qt.DisplayRole, block.content())
        item.setData(qc.Qt.ToolTipRole, block.get_query())
        return item

    def retrieve_block(self, item):
        return item.data(qc.Qt.UserRole).toPyObject()

    def set_blocks(self, blocks):
        self.widget.clear()
        for block in blocks:
            item = self.create_item(block)

            if block.is_showing_comments():
                item.setFlags(item.flags() | qc.Qt.ItemIsEditable)

            self.widget.insertItem(self.widget.count(), item)

    def get_blocks(self):
        blocks = []
        for index in range(self.widget.count()):
            item = self.widget.item(index)
            block = self.retrieve_block(item)
            if block.is_showing_comments():
                comments = str(item.data(qc.Qt.DisplayRole).toPyObject())
                block.set_comments(comments)
            blocks.append(block)
        return blocks
