import sys
from PyQt4 import QtGui as qg, QtCore as qc, uic
from backend.Backend import Backend
from backend.constants import architectures

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
        arch = open_arch_dialog(dialog)
        return arch, filenames[0]
    raise Exception('Failed to open dialog')


def open_arch_dialog(window):
    dialog = uic.loadUi('arch_dialog.ui')
    arch_table = dialog.findChild(qg.QTableWidget, 'arch_table')
    row = -1  # idk why
    arch_table.setColumnCount(1)
    arch_table.setRowCount(len(architectures))
    arch_table.horizontalHeader().setResizeMode(0, qg.QHeaderView.Stretch)
    for archi in architectures:
        item = qg.QTableWidgetItem(archi)
        arch_table.setItem(row, 1, item)
        row += 1
    dialog.show()
    if dialog.exec_():
        if arch_table.selectedItems() is not None:
            arch = arch_table.selectedItems[0]
        else:
            arch = 'x86'
        return arch
    return Exception('Failed to open dialog')


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
        print(gadgets)
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
    saveProjectButton = w.findChild(qg.QAction, 'actionSave')
    saveProjectButton.setShortcut('Ctrl+Q')

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
