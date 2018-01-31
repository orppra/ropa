import sys

from PyQt4 import QtGui as qg, QtCore as qc, uic

from ropa.backend import Backend
from ropa.gui import UI_PATH
from html_delegate import HTMLDelegate

from controller import (
    ListKeyController,
    FilterInputController,
    BadbytesInputController,
    MenuItemController
)

from ropa.services import (
    ExportService
)

try:
    _fromUtf8 = qc.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

Ui_MainWindow, QtBaseClass = uic.loadUiType(UI_PATH + '/scene.ui')


class App(qg.QMainWindow, Ui_MainWindow):
    def __init__(self, app_name, args, new_project=None, open_project=None):
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

        mcontroller = MenuItemController(self)
        if new_project is not None:
            mcontroller.start_new_project(new_project)
        if open_project is not None:
            mcontroller.open_project(open_project)

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
        self.gadgets_list_widget.setAcceptDrops(False)
        self.gadgets_list_widget.setDropIndicatorShown(False)
        self.gadgets_list_widget.setVerticalScrollMode(
            qg.QAbstractItemView.ScrollPerPixel)
        self.gadgets_list_widget.setItemDelegate(
            HTMLDelegate(self.gadgets_list_widget))

        self.chain_list_widget = self.findChild(qg.QListWidget, 'chainList')
        self.chain_list_widget.setDragEnabled(True)
        self.chain_list_widget.setAcceptDrops(True)
        self.chain_list_widget.setDropIndicatorShown(True)
        self.chain_list_widget.setItemDelegate(
            HTMLDelegate(self.gadgets_list_widget))

        controller = ListKeyController(self.chain_list_widget)
        self.chain_list_widget.keyPressEvent = controller.key_press_event
        self.chain_list_widget.keyReleaseEvent = controller.key_release_event

        self.favorites_list_widget = self.findChild(qg.QListWidget,
                                                    'favoritesList')
        self.favorites_list_widget.setDragEnabled(True)
        self.favorites_list_widget.setAcceptDrops(True)
        self.favorites_list_widget.setDropIndicatorShown(True)
        self.favorites_list_widget.setItemDelegate(
            HTMLDelegate(self.gadgets_list_widget))

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

        self.search_instructions_button.setToolTip(
            "Search for instruction gadgets")
        self.search_poppopret_button.setToolTip(
            "Search for gadgets containing <i>POP POP RET</i> sequences")
        self.search_semantics_button.setToolTip(
            "Search for gadgets using Ropper's semantic searching function")

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

        exporter = ExportService(self.backend, self.chain_list_widget)

        self._bind_menu_button(self, 'actionBinary',
                               exporter.export_binary)
        self._bind_menu_button(self, 'actionStruct',
                               exporter.export_python_struct)
        self._bind_menu_button(self, 'actionPwntools',
                               exporter.export_python_pwntools)

    def _on_open_project(self):
        controller = FilterInputController(self.backend, self.filter_input,
                                           self.gadgets_list_widget)
        controller.filter_function()
