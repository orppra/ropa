from PyQt4 import QtGui as qg, QtCore as qc


class DialogService:
    def file_dialog(self, title):
        dialog = qg.QFileDialog()
        dialog.setWindowTitle(title)
        dialog.setFileMode(qg.QFileDialog.AnyFile)
        filenames = qc.QStringList()
        if dialog.exec_():
            filenames = dialog.selectedFiles()
            return filenames[0]
        raise Exception('Failed to open dialog')
