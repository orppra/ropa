import sys
from PyQt4 import QtCore, QtGui, uic

class Scene(QtGui.QWidget):
	def __init__(self):
    	uic.loadUi('scene.ui', self)
    sys.exit(app.exec_())

def main():
    
    app = QtGui.QApplication(sys.argv)

    app_name = 'VsymX'

    w = Scene()
    w.resize(500, 500)
    w.move(300, 300)
    w.setWindowTitle(app_name)
    w.show()

    #setProperty('', value)
    #findChild(name)
    #searchBar, searchButton
    

if __name__=='__main__':
	main()