# ropa
# Copyright (C) 2017-2018 orppra

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys

from PyQt4 import QtGui as qg, QtCore as qc, uic

from ropa.backend import Backend
from ropa.gui import UI_PATH

from controller import (
    SearchListController,
    ChainListController,
    FavoritesListController,
    InstructionsButtonController as IBController,
    SemanticsButtonController as SBController,
    PoppopretButtonController as PBController,
    FilterInputController,
    BadbytesInputController,
    MenuController
)

try:
    _fromUtf8 = qc.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

Ui_MainWindow, QtBaseClass = uic.loadUiType(UI_PATH + '/scene.ui')


class App(qg.QMainWindow, Ui_MainWindow):
    def __init__(self, app_name, args, filepath=None):
        self.app_name = app_name

        self.backend = Backend(self)

        self.app = qg.QApplication(args)
        qg.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self._init_list_widgets()
        self._init_text_inputs()
        self._init_buttons()
        self._init_menu_buttons()

        try:
            self.menu_controller.start_new_project(filepath)
        except ValueError:
            self.menu_controller.open_project(filepath)

    def quit(self):
        sys.exit(self.app.exec_())

    def get_backend(self):
        return self.backend

    def get_app_name(self):
        return self.app_name

    def _init_list_widgets(self):
        search_list_widget = self.findChild(qg.QListWidget,
                                            'searchList')
        self.search_list = SearchListController(search_list_widget)

        chain_list_widget = self.findChild(qg.QListWidget, 'chainList')
        self.chain_list = ChainListController(chain_list_widget)

        favorites_list_widget = self.findChild(qg.QListWidget,
                                               'favoritesList')
        self.favorites_list = FavoritesListController(favorites_list_widget)

    def _init_buttons(self):
        instructions_button_widget = self.findChild(qg.QPushButton,
                                                    'searchInstructions')
        self.instructions_button = IBController(instructions_button_widget,
                                                self.backend,
                                                self.filter_input,
                                                self.search_list)
        poppopret_button_widget = self.findChild(qg.QPushButton,
                                                 'searchPopPopRet')
        self.poppopret_button = PBController(poppopret_button_widget,
                                             self.backend,
                                             self.search_list)
        semantics_button_widget = self.findChild(qg.QPushButton,
                                                 'searchSemantics')
        self.semantics_button = SBController(semantics_button_widget,
                                             self.backend,
                                             self.filter_input,
                                             self.search_list)

    def _init_text_inputs(self):
        filter_input = self.findChild(qg.QLineEdit, 'searchBar')

        badbytes_input = self.findChild(qg.QLineEdit, 'badbytesInput')

        self.filter_input = FilterInputController(filter_input,
                                                  self.backend,
                                                  self.search_list)
        self.badbytes_input = BadbytesInputController(badbytes_input,
                                                      self.backend,
                                                      self.search_list,
                                                      self.filter_input)

    def _init_menu_buttons(self):
        self.menu_controller = MenuController(self)
