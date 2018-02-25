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

from ropa import config


class RecentFilesService:
    def __init__(self):
        with open(config.RECENT_FILES, 'r') as infile:
            self.files = json.load(infile)

    def add_file(self, filepath):
        if filepath in self.files:
            self.files.remove(filepath)
        self.files.insert(0, filepath)
        with open(config.RECENT_FILES, 'w') as outfile:
            json.dump(self.files, outfile)

    def get_files(self):
        return self.files
