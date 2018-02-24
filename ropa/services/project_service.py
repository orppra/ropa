import json

from ropa.services import DialogService


class ProjectService:
    def __init__(self, backend):
        self.backend = backend
        self.dialog_service = DialogService()

    def new_file(self, filepath=None):
        if filepath is None:
            filepath = self.dialog_service.file_dialog('New Project')

        self.backend.set_filename(str(filepath))
        self.backend.activate()

        print(repr(filepath))
        return filepath

    def open_file(self, filepath=None):
        if filepath is None:
            filepath = self.dialog_service.file_dialog('Open Project')

        save_data = None
        with open(filepath, 'r') as infile:
            save_data = json.load(infile)

        self.backend.set_filename(save_data['filename'])
        self.backend.activate()

        # doesn't work for now, need to settle on refactoring other stuff first
        # self.chain = save_data['chain']
        # self.favorites = save_data['favorites']

    def save_file(self):
        filepath = self.dialog_service.file_dialog('Save Project')
        with open(filepath, 'w') as outfile:
            save_data = {
                # doesn't work now, settle on refactoring first
                # 'chain': self.chain,
                # 'favorites': self.favorites,
                'filename': self.backend.get_filename()
            }
            json.dump(save_data, outfile)
            outfile.close()
