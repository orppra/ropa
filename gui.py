import sys
from PyQt4 import QtGui, uic
from ropper import Backend

Ui_MainWindow, QtBaseClass = uic.loadUiType('scene.ui')
app = QtGui.QApplication(sys.argv)


class App(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


def quit():
    app.quit()


def main():
    app_name = 'VsymX'

    # TODO: bind this thing correctly
    # exit = app.findChild(QtGui.QAction, 'actionExit')
    # exit.clicked.connect(quit)

    w = App()
    w.resize(1080, 720)
    w.move(300, 300)
    w.setWindowTitle(app_name)

    backend = Backend(w)

    # get list
    def showInResultsList(gadgets):
        pass

    w.filterInput = w.findChild(QtGui.QLineEdit, 'searchBar')

    def filterFunction():
        gadgets = backend.process_query('instruction', w.filterInput.text)
        showInResultsList(gadgets)
    w.filterButton = w.findChild(QtGui.QPushButton, 'searchButton')
    w.filterButton.clicked.connect(filterFunction)

    w.show()
    sys.exit(app.exec_())

    # setProperty('', value)
    # findChild(child_type, child_name)
    # searchBar, searchButton


if __name__ == '__main__':
    main()
