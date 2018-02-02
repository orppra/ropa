from button_controller import ButtonController


class SemanticsButtonController(ButtonController):
    def __init__(self, widget, backend, input_box, lwc):
        super(SemanticsButtonController, self).__init__(widget, backend)
        self.input_box = input_box
        self.lwc = lwc

        self._bind_clicked(self.filter)
        self.widget.setToolTip(
            "Search for gadgets using Ropper's semantic searching function")

    def filter(self):
        gadgets = self.backend.process_query('semantic',
                                             self.input_box.get_text())
        self.lwc.set_gadgets(gadgets)
