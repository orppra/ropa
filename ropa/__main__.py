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

import argparse
import sys

from ropa.gui import App


def start(args, file=None, load=None):
    app_name = 'ropa'

    w = App(app_name, args, file)

    w.show()
    w.quit()


def main():
    parser = argparse.ArgumentParser(description='Ropa - GUI based on Ropper')
    parser.add_argument('file', nargs='?')
    args = parser.parse_args()

    start(sys.argv, args.file)


if __name__ == "__main__":
    main()
