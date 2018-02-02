from button_controller import ButtonController


class PoppopretButtonController(ButtonController):
    def __init__(self, widget, backend, lwc):
        super(PoppopretButtonController, self).__init__(widget, backend)
        self.lwc = lwc

        self._bind_clicked(self.filter)
        self.widget.setToolTip(
            "Search for gadgets containing <i>POP POP RET</i> sequences")

    def filter(self):
        gadgets = self.backend.process_query('pop-pop-ret', '')
        self.lwc.set_gadgets(gadgets)
