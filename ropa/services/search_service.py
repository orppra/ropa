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

from search_backends import RopperBackend
from ropa.gadget import GadgetBlock


class SearchService:

    def __init__(self, app):
        self.app = app

        self.backends = [
            RopperBackend(app)
        ]

        self.reset()

    def get_filepath(self):
        return self.filepath

    def set_filepath(self, filepath):
        self.filepath = filepath

        for b in self.backends:
            b.set_file(filepath)

    def reset(self):
        for b in self.backends:
            b.reset()

        self.chain = []
        self.favourites = []
        self.update_badbytes('0a0d')

    def update_badbytes(self, badbytes):
        for b in self.backends:
            b.update_badbytes(badbytes)

    def process_query(self, command, ipt):
        if command == 'pop-pop-ret':
            query = command
        else:
            query = ipt

        blocks = []
        for b in self.backends:
            gadgets = b.query(query)
            blocks.extend([GadgetBlock([gadget]) for gadget in gadgets])

        return blocks

    def get_addr_len(self):
        ropper_backend = next(
            (b for b in self.backends if b.name == 'RopperBackend'), None)
        return ropper_backend.get_addr_len()
