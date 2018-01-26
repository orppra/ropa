from ropper import RopperService
import json
import struct

# poppopret: pop ???; pop ???; ret
# jmpreg: jmp ???


class Backend:

    def __init__(self, app):
        self.app = app
        self.service = self.make_service_instance()
        self.chain = []
        self.user_blocks = []

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.add_file()

    def get_arch(self):
        return self.arch

    def set_arch(self, arch):
        self.arch = arch

    def activate(self):
        self.service.loadGadgetsFor()

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
        print(gadgets)
        ret = []
        for gadget in gadgets:
            block = {'address': hex(gadget[1].address)[:-1],
                     'instructions': []}
            for line in gadget[1].lines:
                block['instructions'].append(line[1])
        return ret

    def search_instruction(self, filter):
        gadgets = self.service.search(
            search=filter,
            name=self.filename)

        ret = []
        for gadget in gadgets:
            block = {'address': hex(gadget[1].address)[:-1],
                     'instructions': []}
            for line in gadget[1].lines:
                block['instructions'].append(line[1])

            ret.append(block)

        return ret

    def search_jmpreg(self, location, offset):
        gadgets = self.service.searchJmpReg(
            name=self.filename,
            regs=[location, offset])

        return gadgets

    def search_poppopret(self):
        gadgets = self.service.searchPopPopRet(
            name=self.filename)

        ret = []
        for gadget in gadgets[self.filename]:
            block = {'address': hex(gadget.address)[:-1],
                     'instructions': []}
            for line in gadget.lines:
                block['instructions'].append(line[1])

            ret.append(block)

        return ret

    def process_query(self, command, ipt):
        gadgets = None

        if command == 'semantic':
            # semantic search
            gadgets = self.search_semantic(ipt)
            for i in range(len(gadgets)):
                gadgets[i]['info'] = ipt

        if command == 'instruction':
            gadgets = self.search_instruction(ipt)
            for i in range(len(gadgets)):
                gadgets[i]['info'] = ipt

        if command == 'jmp-reg':
            gadgets = self.search_jmpreg(
                ipt.split(',')[0],
                ipt.split(',')[1])
            # not supported right now

        if command == 'pop-pop-ret':
            gadgets = self.search_poppopret()
            for i in range(len(gadgets)):
                gadgets[i]['info'] = 'pop-pop-ret'

        return gadgets

    #######################################
    # EXPORTATION TOOLS
    #######################################

    def num_bits(self, arch):
        if arch.endswith('64'):
            return 64
        return 32

    def export_binary(self, file, chain):
        with open(file, 'w') as outfile:
            for block in chain:
                for gadget in block:
                    if self.num_bits(self.get_arch()) == 32:
                        outfile.write(struct.pack('<I',
                                      int(gadget['address'], 16)))
                    else:
                        outfile.write(struct.pack('<Q',
                                      int(gadget['address'], 16)))
            outfile.close()

    def export_python_struct(self, file, chain):
        with open(file, 'w') as outfile:
            outfile.write('p = ""\n')
            for block in chain:
                for gadget in block:
                    if self.num_bits(self.get_arch()) == 32:
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

    def export_python_pwntools(self, file, chain):
        with open(file, 'w') as outfile:
            outfile.write('p = ""\n')
            for block in chain:
                for gadget in block:
                    if self.num_bits(self.get_arch()) == 32:
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

    #######################################
    # PROJECT TOOLS
    #######################################

    def open_project(self, file):
        save_data = None
        with open(file, 'r') as infile:
            save_data = json.load(infile)

        self.set_filename(save_data['filename'])
        self.set_arch(save_data['arch'])
        self.activate()
        self.chain = save_data['chain']
        self.user_blocks = save_data['user_blocks']

    def save_project(self, file):
        with open(file, 'w') as outfile:
            save_data = {
                'chain': self.chain,
                'user_blocks': self.user_blocks,
                'filename': self.filename,
                'arch': self.arch
            }
            json.dump(save_data, outfile)
            outfile.close()


def test():
    pass


if __name__ == '__main__':
    test()
