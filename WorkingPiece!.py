from Main import Ui_MainWindow
from nonregusrscreen import Ui_NonRegUserScreen
from PyQt5 import QtCore, QtGui, QtWidgets
from reguserscreen import Ui_RegUserScreen
from Choose import Ui_Choose
from measure1 import Ui_measure1
from measure2 import Ui_measure2
import os
import time


class Firstwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Firstwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton.clicked.connect(self.hide)


class NonRegwindow(QtWidgets.QDialog, Ui_NonRegUserScreen):
    def __init__(self, parent=None):
        super(NonRegwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)
    
    def register(self):
        user = self.lineEdit.text()
        userUP = user.upper()
        f = open(userUP + ".txt", "a") #if start with "r", will give an error if file does not exist
        f.close()
        f = open(userUP + ".txt", "r")
        if f.readline() != "": #this ensures another file with the same name does not exist
            self.entername.setText("This name is already in use. Try another one")
            f.close()

        elif f.readline() == "":
            manager.openchoice()

class Regwindow(QtWidgets.QDialog, Ui_RegUserScreen):
    
    def __init__(self, parent=None):
        super(Regwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)

    def openuser(self):
        user = self.lineEdit.text()
        userUP = user.upper()
        f = open(userUP + ".txt", "a") #if start with "r", will give an error if file does not exist
        f.close()
        f = open(userUP + ".txt", "r")
        if f.readline() == "":
            self.entername.setText("This name does not seem to be registered.")
            f.close()
            os.remove(userUP + ".txt")
        
        else:
            manager.openchoice()
            

class Choose(QtWidgets.QDialog, Ui_Choose):
    def __init__(self, parent=None):
        super(Choose, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.hide)
        

class Measure1(QtWidgets.QDialog, Ui_measure1):
    def __init__(self, parent=None):
        super(Measure1, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)

    def PushMeasurement(self):
        weight = "1-" + self.spinweight.text()
        waist = "2-" + self.spinwaist.text()
        arms = "3-" + self.spinarms.text()
        thighs = "4-" + self.spinthighs.text()

        user = self.entername_6.text()
        userUP = user.upper()
        f = open(userUP + ".txt", "a")
        f.write(weight + "\n")
        f.write(waist + "\n")
        f.write(arms + "\n")
        f.write(thighs + "\n")
        f.close()
        time.sleep(1)
        manager.openmeasure2()



class Measure2(QtWidgets.QDialog, Ui_measure2):
    def __init__(self, parent=None):
        super(Measure2, self).__init__(parent)
        self.setupUi(self)
        self.measure1 = Measure1()
        self.pushButton_3.clicked.connect(self.hide)
        self.pushButton_4.clicked.connect(self.updatetable)

    def updatetable(self):
        self.wecur.setText(self.measure1.spinweight.text())
        manager.average("1-", self.measure1.spinweight.text(),self.weavg.setText)
        



    




class Manager:
    def __init__(self):

        #Show windows/hide windows section
        self.first = Firstwindow()
        self.second = NonRegwindow()
        self.third = Regwindow()
        self.choose = Choose()
        self.measure1 = Measure1()
        self.measure2 = Measure2()



        self.first.pushButton.clicked.connect(self.third.show)
        self.first.pushButton_2.clicked.connect(self.second.show)
        self.second.pushButton_2.clicked.connect(self.first.show)
        self.third.pushButton_2.clicked.connect(self.first.show)
        self.measure1.pushButton_2.clicked.connect(self.choose.show)
        self.measure2.pushButton_3.clicked.connect(self.choose.show)
        self.choose.pushButton.clicked.connect(self.measure1.show)
        self.first.show()


        #linked to functions related to NonReg window
        self.second.pushButton.clicked.connect(self.second.register)

        #linked to functions related to Reg window
        self.third.pushButton.clicked.connect(self.third.openuser)

        #linked to functions related to measure1
        self.measure1.pushButton.clicked.connect(self.measure1.PushMeasurement)

        #linked to functions related to measure2
        
        

    def openchoice(self):
        self.third.hide()
        self.second.hide()
        self.choose.show()
        if self.third.lineEdit.text() != "":
            self.measure1.entername_6.setText((self.third.lineEdit.text()).capitalize())
            self.measure2.entername_8.setText((self.third.lineEdit.text()).capitalize())
        else: 
            self.measure1.entername_6.setText((self.second.lineEdit.text()).capitalize())
            self.measure2.entername_8.setText((self.second.lineEdit.text()).capitalize())

    def openmeasure2(self):
        self.measure1.hide()
        self.measure2.show()


    def average(self, n, o, add):
        userUP = self.measure2.entername_8.text().upper()
        f = open(userUP + ".txt", "r")
        avg = 0
        hm = 0
        for line in f:
            if line.startswith(n):
                hm = hm + float(line[2:].strip())
                avg = avg + 1
        resavg = hm / avg
        avgtot = (float(o) - float(resavg))
        add(str(avgtot))
        f.close()

        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())