from nonregusrscreen import Ui_NonRegUserScreen
from Main import Ui_MainWindow     # needs to import from the main file
from PyQt5 import QtCore, QtGui, QtWidgets #importing PyQt functionality

class mainWin(QtWidgets.QMainWindow): #mainWin is new subclass. QtWidgets.Whatever the window was
    def __init__(self, *args, **kwargs):   #passing arguments from whatever was called
       super().__init__(*args, **kwargs)
       self.ui = Ui_MainWindow() # this line and below builds what we had in the original file into here
       self.ui.setupUi(self)
       self.ui.pushButton_2.clicked.connect(self.openwindow) # you have to include UI, otherwise it will not work.
    
    def openwindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_NonRegUserScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    
        



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = mainWin()
    w.show()
    app.exec_()