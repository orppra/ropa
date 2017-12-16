from backend.Backend import Backend

arch = 'x86'

chain = [[{'address': '0x45464748', 'instruction': 'testing'}],
		 [{'address': '0x45464748', 'instruction': 'testing'}, {'address': '0x45464748', 'instruction': 'testing'}]]

backend = Backend(None)
backend.export_binary('test_out', chain, arch)
backend.export_python_struct('test_out_struct.py', chain, arch)
backend.export_python_pwntools('test_out_pwntools.py', chain, arch)
