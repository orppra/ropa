import sys
from PyQt4 import QtCore, QtGui, uic

Ui_MainWindow, QtBaseClass = uic.loadUiType('scene.ui')

class App(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    app_name = 'VsymX'

    w = App()
    w.resize(1080, 720)
    w.move(300, 300)
    w.setWindowTitle(app_name)
    w.show()
    sys.exit(app.exec_())

    #setProperty('', value)
    #findChild(name)
    #searchBar, searchButton
    
if __name__=='__main__':
	main()