import ropper
from ropper import RopperService

search_by = {
	'byInstruction': search_instruction,
	'byOpcode': search_opcode,
	'findJmpRet': search_jmpret,
	'findPopPopRet': search_poppopret,
}

def get_filename():
	pass

def get_architecture():
	pass

def add_file(service):
	filename = get_filename()
	if filename == None:
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

def get_jmpreg

def close_file(service):
	service.removeFile(get_filename())





def test():
	pass

if __name__ == '__main__':
	test()
