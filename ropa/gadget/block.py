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


class Block:

    def __init__(self, gadgets, comments=""):
        self.gadgets = gadgets
        self.comments = comments
        self.show_comments = False

    def add_gadgets(self, gadgets):
        self.gadgets.extend(gadgets)

    def get_gadgets(self):
        return self.gadgets

    def get_comments(self):
        return self.comments

    def merge(self, rhs):
        block = Block(self.gadgets, self.comments + " " + rhs.comments)
        block.add_gadgets(rhs.get_gadgets())
        return block

    def set_comments(self, comments):
        self.comments = comments

    def toggle_show_comments(self):
        self.show_comments = not self.show_comments

    def is_showing_comments(self):
        return not self.show_comments

    def content(self):
        cell = ''

        if not self.show_comments:
            cell += '<pre>'
            for i in range(len(self.gadgets)):
                gadget = self.gadgets[i]
                if i > 0:
                    cell += "<br/>"
                cell += gadget.content()

            cell += '</pre>'
        else:
            cell = self.comments

        self.toggle_show_comments()

        return cell

    def get_query(self):
        query = ""

        for i in range(len(self.gadgets)):
            gadget = self.gadgets[i]
            if i > 0:
                query += "\n"
            query += gadget.get_query()

        return query

    def __repr__(self):
        res = ""

        for gadget in self.gadgets:
            res += repr(gadget)
            res += "\n"

        return res
