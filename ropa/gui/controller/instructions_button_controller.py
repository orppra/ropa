from button_controller import ButtonController


class InstructionsButtonController(ButtonController):
    def __init__(self, widget, backend, input_box, lwc):
        super(InstructionsButtonController, self).__init__(widget, backend)
        self.input_box = input_box
        self.lwc = lwc

        self.widget.setToolTip(
            "Search for instruction gadgets")
        self._bind_clicked(self.filter)

    def filter(self):
        gadgets = self.backend.process_query('instruction',
                                             self.input_box.get_text())
        self.lwc.set_gadgets(gadgets)
