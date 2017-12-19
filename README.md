# ropa
ropa is a GUI to craft [ROP](https://en.wikipedia.org/wiki/Return-oriented_programming) chains as easily as possible, based on [Ropper](https://github.com/sashs/Ropper).

ropa provides a cleaner interface when using ropper as compared to the command line.

## Table of Contents

- [Features](#features)
- [Install](#install)
- [Usage](#usage)
	- [Generator](#generator)
- [License](#license)

## Features

- Gadget searching with ropper
- Easy gadget selection
- Group multiple gadgets
- Export rop chain as binary file or python scripts (struct/pwntools/custom)
- Project saving

### New to ROP
ropa can provide a smoother workflow by crafting the rop chain in the GUI, then exporting the final chain in the desired format.

### Experienced
For people that are already experienced, CLI may be your thing, and this is just dumb and tedious. However, you can also use this as a cleaner terminal to filter out the relevant gadgets.

## Install
### Ropper
We use the Ropper API for our gadget searching. Installation instructions can be found [here](https://github.com/sashs/Ropper). Or, just do

```
pip install Ropper
```

### PyQt4
The GUI runs on top of PyQt4. To install, just do

#### Apt
```
sudo apt install python-qt4
```

#### Yum
```
sudo yum install PyQt4
```

## Usage
`python gui.py`

## License
[MIT](LICENSE)
