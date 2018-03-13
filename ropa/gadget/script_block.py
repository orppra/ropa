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

from block import Block


class ScriptBlock(Block):

    def __init__(self, text):
        super(ScriptBlock, self).__init__('ScriptBlock')
        self.text = text

    def content(self):
        return self.text

    def is_editable(self):
        return False

    def set_text(self, text):
        self.text = text

    def get_text(self, text):
        return self.text

    def __repr__(self):
        res = ""

        for gadget in self.gadgets:
            res += repr(gadget)
            res += "\n"

        return res
