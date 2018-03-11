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
    def __init__(self, app, widget):
        super(BadbytesInputController, self).__init__(app, widget)
        self._bind_input_changed(self.update)
        self._bind_input_return(self.filter)

    def filter(self):
        filter_button = self.app.instructions_button
        filter_button.filter()

    def update(self):
        if len(self.get_text()) % 2 == 0:
            self.search_service.update_badbytes(self.get_text())
