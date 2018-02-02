class ButtonController(object):
    def __init__(self, widget, backend):
        self.widget = widget
        self.backend = backend

    def _bind_clicked(self, func):
        self.widget.clicked.connect(lambda: func())
