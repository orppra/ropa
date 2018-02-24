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


from PyQt4 import QtGui as qg


class HTMLDelegate(qg.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(HTMLDelegate, self).__init__(parent)
        self.doc = qg.QTextDocument(self)

    def paint(self, painter, option, index):
        painter.save()

        options = qg.QStyleOptionViewItemV4(option)
        self.initStyleOption(options, index)

        self.doc.setHtml(options.text)
        options.text = ""

        style = qg.QApplication.style() if options.widget is None \
            else options.widget.style()
        style.drawControl(qg.QStyle.CE_ItemViewItem, options, painter)

        ctx = qg.QAbstractTextDocumentLayout.PaintContext()

        if option.state & qg.QStyle.State_Selected:
            ctx.palette.setColor(qg.QPalette.Text,
                                 option.palette.color(
                                     qg.QPalette.Active,
                                     qg.QPalette.HighlightedText))

        textRect = style.subElementRect(qg.QStyle.SE_ItemViewItemText, options)
        painter.translate(textRect.topLeft())
        self.doc.documentLayout().draw(painter, ctx)

        painter.restore()
