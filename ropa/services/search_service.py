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

from ropper import RopperService

from ropa.gadget import (
    Gadget,
    Instruction
)


class SearchService:

    def __init__(self, app):
        self.app = app
        self.reset()

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.add_file()

    def get_addr_len(self):
        f = self.service.getFileFor(self.filename)
        return f.arch.addressLength

    def activate(self):
        self.service.loadGadgetsFor()

    def reset(self):
        self.service = self.make_service_instance()
        self.chain = []
        self.favorites = []

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
        filename = self.filename
        if filename is None:
            return 'Error: no file found'
        self.service.addFile(filename)
        return 'Success'

    def close_file(self):
        self.service.removeFile(self.filename)

    #######################################
    # ROPPER SEARCH FUNCTIONS
    #######################################

    def search_semantic(self, filter):
        # ropper2 --file <afile> --semantic "<any constraint>"
        self.service.analyseGadgets(self.service.getFileFor(self.filename))
        gadgets = self.service.semanticSearch(
            search=[filter])

        return gadgets

    def search_instruction(self, filter_text):
        gadgets = self.service.search(
            search=filter_text,
            name=self.filename)

        return gadgets

    def search_jmpreg(self, location, offset):
        gadgets = self.service.searchJmpReg(
            name=self.filename,
            regs=[location, offset])

        return gadgets

    def search_poppopret(self):
        gadgets = self.service.searchPopPopRet(
            name=self.filename)

        return gadgets

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
            for line in gadget[1].lines:
                instructions.append(Instruction(line[1]))

            ret.append(Gadget(gadget[1].address, instructions, query))

        return ret


def test():
    pass


if __name__ == '__main__':
    test()
