from nonregusrscreen import Ui_NonRegUserScreen
from Main import Ui_MainWindow     # needs to import from the main file
from PyQt5 import QtCore, QtGui, QtWidgets #importing PyQt functionality

class mainWin(QtWidgets.QMainWindow, Ui_MainWindow): #mainWin is new subclass. QtWidgets.Whatever the window was / you need to get inheritance from Ui_MainWindow, otherwise you wil lahve to use self.ui.pushbutton....
    def __init__(self, *args, **kwargs):   #passing arguments from whatever was called
       super().__init__(*args, **kwargs)
       self.ui = Ui_MainWindow()
       self.setupUi(self)
       self.pushButton_2.clicked.connect(self.openwindow) # you have to include UI, otherwise it will not work.
    
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