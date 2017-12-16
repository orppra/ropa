import sys
from PyQt4 import QtGui as qg, QtCore as qc, uic
from ropper import Backend

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
        return filenames[0]


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

    backend = Backend(w)

    # get list
    def showInResultsList(gadgets):
        pass

    w.filterInput = w.findChild(qg.QLineEdit, 'searchBar')

    def filterFunction():
        gadgets = backend.process_query('instruction', w.filterInput.text)
        showInResultsList(gadgets)

    w.filterButton = w.findChild(qg.QPushButton, 'searchButton')
    w.filterButton.clicked.connect(filterFunction)

    def startNewProject():
        filepath = open_file_dialog()
        print(filepath)
        backend.set_filename(filepath)

    newProjectButton = w.findChild(qg.QAction, 'actionNew')
    newProjectButton.clicked.connect()

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
