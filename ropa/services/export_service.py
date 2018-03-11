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

import subprocess
import sys

from PyQt4 import QtCore as qc

from ropa.services import DialogService


class ExportService:
    def __init__(self, app, lwc):
        self.app = app
        self.search_service = app.get_search_service()
        self.lwc = lwc
        self.dialog_service = DialogService()

    def open_exported(self, filepath):
        if sys.platform.startswith('linux'):
            subprocess.call(["xdg-open", filepath])

        # Let's ignore this for now,
        # I don't even know how to set python qt up on windows
        #
        # elif sys.platform.startswith('win'):
        #     subprocess.call([filepath])

        elif sys.platform.startswith('darwin'):  # mac
            subprocess.call(["open", filepath])

    def pre_export(self):
        filepath = self.dialog_service.file_dialog('Export')
        gadgets = []
        for index in range(self.lwc.count()):
            block = self.lwc.get_item(index).data(qc.Qt.UserRole).toPyObject()
            for gadget in block.get_gadgets():
                gadgets.append(gadget)

        return filepath, gadgets

    def export_python_struct(self):
        filepath, gadgets = self.pre_export()

        with open(filepath, 'w') as outfile:
            outfile.write('p = ""\n')
            for gadget in gadgets:
                if self.search_service.get_addr_len() == 4:
                    outfile.write('p += struct.pack("<I", {})'
                                  .format(hex(gadget.get_addr())[:-1]))
                else:
                    outfile.write('p += struct.pack("<Q", {})'
                                  .format(hex(gadget.get_addr())[:-1]))

                outfile.write('  # ')
                for instruction in gadget.get_instructions():
                    outfile.write('{}; '.format(instruction.get_text()))

                outfile.write('\n')
            outfile.close()

        self.open_exported(filepath)

    def export_python_pwntools(self):
        filepath, gadgets = self.pre_export()

        with open(filepath, 'w') as outfile:
            outfile.write('p = ""\n')
            for gadget in gadgets:
                if self.search_service.get_addr_len() == 4:
                    outfile.write('p += p32({})'
                                  .format(hex(gadget.get_addr())[:-1]))
                else:
                    outfile.write('p += p64({})'
                                  .format(hex(gadget.get_addr())[:-1]))

                outfile.write('  # ')
                for instruction in gadget.get_instructions():
                    outfile.write('{}; '.format(instruction.get_text()))

                outfile.write('\n')
            outfile.close()

        self.open_exported(filepath)
