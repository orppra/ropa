import os

from file_dialog_controller import FileDialogController


class MenuItemController:
    def __init__(self, app):
        self.app = app
        self.file_dialog_controller = FileDialogController()

    def _get_backend(self):
        return self.app.backend

    def start_new_project(self, filepath=None):
        filepath, arch = self.file_dialog_controller.new_file_dialog(filepath)
        self.app.setWindowTitle(self.app.app_name + ' - ' +
                                os.path.basename(str(filepath)))
        self._get_backend().set_arch(arch)
        self._get_backend().set_filename(str(filepath))
        self._get_backend().activate()

    def open_project(self, filepath=None):
        if filepath is None:
            filepath = self.file_dialog_controller.open_file_dialog()
        print("Opened " + str(filepath))
        self._get_backend().open_project(str(filepath))
        filename = str(self._get_backend().get_filename())
        self.app.setWindowTitle(self.app.app_name + ' - ' + filename)

    def save_project(self):
        filepath = self.file_dialog_controller.open_file_dialog()
        self._get_backend().save_project(str(filepath))
