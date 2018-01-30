import os

from ropa.services import ProjectService


class MenuItemController:
    def __init__(self, app):
        self.app = app
        self.project_service = ProjectService(app)

    def _get_backend(self):
        return self.app.backend

    def start_new_project(self, filepath=None):
        filepath, arch = self.project_service.new_file(filepath)
        self.app.setWindowTitle(self.app.app_name + ' - ' +
                                os.path.basename(str(filepath)))
        self.app._on_open_project()

    def open_project(self, filepath=None):
        self.project_service.open_file(filepath)
        self.app.setWindowTitle(self.app.app_name + ' - ' +
                                self._get_backend().get_filename())
        self.app._on_open_project()

    def save_project(self):
        self.project_service.save_file()
