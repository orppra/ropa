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


class FilterInputController(InputController):
    def __init__(self, widget, backend, lwc):
        super(FilterInputController, self).__init__(widget, backend)
        self.lwc = lwc
        self._bind_input_return(self.filter)

    def filter(self):
        gadgets = self.backend.process_query('instruction', self.get_text())
        self.lwc.set_gadgets(gadgets)
