from input_controller import InputController


class BadbytesInputController(InputController):
    def __init__(self, widget, backend, lwc, filter_button):
        super(BadbytesInputController, self).__init__(widget, backend)
        self.lwc = lwc
        self.filter_button = filter_button
        self._bind_input_changed(self.update)
        self._bind_input_return(self.filter)

    def filter(self):
        self.filter_button.filter()

    def update(self):
        if len(self.get_text()) % 2 == 0:
            self.backend.update_badbytes(self.get_text())
