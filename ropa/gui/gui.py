import sys

from PyQt4 import QtGui as qg, QtCore as qc, uic

from ropa.backend import Backend
from ropa.gui import UI_PATH

from controller import (
    ListKeyController,
    FilterInputController,
    BadbytesInputController,
    MenuItemController,
    ExportController
)

try:
    _fromUtf8 = qc.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

Ui_MainWindow, QtBaseClass = uic.loadUiType(UI_PATH + '/scene.ui')


class App(qg.QMainWindow, Ui_MainWindow):
    def __init__(self, app_name, args):
        self.app_name = app_name

        self.backend = Backend(self)

        self.app = qg.QApplication(args)
        qg.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self._load_list_widgets()
        self._load_textinputs()
        self._load_buttons()
        self._bind_menu_buttons()

    def get_backend(self):
        return self.backend

    def get_app_name(self):
        return self.app_name

    def quit(self):
        sys.exit(self.app.exec_())

    def _load_list_widgets(self):
        self.gadgets_list_widget = self.findChild(qg.QListWidget,
                                                  'gadgetsList')
        self.gadgets_list_widget.setDragEnabled(True)

        self.chain_list_widget = self.findChild(qg.QListWidget, 'chainList')
        self.chain_list_widget.setDragEnabled(True)
        self.chain_list_widget.setAcceptDrops(True)
        self.chain_list_widget.setDropIndicatorShown(True)

        controller = ListKeyController(self.chain_list_widget)
        self.chain_list_widget.keyPressEvent = controller.key_press_event
        self.chain_list_widget.keyReleaseEvent = controller.key_release_event
        # graphics_model = qg.QStandardItemModel(graphics_view)
        # graphics_view.setModel(graphics_model)

        self.block_list_widget = self.findChild(qg.QListWidget, 'blockList')
        self.block_list_widget.setDragEnabled(True)
        self.block_list_widget.setAcceptDrops(True)
        self.block_list_widget.setDropIndicatorShown(True)
        # model = qg.QStandardItemModel(block_list)
        # block_list.setModel(model)

    def _load_buttons(self):
        self.search_instructions_button = self.findChild(qg.QPushButton,
                                                         'searchInstructions')
        self.search_poppopret_button = self.findChild(qg.QPushButton,
                                                      'searchPopPopRet')
        self.search_semantics_button = self.findChild(qg.QPushButton,
                                                      'searchSemantics')

        controller = FilterInputController(self.backend, self.filter_input,
                                           self.gadgets_list_widget)

        self._bind_button_clicked(self.search_instructions_button,
                                  controller.filter_function)
        self._bind_button_clicked(self.search_poppopret_button,
                                  controller.ppr_function)
        self._bind_button_clicked(self.search_semantics_button,
                                  controller.semantics_function)

    def _load_textinputs(self):
        self.filter_input = self.findChild(qg.QLineEdit, 'searchBar')

        self.badbytes_input = self.findChild(qg.QLineEdit, 'badbytesInput')

        fcontroller = FilterInputController(self.backend, self.filter_input,
                                            self.gadgets_list_widget)
        bcontroller = BadbytesInputController(self.backend,
                                              self.badbytes_input)

        self._bind_input_return(self.filter_input, fcontroller.filter_function)
        self._bind_input_return(self.badbytes_input,
                                fcontroller.filter_function)
        self._bind_input_changed(self.badbytes_input,
                                 bcontroller.update_badbytes)

    def _bind_button_clicked(self, button, func):
        button.clicked.connect(lambda: func())

    def _bind_input_return(self, input_box, func):
        input_box.returnPressed.connect(lambda: func())

    def _bind_input_changed(self, input_box, func):
        input_box.textChanged.connect(lambda: func())

    def _bind_menu_button(self, window, button_name, func, shortcut_str=None):
        button = window.findChild(qg.QAction, button_name)
        if shortcut_str:
            button.setShortcut(shortcut_str)
        button.triggered.connect(lambda: func())

    def _bind_menu_buttons(self):
        mcontroller = MenuItemController(self)

        self._bind_menu_button(self, 'actionNew',
                               mcontroller.start_new_project, 'Ctrl+N')
        self._bind_menu_button(self, 'actionOpen',
                               mcontroller.open_project, 'Ctrl+O')
        self._bind_menu_button(self, 'actionSave',
                               mcontroller.save_project, 'Ctrl+S')

        self._bind_menu_button(self, 'actionQuit', quit, 'Ctrl+Q')

        econtroller = ExportController(self.backend, self.chain_list_widget)

        self._bind_menu_button(self, 'actionBinary',
                               econtroller.export_binary)
        self._bind_menu_button(self, 'actionStruct',
                               econtroller.export_python_struct)
        self._bind_menu_button(self, 'actionPwntools',
                               econtroller.export_python_pwntools)


"""
def get_description_string():
    searchType = w.findChild(qg.QButtonGroup, 'searchType').checkedId()
    if searchType == -2:
        return str(filter_input.text())
    elif searchType == -3:
        return 'pop-pop-ret'
    elif searchType == -4:
        return str(filter_input.text())

def show_title_in_centre():
    return
    print('Added')
    item = graphics_view.item(graphics_view.count() - 1)
    toShow = '<b>' + get_description_string() + '</b>\n' + str(item.text())
    print(toShow)
    item.setText(toShow)

graphics_view.model().rowsInserted.connect(showTitleInCentre)
"""

# DragEnterEvent, DragMoveEvent, DragLeaveEvent, DropEvent
# block_list.drag
# semantics_button = w.findChild(qg.QPushButton, 'semanticsButton')
# semantics_button.clicked.connect(semantics_function)
# ppr_button = w.findChild(qg.QPushButton, 'pprButton')
# ppr_button.clicked.connect(ppr_function)

# def drop(e):
#     indices = gadgets_list.selectedIndexes()
#     print (gadgets_list.selectedIndexes())

# block_list.dropEvent(event)

# show_in_gadgets_list(({'address': '1234',
#                        'instructions': 'high five!'},))
