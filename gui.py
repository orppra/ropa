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
    sys.exit(app.exec_())


def open_file_dialog(backend):
    dialog = qg.QFileDialog()
    dialog.setWindowTitle('Open File')
    dialog.setFileMode(qg.QFileDialog.AnyFile)
    filenames = qc.QStringList()
    if dialog.exec_():
        filenames = dialog.selectedFiles()
        arch = open_arch_dialog()
        return arch, filenames[0]
    raise Exception('Failed to open dialog')


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


def bind_menu_button(window, button_name, func, shortcut_str=None):
    button = window.findChild(qg.QAction, 'actionQuit')
    if shortcut_str:
        button.setShortcut(qg.QKeySequence(shortcut_str))
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
