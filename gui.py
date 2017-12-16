import sys
from PyQt4 import QtGui as qg, QtCore as qc, uic
from backend.Backend import Backend

Ui_MainWindow, QtBaseClass = uic.loadUiType('scene.ui')
app = qg.QApplication(sys.argv)


class App(qg.QMainWindow, Ui_MainWindow):
    def __init__(self):
        qg.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


def quit():
    app.quit()


def open_file_dialog(backend):
    dialog = qg.QFileDialog()
    dialog.setWindowTitle('Open File')
    dialog.setFileMode(qg.QFileDialog.AnyFile)
    filenames = qc.QStringList()
    if dialog.exec_():
        filenames = dialog.selectedFiles()
        arch = open_arch_dialog()
        return arch, filenames[0]
    raise Exception('Failed to open dialog/')


def open_arch_dialog():
    dialog = qg.QDialog()
    dialog.ui = uic.loadUi('arch_dialog.ui')
    dialog.ui.show()
    arch_table = dialog.ui.findChild(qg.QTableWidget, 'arch_table')
    # if arch_table.selectedItems():
    #    arch = arch_table.selectedItems()[0]
    arch = None
    return arch


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
        filepath, arch = open_file_dialog(backend)
    newProjectButton = w.findChild(qg.QAction, 'actionNew')
    newProjectButton.triggered.connect(startNewProject)

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
