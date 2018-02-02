from input_controller import InputController


class FilterInputController(InputController):
    def __init__(self, widget, backend, lwc):
        super(FilterInputController, self).__init__(widget, backend)
        self.lwc = lwc
        self._bind_input_return(self.filter)

    def filter(self):
        gadgets = self.backend.process_query('instruction', self.get_text())
        self.lwc.set_gadgets(gadgets)
