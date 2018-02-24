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

from button_controller import ButtonController


class PoppopretButtonController(ButtonController):
    def __init__(self, widget, backend, lwc):
        super(PoppopretButtonController, self).__init__(widget, backend)
        self.lwc = lwc

        self._bind_clicked(self.filter)
        self.widget.setToolTip(
            "Search for gadgets containing <i>POP POP RET</i> sequences")

    def filter(self):
        gadgets = self.backend.process_query('pop-pop-ret', '')
        self.lwc.set_gadgets(gadgets)
