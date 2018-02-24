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


class DialogService:
    def file_dialog(self, title):
        dialog = qg.QFileDialog()
        dialog.setWindowTitle(title)
        dialog.setFileMode(qg.QFileDialog.AnyFile)
        filenames = qc.QStringList()
        if dialog.exec_():
            filenames = dialog.selectedFiles()
            return filenames[0]
        raise Exception('Failed to open dialog')
