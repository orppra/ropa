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

    def export_block(self, block):
        res = ''
        if len(block.get_comments()) > 0:
            res += '\n'
            for line in block.get_comments().split('\n'):
                res += '# {}\n'.format(line)

        for gadget in block.get_gadgets():
            addr = hex(gadget.get_addr())[:-1]
            if self.search_service.get_addr_len() == 4:
                res += 'p += p32({})'.format(addr)
            else:
                res += 'p += p64({})'.format(addr)

            res += '  # '
            for instruction in gadget.get_instructions():
                res += '{}; '.format(instruction.get_text())

            res += '\n'

        if len(block.get_comments()) > 0:
            res += '\n'

        return res

    def export(self):
        filepath = self.dialog_service.file_dialog('Export')
        lwc = self.app.chain_list

        with open(filepath, 'w') as outfile:
            outfile.write('p = ""\n')

            for block in lwc.get_blocks():
                outfile.write(self.export_block(block))

            outfile.close()

        self.open_exported(filepath)
