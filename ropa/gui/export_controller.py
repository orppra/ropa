from file_dialog_controller import FileDialogController


class ExportController:
    def __init__(self, backend, widget):
        self.backend = backend
        self.widget = widget
        self.file_dialog_controller = FileDialogController()

    def export_binary(self):
        filepath = self.file_dialog_controller.open_file_dialog()
        chain = []
        for index in range(self.widget.count()):
            block = str(self.widget.item(index).text())
            print(str(block))
            block = block.strip().split('\n')
            address = block[0]
            block = block[2:]
            instructions = []
            for b in block:
                instructions.append(block)
            chain.append([{'address': address, 'instructions': instructions}])

        self.backend.export_binary(filepath, chain)

    def export_python_struct(self):
        filepath = self.file_dialog_controller.open_file_dialog()
        chain = []
        for index in range(self.widget.count()):
            block = str(self.widget.item(index).text())
            print(str(block))
            block = block.strip().split('\n')
            address = block[0]
            block = block[2:]
            instructions = []
            for b in block:
                instructions.append(b)
            chain.append([{'address': address, 'instructions': instructions}])

        self.backend.export_python_struct(filepath, chain)

    def export_python_pwntools(self):
        filepath = self.file_dialog_controller.open_file_dialog()
        chain = []
        for index in range(self.widget.count()):
            block = str(self.widget.item(index).text())
            block = block.strip().split('\n')
            address = block[0]
            block = block[2:]
            instructions = []
            for b in block:
                print(b)
                instructions.append(b)
            print(instructions)
            chain.append([{'address': address, 'instructions': instructions}])

        self.backend.export_python_pwntools(filepath, chain)
