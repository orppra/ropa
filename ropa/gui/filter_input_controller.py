from list_widget_controller import ListWidgetController


class FilterInputController:
    def __init__(self, backend, textbox, list_widget):
        self.backend = backend
        self.textbox = textbox
        self.widget = list_widget

    def _get_text(self):
        return str(self.textbox.text())

    def filter_function(self):
        gadgets = self.backend.process_query('instruction', self._get_text())
        ListWidgetController(self.widget).show_in_gadgets_list(gadgets)

    def semantics_function(self):
        gadgets = self.backend.process_query('semantic', self._get_text())
        ListWidgetController(self.widget).show_in_gadgets_list(gadgets)

    def ppr_function(self):
        gadgets = self.backend.process_query('pop-pop-ret', '')
        ListWidgetController(self.widget).show_in_gadgets_list(gadgets)
