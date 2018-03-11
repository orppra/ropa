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

from ropper.common.error import NotSupportedError
from ropper import RopperService

from ropa.gadget import (
    Block,
    Gadget,
    Instruction
)


class SearchService:

    def __init__(self, app):
        self.app = app
        self.reset()

    def get_filepath(self):
        return self.filepath

    def set_filepath(self, filepath):
        self.filepath = filepath
        self.add_file()

    def get_addr_len(self):
        f = self.service.getFileFor(self.filepath)
        return f.arch.addressLength

    def activate(self):
        self.service.loadGadgetsFor()

        try:
            self.search_poppopret()
        except NotSupportedError:
            self.app.poppopret_button.set_disabled()
            self.app.poppopret_button.set_tooltip("Only supported on "
                                                  "x86 binaries")

    def reset(self):
        self.service = self.make_service_instance()
        self.chain = []
        self.favourites = []
        self.update_badbytes('0a0d')

    #######################################
    # ROPPER INIT FUNCTIONS
    #######################################

    def update_badbytes(self, badbytes):
        self.service.options.badbytes = badbytes

    def make_service_instance(self):
        options = {'color': False,
                   'badbytes': '0a0d',
                   'all': False,
                   'inst_count': 6,
                   'type': 'all',
                   'detailed': False}
        rs = RopperService(options)
        return rs

    def add_file(self):
        filepath = self.filepath
        if filepath is None:
            return 'Error: no file found'
        self.service.addFile(filepath)
        return 'Success'

    def close_file(self):
        self.service.removeFile(self.filepath)

    #######################################
    # ROPPER SEARCH FUNCTIONS
    #######################################

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

    def search_jmpreg(self, location, offset):
        gadgets = self.service.searchJmpReg(
            name=self.filepath,
            regs=[location, offset])

        return gadgets

    def search_poppopret(self):
        gadgets = self.service.searchPopPopRet(
            name=self.filepath)

        ret = []
        for gadget in gadgets[self.filename]:
            block = {'address': gadget.address,
                     'lines': []}
            for line in gadget.lines:
                block['lines'].append(line[1])

            ret.append(block)

        return ret

    def process_query(self, command, ipt):
        gadgets = None
        query = ""

        if command == 'semantic':
            # semantic search
            gadgets = self.search_semantic(ipt)
            query = ipt

        if command == 'instruction':
            gadgets = self.search_instruction(ipt)
            query = ipt

        if command == 'jmp-reg':
            gadgets = self.search_jmpreg(
                ipt.split(',')[0],
                ipt.split(',')[1])
            # not supported right now
            query = command

        if command == 'pop-pop-ret':
            gadgets = self.search_poppopret()
            query = command

        ret = []
        for gadget in gadgets:
            instructions = []
            for line in gadget['lines']:
                instructions.append(Instruction(line))

            gadget = Gadget(gadget['address'], instructions, query)
            ret.append(Block([gadget]))

        return ret


def test():
    pass


if __name__ == '__main__':
    test()
