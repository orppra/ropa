# ropa
![screenshot](https://github.com/orppra/ropa/raw/master/screenshots/ropa_screenshot.png)

[![Build Status](https://travis-ci.org/orppra/ropa.svg?branch=master)](https://travis-ci.org/orppra/ropa)

ropa is a GUI tool to create ROP chains using the ropper API (i.e. a drag and drop interface to create rop chains).

Features include:
- Gadget searching with ropper
- Drag and drop to craft ROP chain
- "Bookmark" gadgets
- Export rop chain as exploit scripts (struct/pwntools/custom)
- Project saving

## Table of Contents
- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)

## Install
We use the [Ropper API](https://github.com/sashs/Ropper) for our gadget searching. The GUI runs on top of PyQt4.

### ropper
```
$ pip install Ropper
```

### pyqt4
```
$ sudo apt install python-qt4
$ sudo yum install PyQt4
```

You can install ropa from pip (currently only on python2 as ropper itself is under development in porting to python3)
```
$ pip install ropa
```

Or, if you would like to build from source
```
$ git clone https://github.com/orppra/ropa.git
$ python setup.py install
```

## Usage
Once you have installed ropa
```
$ ropa
```

Alternatively, without installation
```
$ python ropa.py
```

## Contribute
This is still under development, PRs are welcomed.
