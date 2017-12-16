from ropper import RopperService

import json
import struct

# poppopret: pop ???; pop ???; ret
# jmpreg: jmp ???


class Backend:

    def __init__(self, app):
        self.app = app
        self.filename = None
        self.service = self.make_service_instance()

    #######################################
    # IO COMMUNICATION
    #######################################

    def set_filename(self, filename):
        self.filename = filename
        pass

    def set_arch(self, arch):
        self.arch = arch
        pass

    def get_searchcommand(self):
        pass

    def set_filterInput(self):
        return self.app.filterInput.text()

    def get_ropchain(self):
        # returns a list of list of tuples
        pass

    def update_ropchain(self):
        pass

    def update_savedblocks(self):
        pass

    #######################################
    # ROPPER INIT FUNCTIONS
    #######################################

    def make_service_instance(self):
        options = {'color': False,
                   'badbytes': '',
                   'all': False,
                   'inst_count': 6,
                   'type': 'all',
                   'detailed': False}
        rs = RopperService(options)
        return rs

    def add_file(self):
        filename = self.get_filename()
        if filename is None:
            return 'Error: no file found'
        self.service.addFile(filename)
        return 'Success'

    def close_file(self):
        self.service.removeFile(self.get_filename())

    #######################################
    # ROPPER SEARCH FUNCTIONS
    #######################################

    def search(self, filter):
        # ropper2 --file <afile> --semantic "<any constraint>"
        gadgets = self.service.semanticSearch(
            search=filter)
        return gadgets

    def search_instruction(self, filter):
        gadgets = self.service.search(
            search=filter,
            name=self.get_filename())
        return gadgets

    def search_jmpreg(self, location, offset):
        gadgets = self.service.searchJmpReg(
            name=self.get_filename(),
            regs=[location, offset])
        return gadgets

    def search_poppopret(self):
        gadgets = self.service.searchPopPopRet(
            name=self.get_filename())
        return gadgets

    def process_query(self, command, ipt):
        gadgets = None

        if command == 'search':
            # semantic search
            gadgets = self.search(ipt)

        if command == 'instruction':
            gadgets = self.search_instruction(ipt)

        if command == 'jmp-reg':
            gadgets = self.search_jmpreg(
                ipt.split(',')[0],
                ipt.split(',')[1])

        if command == 'pop-pop-ret':
            gadgets = self.search_poppopret()

        # process gadgets
        print(gadgets)
        ret = []
        for elem in gadgets:
            print(elem)
        return ret

    #######################################
    # EXPORTATION TOOLS
    #######################################

    def num_bits(self, arch):
        if arch.endswith('64'):
            return 64
        return 32

    def export_binary(self, file, chain, arch):
        with open(file, 'w') as outfile:
            for block in chain:
                for gadget in chain:
                    if self.num_bits(arch) == 32:
                        outfile.write(struct.pack('<I',
                                      int(gadget['address'], 16)))
                    else:
                        outfile.write(struct.pack('<Q',
                                      int(gadget['address'], 16)))
            outfile.close()

    def export_python_struct(self, file, chain, arch):
        with open(file, 'w') as outfile:
            outfile.write('p = ""')
            for block in chain:
                for gadget in chain:
                    if self.num_bits(arch) == 32:
                        outfile.write(
                            'p += struct.pack("<I", {})  # {}'
                            .format(gadget['address'], gadget['bytes']))
                    else:
                        outfile.write(
                            'p += struct.pack("<Q", {})  # {}'
                            .format(gadget['address'], gadget['bytes']))
            outfile.close()

    def export_python_pwntools(self, file, chain, arch):
        with open(file, 'w') as outfile:
            outfile.write('p = ""')
            for block in chain:
                for gadget in chain:
                    if self.num_bits(arch) == 32:
                        outfile.write(
                            'p += p32({})  # {}'
                            .format(gadget['address'], gadget['bytes']))
                    else:
                        outfile.write(
                            'p += p64({})  # {}'
                            .format(gadget['address'], gadget['bytes']))
            outfile.close()

    #######################################
    # PROJECT TOOLS
    #######################################

    def save_project(self, file, chain, user_blocks):
        with open(file, 'w') as outfile:
            json.dump({'chain': chain, 'user_blocks': user_blocks}, outfile)
            outfile.close()


def test():
    pass


if __name__ == '__main__':
    test()
