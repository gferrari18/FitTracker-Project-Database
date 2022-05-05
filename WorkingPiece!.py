from msilib.schema import Class
from Main import Ui_MainWindow
from nonregusrscreen import Ui_NonRegUserScreen
from PyQt5 import QtCore, QtGui, QtWidgets
from reguserscreen import Ui_RegUserScreen
from Choose import Ui_Choose
from measure1 import Ui_measure1
from measure2 import Ui_measure2
from EnterEx import Ui_EnterEx
from viewex1 import Ui_viewex1
from viewex2 import Ui_ViewEx2
import os
import time
import collections


class MuscleGroup:
    def __init__(self, muscname='', exname='',sets='',reps='',weight=''):
        self.muscname= muscname
        self.exname = exname
        self.sets = sets
        self.reps = reps
        self.weight = weight


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

        else:
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
        self.pushButton_3.clicked.connect(self.hide)
        

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
        manager.upmeasure2()
        time.sleep(1)
        manager.openmeasure2()



class Measure2(QtWidgets.QDialog, Ui_measure2):
    def __init__(self, parent=None):
        super(Measure2, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.hide)
        #self.pushButton_4.clicked.connect(self.updatetable)

    def updatetable(self):
        manager.average("1-", self.wecur.text(),self.weavg.setText)
        manager.average("2-", self.wacur.text(),self.waavg.setText)
        manager.average("3-", self.arcur.text(),self.aravg.setText)
        manager.average("4-", self.thcur.text(),self.thavg.setText)
        self.initial()

    def initial(self):
        manager.initial("1-", self.weini.setText)
        manager.initial("2-", self.waini.setText)
        manager.initial("3-", self.arini.setText)
        manager.initial("4-", self.thini.setText)

class EnterEx(QtWidgets.QDialog, Ui_EnterEx):
    def __init__(self, parent=None):
        super(EnterEx, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.comboBox_2.clear)
        self.pushButton.clicked.connect(self.appendex)
        


    def appendex(self):
        if self.comboBox.currentText() == "" or self.comboBox_2.currentText() == "":
            self.label_6.setText("You must fill all boxes!")
        else:
            userUP = (self.entername.text()).upper()
            entry = ((self.comboBox.currentText())+ " " + (self.comboBox_2.currentText())+ " " + (self.spinBox.text())+ " " + (self.spinBox_2.text()) + " " + (self.spinBox_3.text())+ "\n")
            f = open(userUP + ".txt", "a")
            f.write(entry)
            f.close()
            self.label_6.setText("Entry for " + (self.comboBox_2.currentText()) + " was registered")
            self.comboBox.setCurrentIndex(0)

class ViewEx1(QtWidgets.QDialog, Ui_viewex1):
    def __init__(self, parent = None):
        super(ViewEx1, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.viewexcheck)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.comboBox_2.clear)


    def viewexcheck(self):
        if self.comboBox.currentText() == "" or self.comboBox_2.currentText() == "":
            self.label_6.setText("You must fill all boxes!")
        else:
            self.hide()
            manager.viewex2.ExName.setText(self.comboBox_2.currentText())
            manager.viewex2.show()
            manager.UpdateViewEx2()
            

class ViewEx2(QtWidgets.QDialog,Ui_ViewEx2):
    def __init__(self,parent=None):
        super(ViewEx2, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.hide)



