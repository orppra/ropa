import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from backend.Backend import Backend  # noqa

backend = Backend(None)
# backend.set_filename('../test-binaries/ls-x86')
backend.set_filename('/tmp/a.out')
# backend.set_arch('x86')
backend.activate()

# print('\n--- instruction: mov eax ---\n')
res = backend.process_query('instruction', 'pop ???; pop ???; ret')
# print(res)

# res = backend.process_query('jmp-reg', '')
# print(res)

# print('\n--- pop pop ret ---\n')
# res = backend.process_query('pop-pop-ret', '')
# print(res)

test_chain = []
for i in res:
    test_chain.append([i])

backend.export_binary('test_binary', test_chain)
backend.export_python_struct('test_struct.py', test_chain)
backend.export_python_pwntools('test_pwntools.py', test_chain)
