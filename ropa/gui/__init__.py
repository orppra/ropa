import os
dir_path = os.path.dirname(os.path.realpath(__file__))
UI_PATH = dir_path + '/../ui'

from gui import App  # noqa
