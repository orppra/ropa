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


class Gadget:

    def __init__(self, address, instructions, query):
        self.addr = address
        self.instructions = instructions
        self.query = query
        self.comments = "aaaaaa"
        self.show_comments = False

    def get_addr(self):
        return self.addr

    def get_instructions(self):
        return self.instructions

    def get_query(self):
        return self.query

    def get_comments(self):
        return self.comments

    def set_comments(self, comments):
        self.comments = comments

    def is_showing_comments(self):
        return not self.show_comments

    def content(self):
        if not self.show_comments:
            cell = '<pre>'
            cell += '<b>%s</b>\n' % hex(self.addr)[:-1]
            for instruction in self.instructions:
                cell += '%s\n' % instruction.get_text()
            cell += '</pre>'
        else:
            cell = self.comments

        self.show_comments = not self.show_comments

        return cell

    def __repr__(self):
        res = ''
        res += hex(self.addr)[:-1]
        for i in self.instructions:
            res += i.get_text()
        res += '(%s)' % self.query

        return res
