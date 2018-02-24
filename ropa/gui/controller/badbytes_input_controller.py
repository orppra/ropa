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

from input_controller import InputController


class BadbytesInputController(InputController):
    def __init__(self, widget, backend, lwc, filter_button):
        super(BadbytesInputController, self).__init__(widget, backend)
        self.lwc = lwc
        self.filter_button = filter_button
        self._bind_input_changed(self.update)
        self._bind_input_return(self.filter)

    def filter(self):
        self.filter_button.filter()

    def update(self):
        if len(self.get_text()) % 2 == 0:
            self.backend.update_badbytes(self.get_text())
