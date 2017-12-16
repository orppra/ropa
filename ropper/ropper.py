import ropper
from ropper import RopperService

search_by = {
    'generalSearch': search,
    'byInstruction': search_instruction,
    #'byOpcode': search_opcode,
    'findJmpReg': search_jmpreg,
    'findPopPopRet': search_poppopret,
}

# poppopret: pop ???; pop ???; ret
# jmpreg: jmp ???


def get_filename():
    pass


def get_architecture():
    pass


def get_searchcommand():
    pass


def get_ropchain():
    # returns a list of list of tuples
    pass


def add_file(service):
    filename = get_filename()
    if filename is None:
        return 'Error: no file found'
    service.addFile(filename)
    return 'Success'


def get_instance():
    options = {'color': False,
               'badbytes': '',
               'all': False,
               'inst_count': 6,
               'type': 'all',
               'detailed': False}
    rs = RopperService(options)
    return rs


def search():
    pass


def search_instruction():
    pass


def search_jmpreg():
    pass


def search_poppopret():
    pass


def close_file(service):
    service.removeFile(get_filename())


def test():
    pass


if __name__ == '__main__':
    test()
