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
    sys.exit(app.exec_())


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


def bind_menu_button(window, button_name, func, shortcut_str=None):
    button = window.findChild(qg.QAction, button_name)
    if shortcut_str:
        button.setShortcut(shortcut_str)
    button.triggered.connect(func)


def main():
    app_name = 'VsymX'

    w = App()
    w.resize(1080, 720)
    w.move(300, 300)
    w.setWindowTitle(app_name)

    backend = Backend(w)

    # get list
    def showInResultsList(gadgets):
        print(gadgets)
        pass

    filterInput = w.findChild(qg.QLineEdit, 'searchBar')

    def filterFunction():
        gadgets = backend.process_query('instruction', filterInput.text)
        showInResultsList(gadgets)

    filterButton = w.findChild(qg.QPushButton, 'searchButton')
    filterButton.clicked.connect(filterFunction)

    def startNewProject():
        filepath, arch = open_file_dialog(backend)

    bind_menu_button(w, 'actionNew', startNewProject, 'Ctrl+N')
    bind_menu_button(w, 'actionQuit', quit, 'Ctrl+Q')
    w.show()
    quit()


if __name__ == '__main__':
    main()
