class BadbytesInputController:
    def __init__(self, backend, textbox):
        self.backend = backend
        self.textbox = textbox

    def _get_text(self):
        return str(self.textbox.text())

    def update_badbytes(self):
        self.backend.update_badbytes(self._get_text())
