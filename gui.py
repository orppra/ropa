import sys
from PyQt4 import QtGui as qg, QtCore as qc, uic

Ui_MainWindow, QtBaseClass = uic.loadUiType('scene.ui')
app = qg.QApplication(sys.argv)


class App(qg.QMainWindow, Ui_MainWindow):
    def __init__(self):
        qg.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


def quit():
    app.quit()


def open_file_dialog():
    dialog = qg.QFileDialog()
    dialog.setFileMode(qg.QFileDialog.AnyFile)
    filenames = qc.QStringList()
    if dialog.exec_():
        filenames = dialog.selectedFiles()
        for filename in filenames:
            open_file(filename)


def open_file(filename):
    result = ''
    with open(filename, 'r') as file:
        for line in file:
            result += line
    return result


def main():
    app_name = 'VsymX'

    # TODO: bind this thing correctly
    # exit = app.findChild(qg.QAction, 'actionExit')
    # exit.clicked.connect(quit)

    w = App()
    w.resize(1080, 720)
    w.move(300, 300)
    w.setWindowTitle(app_name)
    w.show()
    open_file_dialog()
    sys.exit(app.exec_())

    # setProperty('', value)
    # findChild(child_type, child_name)
    # searchBar, searchButton


if __name__ == '__main__':
    main()
