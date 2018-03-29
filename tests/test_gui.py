import pytest
import sys
import tests

from ropa.gui import App


@pytest.fixture(scope='module')
def app():
    return App('ropa', sys.argv, tests.test_binaries['TEST_X86_64'])


class TestGui(object):
    @pytest.fixture(autouse=True)
    def setup(self, app):
        yield
        app.reset()