class Manager:
    def __init__(self):

        #Show windows/hide windows section
        self.first = Firstwindow()
        self.second = NonRegwindow()
        self.third = Regwindow()
        self.choose = Choose()
        self.measure1 = Measure1()
        self.measure2 = Measure2()
        self.enterex = EnterEx()
        self.viewex1 = ViewEx1()
        self.viewex2 = ViewEx2()
    



        self.first.pushButton.clicked.connect(self.third.show)
        self.first.pushButton_2.clicked.connect(self.second.show)
        self.second.pushButton_2.clicked.connect(self.first.show)
        self.third.pushButton_2.clicked.connect(self.first.show)
        self.measure1.pushButton_2.clicked.connect(self.choose.show)
        self.measure2.pushButton_3.clicked.connect(self.choose.show)
        self.choose.pushButton.clicked.connect(self.measure1.show)
        self.choose.pushButton_2.clicked.connect(self.enterex.show)
        self.choose.pushButton_3.clicked.connect(self.viewex1.show)
        self.enterex.comboBox.activated.connect(self.UpdateComBox)
        self.viewex1.comboBox.activated.connect(self.UpdateComBox2)
        self.enterex.pushButton_2.clicked.connect(self.choose.show)
        self.viewex1.pushButton_2.clicked.connect(self.choose.show)
        self.viewex2.pushButton_3.clicked.connect(self.choose.show)
        self.first.show()

        
        self.second.pushButton.clicked.connect(self.second.register)
        self.third.pushButton.clicked.connect(self.third.openuser)
        self.measure1.pushButton.clicked.connect(self.measure1.PushMeasurement)
        self.measure1.pushButton.clicked.connect(self.measure2.updatetable)

    def openchoice(self):
        self.third.hide()
        self.second.hide()
        self.choose.show()
        if self.third.lineEdit.text() != "":
            self.measure1.entername_6.setText((self.third.lineEdit.text()).capitalize())
            self.measure2.entername_8.setText((self.third.lineEdit.text()).capitalize())
            self.enterex.entername.setText((self.third.lineEdit.text()).capitalize())
            self.viewex1.entername.setText((self.third.lineEdit.text()).capitalize())
            self.viewex2.entername_8.setText((self.third.lineEdit.text()).capitalize())
        else: 
            self.measure1.entername_6.setText((self.second.lineEdit.text()).capitalize())
            self.measure2.entername_8.setText((self.second.lineEdit.text()).capitalize())
            self.enterex.entername.setText((self.second.lineEdit.text()).capitalize())
            self.viewex1.entername.setText((self.second.lineEdit.text()).capitalize())
            self.viewex2.entername_8.setText((self.second.lineEdit.text()).capitalize())

    def openmeasure2(self):
        self.measure1.hide()
        self.measure2.show()

    def upmeasure2(self):
        self.measure2.wecur.setText(self.measure1.spinweight.text())
        self.measure2.wacur.setText(self.measure1.spinwaist.text())
        self.measure2.arcur.setText(self.measure1.spinarms.text())
        self.measure2.thcur.setText(self.measure1.spinthighs.text())


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
        avgtotd = "{:.2f}".format(avgtot)
        add(str(avgtotd))
        f.close()

    def initial(self, n, add):
        userUP = self.measure2.entername_8.text().upper()
        measure = collections.deque()
        f = open(userUP + ".txt", "r")
        for line in f:
            if line.startswith(n):
                hm = line[2:].strip()
                measure.append(hm)
        l = measure.popleft()
        add(l)

    def UpdateComBox(self):
        self.enterex.comboBox_2.clear()
        userUP = self.enterex.entername.text().upper()
        items = []
        f = open(userUP + ".txt", "r")
        if self.enterex.comboBox.currentText() != "":
            for line in f:
                if line.startswith(self.enterex.comboBox.currentText()):
                    hm = line.strip().split(" ")
                    if hm[1] not in items: items.append(hm[1])
        f.close()
        self.enterex.comboBox_2.addItems(items)
        self.enterex.comboBox_2.setCurrentIndex(0)
    

  
    def UpdateComBox2(self):
        self.viewex1.comboBox_2.clear()
        userUP = self.viewex1.entername.text().upper()
        items = []
        f = open(userUP + ".txt", "r")
        if self.viewex1.comboBox.currentText() != "":
            for line in f:
                if line.startswith(self.viewex1.comboBox.currentText()):
                    hm = line.strip().split(" ")
                    if hm[1] not in items: items.append(hm[1])
        f.close()
        self.viewex1.comboBox_2.addItems(items)
        self.viewex1.comboBox_2.setCurrentIndex(0)


    def UpdateViewEx2(self):
        userUP = (self.viewex1.entername.text()).upper()
        f = open(userUP + ".txt", "r")
        musclist = []
        for line in f:
            if line.startswith(self.viewex1.comboBox.currentText()):
                hm = line.strip().split(" ")
                musc = MuscleGroup(hm[0],hm[1],hm[2],hm[3],hm[4])
                if musc.exname == self.viewex1.comboBox_2.currentText():
                    musclist.append(musc)
        f.close()

        setini = musclist[0].sets
        self.viewex2.sini.setText(setini)
        repini = musclist[0].reps
        self.viewex2.rini.setText(repini)
        weightini = musclist[0].weight
        self.viewex2.wini.setText(weightini)
        xm = (len(musclist) - 1)
        setcur = musclist[xm].sets
        self.viewex2.scur.setText(setcur)
        repcur = musclist[xm].reps
        self.viewex2.rcur.setText(repcur)
        weightcur = musclist[xm].weight
        self.viewex2.wcur.setText(weightcur)
    
     

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())