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

from backend import Backend

from ropper.common.error import NotSupportedError
from ropper import RopperService

from ropa.gadget import (
    Gadget,
    Instruction
)


class RopperBackend(Backend):
    def __init__(self):
        super(RopperBackend, self).__init__('RopperBackend')

    def reset(self):
        self.service = self.make_service_instance()

    def set_file(self, filepath):
        self.filepath = filepath
        self.service.addFile(filepath)
        self.activate()

    def update_badbytes(self, badbytes):
        self.service.options.badbytes = badbytes

    def query(self, ipt):
        gadgets = []
        query = ""

        if ipt == 'pop-pop-ret':
            gadgets = self.search_poppopret()
        else:
            gadgets = self.search_instruction(ipt)
            try:
                gadgets.extend(self.search_semantic(ipt))
            except Exception:
                pass

        query = ipt

        ret = []
        for gadget in gadgets:
            instructions = []
            for line in gadget['lines']:
                instructions.append(Instruction(line))

            gadget = Gadget(gadget['address'], instructions, query)
            ret.append(gadget)

        return ret

    def get_addr_len(self):
        f = self.service.getFileFor(self.filepath)
        return f.arch.addressLength

    """
    Initialization
    """

    def activate(self):
        self.service.loadGadgetsFor()

        try:
            self.search_poppopret()
        except NotSupportedError:
            self.app.poppopret_button.set_disabled()
            self.app.poppopret_button.set_tooltip("Only supported on "
                                                  "x86 binaries")

    def make_service_instance(self):
        options = {'color': False,
                   'badbytes': '0a0d',
                   'all': False,
                   'inst_count': 6,
                   'type': 'all',
                   'detailed': False}
        rs = RopperService(options)
        return rs

    """
    Searching
    """

    def search_semantic(self, filter):
        # ropper2 --file <afile> --semantic "<any constraint>"
        self.service.analyseGadgets(self.service.getFileFor(self.filepath))
        gadgets = self.service.semanticSearch(
            search=[filter])

        ret = []
        for gadget in gadgets:
            block = {'address': gadget[1].address,
                     'lines': []}
            for line in gadget[1].lines:
                block['lines'].append(line[1])

            ret.append(block)

        return ret

    def search_instruction(self, filter_text):
        gadgets = self.service.search(
            search=filter_text,
            name=self.filepath)

        ret = []
        for gadget in gadgets:
            block = {'address': gadget[1].address,
                     'lines': []}
            for line in gadget[1].lines:
                block['lines'].append(line[1])

            ret.append(block)

        return ret

    def search_poppopret(self):
        gadgets = self.service.searchPopPopRet(
            name=self.filepath)

        ret = []
        for gadget in gadgets[self.filepath]:
            block = {'address': gadget.address,
                     'lines': []}
            for line in gadget.lines:
                block['lines'].append(line[1])

            ret.append(block)

        return ret
