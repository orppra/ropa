class InputController(object):
    def __init__(self, widget, backend):
        self.widget = widget
        self.backend = backend

    def get_text(self):
        return str(self.widget.text())

    def _bind_input_return(self, func):
        self.widget.returnPressed.connect(lambda: func())

    def _bind_input_changed(self, func):
        self.widget.textChanged.connect(lambda: func())
