import os
from tests import test_binaries


class TestBasic(object):
    def test_binaries_exist(self):
        '''
        test to ensure the test binaries even exist
        '''
        for _, binary in test_binaries.iteritems():
            print binary
            assert os.path.exists(binary)
