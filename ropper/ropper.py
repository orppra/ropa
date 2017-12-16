from ropper import RopperService

import json
import struct

# poppopret: pop ???; pop ???; ret
# jmpreg: jmp ???

#######################################
# IO COMMUNICATION
#######################################


def get_filename():
    pass


def get_architecture():
    pass


def get_searchcommand():
    pass


def get_ropchain():
    # returns a list of list of tuples
    pass


#######################################
# ROPPER INIT FUNCTIONS
#######################################


def add_file(service):
    filename = get_filename()
    if filename is None:
        return 'Error: no file found'
    service.addFile(filename)
    return 'Success'


def close_file(service):
    service.removeFile(get_filename())


def get_instance():
    options = {'color': False,
               'badbytes': '',
               'all': False,
               'inst_count': 6,
               'type': 'all',
               'detailed': False}
    rs = RopperService(options)
    return rs


#######################################
# ROPPER SEARCH FUNCTIONS
#######################################


def search():
    pass


def search_instruction():
    pass


def search_jmpreg():
    pass


def search_poppopret():
    pass


search_by = {
    'generalSearch': search,
    'byInstruction': search_instruction,
    # 'byOpcode': search_opcode,
    'findJmpReg': search_jmpreg,
    'findPopPopRet': search_poppopret,
}


#######################################
# EXPORTATION TOOLS
#######################################


def export_binary(file, chain, bit):
    with open(file, 'w') as outfile:
        for block in chain:
            for gadget in chain:
                if bit == 32:
                    outfile.write(struct.pack('<I',
                                  int(gadget['address'], 16)))
                else:
                    outfile.write(struct.pack('<Q',
                                  int(gadget['address'], 16)))
        outfile.close()


def export_python_struct(file, chain, bit):
    with open(file, 'w') as outfile:
        outfile.write('p = ""')
        for block in chain:
            for gadget in chain:
                if bit == 32:
                    outfile.write('p += struct.pack("<I", {})  # {}'
                                  .format(gadget['address'], gadget['bytes']))
                else:
                    outfile.write('p += struct.pack("<Q", {})  # {}'
                                  .format(gadget['address'], gadget['bytes']))
        outfile.close()


def export_python_pwntools(file, chain, bit):
    with open(file, 'w') as outfile:
        outfile.write('p = ""')
        for block in chain:
            for gadget in chain:
                if bit == 32:
                    outfile.write('p += p32({})  # {}'
                                  .format(gadget['address'], gadget['bytes']))
                else:
                    outfile.write('p += p64({})  # {}'
                                  .format(gadget['address'], gadget['bytes']))
        outfile.close()


#######################################
# PROJECT TOOLS
#######################################


def save_project(file, chain, user_blocks):
    with open(file, 'w') as outfile:
        json.dump({'chain': chain, 'user_blocks': user_blocks}, outfile)
        outfile.close()


def test():
    pass


if __name__ == '__main__':
    test()
