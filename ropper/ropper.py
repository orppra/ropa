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


def get_filterInput():
    pass


def get_ropchain():
    # returns a list of list of tuples
    pass


#######################################
# ROPPER INIT FUNCTIONS
#######################################


def make_instance():
    options = {'color': False,
               'badbytes': '',
               'all': False,
               'inst_count': 6,
               'type': 'all',
               'detailed': False}
    rs = RopperService(options)
    return rs


def add_file(service):
    filename = get_filename()
    if filename is None:
        return 'Error: no file found'
    service.addFile(filename)
    return 'Success'


def close_file(service):
    service.removeFile(get_filename())


#######################################
# ROPPER SEARCH FUNCTIONS
#######################################


def search(service, filter):
    # ropper2 --file <afile> --semantic "<any constraint>"
    pass


def search_instruction(service, filter):
    gadgets = service.search(
        search=filter,
        name=get_filename())
    return gadgets


def search_jmpreg(service, location, offset):
    gadgets = service.searchJmpReg(
        name=get_filename(),
        regs=[location, offset])
    return gadgets


def search_poppopret(service):
    gadgets = service.searchPopPopRet(
        name=get_filename())
    return gadgets


def process_query():
    command = get_searchcommand()
    service = None
    gadgets = None
    ipt = get_filterInput()

    if command == 'search':
        # semantic search
        pass
    if command == 'instruction':
        gadgets = search_instruction(service, ipt)
    if command == 'jmp-reg':
        gadgets = search_jmpreg(
            service,
            ipt.split(',')[0],
            ipt.split(',')[1])
    if command == 'pop-pop-ret':
        gadgets = search_poppopret(service)

    # process gadgets
    print(gadgets)
    ret = []
    for elem in gadgets:
        print(elem)
    return ret


#######################################
# EXPORTATION TOOLS
#######################################


def export_binary(file, chain, bit):
    with open(file, 'w') as outfile:
        for block in chain:
            for gadget in chain:
                if bit == 32:
                    outfile.write(struct.pack('<I', int(gadget['address'], 16)))
                else:
                    outfile.write(struct.pack('<Q', int(gadget['address'], 16)))
        outfile.close()


def export_python_struct(file, chain, bit):
    with open(file, 'w') as outfile:
        outfile.write('p = ""')
        for block in chain:
            for gadget in chain:
                if bit == 32:
                    outfile.write('p += struct.pack("<I", {})  # {}'.format(gadget['address'], gadget['bytes']))
                else:
                    outfile.write('p += struct.pack("<Q", {})  # {}'.format(gadget['address'], gadget['bytes']))
        outfile.close()


def export_python_pwntools(file, chain, bit):
    with open(file, 'w') as outfile:
        outfile.write('p = ""')
        for block in chain:
            for gadget in chain:
                if bit == 32:
                    outfile.write('p += p32({})  # {}'.format(gadget['address'], gadget['bytes']))
                else:
                    outfile.write('p += p64({})  # {}'.format(gadget['address'], gadget['bytes']))
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
