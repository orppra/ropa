import sys
import os
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


def new_file_dialog():
    dialog = qg.QFileDialog()
    dialog.setWindowTitle('Choose binary')
    dialog.setFileMode(qg.QFileDialog.AnyFile)
    filenames = qc.QStringList()
    if dialog.exec_():
        filenames = dialog.selectedFiles()
        arch = open_arch_dialog()
        return filenames[0], arch
    raise Exception('Failed to open dialog')

def open_file_dialog():
    dialog = qg.QFileDialog()
    dialog.setWindowTitle('Open File')
    dialog.setFileMode(qg.QFileDialog.AnyFile)
    filenames = qc.QStringList()
    if dialog.exec_():
        filenames = dialog.selectedFiles()
        return filenames[0]
    raise Exception('Failed to open dialog')


def open_arch_dialog():
    dialog = uic.loadUi('arch_dialog.ui')
    dialog.setWindowTitle('Select Architecture')
    arch_table = dialog.findChild(qg.QTableWidget, 'arch_table')
    row = -1  # idk why
    arch_table.setColumnCount(1)
    arch_table.setRowCount(len(architectures))
    arch_table.horizontalHeader().setResizeMode(0, qg.QHeaderView.Stretch)
    have_selected = False
    for archi in architectures:
        item = qg.QTableWidgetItem(archi)
        item.setFlags(qc.Qt.ItemIsSelectable | qc.Qt.ItemIsEnabled)
        if not have_selected:
            item.setSelected(True)
            have_selected = True
        arch_table.setItem(row, 1, item)
        row += 1
    dialog.show()
    if dialog.exec_():
        if arch_table.selectedItems() is not None:
            arch = str(arch_table.selectedItems()[0].text())
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
    w.resize(1200, 720)
    w.move(300, 300)
    w.setWindowTitle(app_name)

    backend = Backend(w)
    chain_list = w.findChild(qg.QListView, 'graphicsView')
    chain_list.setDragEnabled(True)
    gadgets_list = w.findChild(qg.QListView, 'gadgetsList')
    gadgets_list.setDragEnabled(True)

    def show_in_gadgets_list(gadgets):
        gadgets_list.reset()
        model = qg.QStandardItemModel(gadgets_list)
        for gadget in gadgets:
            cell = gadget['address'] + ':\n'
            cell += '-' * 2 * len(str(gadget['address'])) + '\n'
            cell += '\n'.join(gadget['instructions']) + '\n'
            item = qg.QStandardItem(cell)
            item.setEditable(False)
            # item.setDragDropMode('InternalMove')
            model.appendRow(item)

        gadgets_list.setModel(model)
        gadgets_list.setDragEnabled(True)
        gadgets_list.viewport().setAcceptDrops(True)
        gadgets_list.setDropIndicatorShown(True)

    filter_input = w.findChild(qg.QLineEdit, 'searchBar')

    def filter_function():
        gadgets = backend.process_query('instruction',
                                        str(filter_input.text()))
        show_in_gadgets_list(gadgets)

    def semantics_function():
        gadgets = backend.process_query('semantic', str(filter_input.text()))
        show_in_gadgets_list(gadgets)

    def ppr_function():
        gadgets = backend.process_query('pop-pop-ret', '')
        show_in_gadgets_list(gadgets)

    filter_button = w.findChild(qg.QPushButton, 'searchButton')

    def filter():
        searchType = w.findChild(qg.QButtonGroup, 'searchType').checkedId()
        if searchType == -2:
            filter_function()
        elif searchType == -3:
            ppr_function()
        elif searchType == -4:
            semantics_function()

    filter_button.clicked.connect(filter)
    filter_input.returnPressed.connect(filter)
    # semantics_button = w.findChild(qg.QPushButton, 'semanticsButton')
    # semantics_button.clicked.connect(semantics_function)
    # ppr_button = w.findChild(qg.QPushButton, 'pprButton')
    # ppr_button.clicked.connect(ppr_function)

    def startNewProject():
        filepath, arch = new_file_dialog()
        w.setWindowTitle(app_name + ' - ' + os.path.basename(str(filepath)))
        backend.set_arch(arch)
        backend.set_filename(str(filepath))
        backend.activate()

    def openProject():
        filepath = open_file_dialog()
        print("Opened " + str(filepath))
        backend.open_project(str(filepath))
        w.setWindowTitle(app_name + ' - ' +
                         os.path.basename(str(backend.get_filename())))

    def saveProject():
        filepath = open_file_dialog()
        backend.save_project(str(filepath))

    bind_menu_button(w, 'actionNew', startNewProject, 'Ctrl+N')
    bind_menu_button(w, 'actionOpen', openProject, 'Ctrl+O')
    bind_menu_button(w, 'actionSave', saveProject, 'Ctrl+S')
    bind_menu_button(w, 'actionQuit', quit, 'Ctrl+Q')

    # show_in_gadgets_list((('1234', 'high five!'),))

    badbytesInput = w.findChild(qg.QLineEdit, 'badbytesInput')

    def updateBadBytes():
        backend.update_badbytes(str(badbytesInput.text()))

    badbytesInput.textChanged.connect(updateBadBytes)

    w.show()
    quit()


if __name__ == '__main__':
    main()
