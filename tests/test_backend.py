from backend.Backend import Backend

backend = Backend(None)
backend.set_filename('/tmp/a.out')
backend.set_arch('x86')
backend.activate()
res = backend.process_query('instruction', 'mov eax')
print(res)

test_chain = []
for i in res:
    test_chain.append([i])

backend.export_binary('test_binary', test_chain)
backend.export_python_struct('test_binary_struct.py', test_chain)
backend.export_python_pwntools('test_binary_pwntools.py', test_chain)
