from nonregusrscreen import Ui_NonRegUserScreen
from PyQt5 import QtCore, QtGui, QtWidgets


class NonReg(QtWidgets.QDialog, Ui_NonRegUserScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NonRegUserScreen
        self.setupUi(self)
        self.pushButton_2.clicked.connect(lambda: self.closewindow)

    def closewindow(self):
        self.window = exit()


    
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = NonReg()
    w.show()
    app.exec_()