import os
import sys

from PyQt4 import QtGui as qg

from ropa.services import ProjectService, ExportService


class MenuController(object):
    def __init__(self, app):
        self.app = app
        self.bind_menu_button(self.app, 'actionQuit', quit, 'Ctrl+Q')

        self.project_service = ProjectService(app.backend)
        self.init_project_buttons()

        self.exporter = ExportService(app.backend, self.app.chain_list)
        self.init_export_buttons()

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
        filter_text = self.app.filter_input.get_text()
        gadgets = self._get_backend().process_query('instruction',
                                                    filter_text)
        self.app.search_list.set_gadgets(gadgets)

    def save_project(self):
        self.project_service.save_file()

    def quit(self):
        sys.exit(self.app.app.exec_())

    def bind_menu_button(self, window, button_name, func, shortcut_str=None):
        button = window.findChild(qg.QAction, button_name)
        if shortcut_str:
            button.setShortcut(shortcut_str)
        button.triggered.connect(lambda: func())
