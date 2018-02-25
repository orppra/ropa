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

import json

from ropa.services import DialogService


class ProjectService:
    def __init__(self, backend):
        self.backend = backend
        self.dialog_service = DialogService()

    def new_file(self, filepath=None):
        if filepath is None:
            filepath = str(self.dialog_service.file_dialog('New Project'))

        self.backend.reset()
        self.backend.set_filename(str(filepath))
        self.backend.activate()

        print(filepath)
        return filepath

    def open_file(self, filepath=None):
        if filepath is None:
            filepath = str(self.dialog_service.file_dialog('Open Project'))

        save_data = None
        with open(filepath, 'r') as infile:
            save_data = json.load(infile)

        self.backend.reset()
        self.backend.set_filename(save_data['filename'])
        self.backend.activate()

        print(filepath)
        return filepath

        # doesn't work for now, need to settle on refactoring other stuff first
        # self.chain = save_data['chain']
        # self.favorites = save_data['favorites']

    def save_file(self):
        filepath = str(self.dialog_service.file_dialog('Save Project'))
        with open(filepath, 'w') as outfile:
            save_data = {
                # doesn't work now, settle on refactoring first
                # 'chain': self.chain,
                # 'favorites': self.favorites,
                'filename': self.backend.get_filename()
            }
            json.dump(save_data, outfile)
            outfile.close()

        return filepath
