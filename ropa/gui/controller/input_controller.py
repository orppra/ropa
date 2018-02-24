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


class InputController(object):
    def __init__(self, widget, backend):
        self.widget = widget
        self.backend = backend

    def clear(self):
        self.widget.clear()

    def get_text(self):
        return str(self.widget.text())

    def _bind_input_return(self, func):
        self.widget.returnPressed.connect(lambda: func())

    def _bind_input_changed(self, func):
        self.widget.textChanged.connect(lambda: func())
