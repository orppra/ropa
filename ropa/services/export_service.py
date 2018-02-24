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

import struct
import subprocess
import sys

from ropa.services import DialogService


class ExportService:
    def __init__(self, backend, lwc):
        self.backend = backend
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

    def export_binary(self):
        filepath = self.dialog_service.file_dialog('Export')
        chain = []
        for index in range(self.lwc.count()):
            block = str(self.lwc.get_item(index).text())
            print(str(block))
            block = block.strip().split('\n')
            address = block[0]
            block = block[2:]
            instructions = []
            for b in block:
                instructions.append(block)
            chain.append([{'address': address, 'instructions': instructions}])

        with open(filepath, 'w') as outfile:
            for block in chain:
                for gadget in block:
                    if self.backend.get_arch_len() == 4:
                        outfile.write(struct.pack('<I',
                                      int(gadget['address'], 16)))
                    else:
                        outfile.write(struct.pack('<Q',
                                      int(gadget['address'], 16)))
            outfile.close()

        self.open_exported(filepath)

    def export_python_struct(self):
        filepath = self.dialog_service.file_dialog('Export')
        chain = []
        for index in range(self.lwc.count()):
            block = str(self.lwc.get_item(index).text())
            print(str(block))
            block = block.strip().split('\n')
            address = block[0]
            block = block[2:]
            instructions = []
            for b in block:
                instructions.append(b)
            chain.append([{'address': address, 'instructions': instructions}])

        with open(filepath, 'w') as outfile:
            outfile.write('p = ""\n')
            for block in chain:
                for gadget in block:
                    if self.backend.get_arch_len() == 4:
                        outfile.write('p += struct.pack("<I", {})'
                                      .format(gadget['address']))
                    else:
                        outfile.write('p += struct.pack("<Q", {})'
                                      .format(gadget['address']))

                    outfile.write('  # ')
                    for instruction in gadget['instructions']:
                        outfile.write('{}; '.format(instruction))

                    outfile.write('\n')
            outfile.close()

        self.open_exported(filepath)

    def export_python_pwntools(self):
        filepath = self.dialog_service.file_dialog('Export')
        chain = []
        for index in range(self.lwc.count()):
            block = str(self.lwc.get_item(index).text())
            block = block.strip().split('\n')
            address = block[0]
            block = block[2:]
            instructions = []
            for b in block:
                print(b)
                instructions.append(b)
            print(instructions)
            chain.append([{'address': address, 'instructions': instructions}])

        with open(filepath, 'w') as outfile:
            outfile.write('p = ""\n')
            for block in chain:
                for gadget in block:
                    if self.backend.get_arch_len() == 4:
                        outfile.write('p += p32({})'
                                      .format(gadget['address']))
                    else:
                        outfile.write('p += p64({})'
                                      .format(gadget['address']))

                    outfile.write('  # ')
                    for instruction in gadget['instructions']:
                        outfile.write('{}; '.format(instruction))

                    outfile.write('\n')
            outfile.close()

        self.open_exported(filepath)
