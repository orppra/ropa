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

import os
import sys

from PyQt4 import QtGui as qg

from ropa.services import (
    ProjectService,
    ExportService,
    RecentFilesService
)


class MenuController(object):
    def __init__(self, app):
        self.app = app
        self.bind_menu_button(self.app, 'actionQuit', quit, 'Ctrl+Q')

        self.project_service = ProjectService(app.backend)
        self.init_project_buttons()

        self.exporter = ExportService(app.backend, self.app.chain_list)
        self.init_export_buttons()

        self.recent_files_service = RecentFilesService()
        self.update_recent_files()

    def _get_backend(self):
        return self.app.backend

    def init_project_buttons(self):
        self.bind_menu_button(self.app, 'actionNew',
                              self.start_new_project, 'Ctrl+N')
        self.bind_menu_button(self.app, 'actionOpen',
                              self.open_project, 'Ctrl+O')
        self.bind_menu_button(self.app, 'actionSave',
                              self.save_project, 'Ctrl+S')

    def init_export_buttons(self):
        self.bind_menu_button(self.app, 'actionBinary',
                              self.exporter.export_binary)
        self.bind_menu_button(self.app, 'actionStruct',
                              self.exporter.export_python_struct)
        self.bind_menu_button(self.app, 'actionPwntools',
                              self.exporter.export_python_pwntools)

    def start_new_project(self, filepath=None):
        filepath = self.project_service.new_file(filepath)
        self.app.setWindowTitle(self.app.app_name + ' - ' +
                                os.path.basename(str(filepath)))
        self._on_open_project()

    def open_project(self, filepath=None):
        self.project_service.open_file(filepath)
        self.app.setWindowTitle(self.app.app_name + ' - ' +
                                self._get_backend().get_filename())
        self._on_open_project()

    def _on_open_project(self):
        self.app.filter_input.clear()
        gadgets = self._get_backend().process_query('instruction', '')
        self.app.search_list.set_gadgets(gadgets)

    def save_project(self):
        filepath = self.project_service.save_file()
        self.recent_files_service.add_file(filepath)
        self.update_recent_files()

    def quit(self):
        sys.exit(self.app.app.exec_())

    def bind_menu_button(self, window, button_name, func, shortcut_str=None):
        button = window.findChild(qg.QAction, button_name)
        if shortcut_str:
            button.setShortcut(shortcut_str)
        button.triggered.connect(lambda: func())

    def update_recent_files(self):
        for i in range(5):
            recent_file_action = self.app.findChild(qg.QAction,
                                                    'itemRecent%d' % i)
            recent_file_action.setVisible(False)

        if len(self.recent_files_service.get_files()) > 0:
            recent_empty_action = self.app.findChild(qg.QAction,
                                                     'itemRecentEmpty')
            recent_empty_action.setVisible(False)

        for i, filepath in enumerate(self.recent_files_service.get_files()):
            recent_file_action = self.app.findChild(qg.QAction,
                                                    'itemRecent%d' % i)
            recent_file_action.setVisible(True)
            recent_file_action.setText(filepath)
            recent_file_action.triggered.disconnect()
            recent_file_action.triggered.connect(self.open_recent(filepath))

    def open_recent(self, filepath):
        def open():
            self.open_project(filepath)
            self.recent_files_service.add_file(filepath)
            self.update_recent_files()

        return open
