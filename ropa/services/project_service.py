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

import pickle

from ropa.services import DialogService


class SaveData:
    def __init__(self, filepath, chain, favourites):
        self.filepath = filepath
        self.chain = chain
        self.favourites = favourites

    def get_filepath(self):
        return self.filepath

    def get_chain(self):
        return self.chain

    def get_favourites(self):
        return self.favourites


class ProjectService:
    def __init__(self, app):
        self.app = app
        self.search_service = app.get_search_service()
        self.dialog_service = DialogService()

    def new_file(self, filepath=None):
        if filepath is None:
            filepath = str(self.dialog_service.file_dialog('New Project'))

        self.search_service.reset()
        self.search_service.set_filepath(str(filepath))
        self.search_service.activate()

        self.app.reset()

        print(filepath)
        return filepath

    def open_file(self, filepath=None):
        if filepath is None:
            filepath = str(self.dialog_service.file_dialog('Open Project'))

        save_data = pickle.loads(open(filepath, 'r').read())

        self.search_service.reset()
        self.search_service.set_filepath(save_data.get_filepath())
        self.search_service.activate()

        self.app.reset()

        for block in save_data.get_chain():
            block.toggle_show_comments()
        for block in save_data.get_favourites():
            block.toggle_show_comments()

        self.app.chain_list.set_blocks(save_data.get_chain())
        self.app.favourites_list.set_blocks(save_data.get_favourites())

        print(filepath)
        return filepath

    def save_file(self):
        filepath = str(self.dialog_service.file_dialog('Save Project'))
        save_data = SaveData(self.search_service.get_filepath(),
                             self.app.chain_list.get_blocks(),
                             self.app.favourites_list.get_blocks())
        open(filepath, 'w').write(pickle.dumps(save_data))

        return filepath
