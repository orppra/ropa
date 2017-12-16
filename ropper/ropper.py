from ropper import RopperService

import json
import struct

# poppopret: pop ???; pop ???; ret
# jmpreg: jmp ???


class Backend:

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

    def get_filterInput(self):
        pass

    def get_ropchain(self):
        # returns a list of list of tuples
        pass

    #######################################
    # ROPPER INIT FUNCTIONS
    #######################################

    def make_instance(self):
        options = {'color': False,
                   'badbytes': '',
                   'all': False,
                   'inst_count': 6,
                   'type': 'all',
                   'detailed': False}
        rs = RopperService(options)
        return rs

    def add_file(self, service):
        filename = self.get_filename()
        if filename is None:
            return 'Error: no file found'
        service.addFile(filename)
        service
        return 'Success'

    def close_file(self, service):
        service.removeFile(self.get_filename())

    #######################################
    # ROPPER SEARCH FUNCTIONS
    #######################################

    def search(self, service, filter):
        # ropper2 --file <afile> --semantic "<any constraint>"
        gadgets = service.semanticSearch(
            search=filter)
        return gadgets

    def search_instruction(self, service, filter):
        gadgets = service.search(
            search=filter,
            name=self.get_filename())
        return gadgets

    def search_jmpreg(self, service, location, offset):
        gadgets = service.searchJmpReg(
            name=self.get_filename(),
            regs=[location, offset])
        return gadgets

    def search_poppopret(self, service):
        gadgets = service.searchPopPopRet(
            name=self.get_filename())
        return gadgets

    def process_query(self):
        command = self.get_searchcommand()
        service = None
        gadgets = None
        ipt = self.get_filterInput()

        if command == 'search':
            # semantic search
            gadgets = self.search(service, ipt)

        if command == 'instruction':
            gadgets = self.search_instruction(service, ipt)

        if command == 'jmp-reg':
            gadgets = self.search_jmpreg(
                service,
                ipt.split(',')[0],
                ipt.split(',')[1])

        if command == 'pop-pop-ret':
            gadgets = self.search_poppopret(service)

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
