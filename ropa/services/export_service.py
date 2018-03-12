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

from ropa.services import DialogService


class ExportService:
    def __init__(self, app):
        self.app = app
        self.search_service = app.get_search_service()
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

    def export(self):
        filepath = self.dialog_service.file_dialog('Export')
        lwc = self.app.chain_list

        with open(filepath, 'w') as outfile:
            outfile.write('p = ""\n')

            for block in lwc.get_blocks():
                if len(block.get_comments()) > 0:
                    outfile.write('\n')
                    for line in block.get_comments().split('\n'):
                        outfile.write('# {}\n'.format(line))

                for gadget in block.get_gadgets():
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
