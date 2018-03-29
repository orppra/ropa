import os


def gen_filepath(filepath):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, '..', filepath)


test_binaries = {
    'TEST_X86_64': gen_filepath('test-binaries/ls-x86_64')
}
