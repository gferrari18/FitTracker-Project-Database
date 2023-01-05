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
import collections
import time
import pyodbc
import webbrowser



class MuscleGroup: #set up class musclegroup so we can sepparate it once entered by user
    def __init__(self,sets='',reps='',weight=''):
        self.sets = sets
        self.reps = reps
        self.weight = weight


class Firstwindow(QtWidgets.QMainWindow, Ui_MainWindow): #sets up greeting window
    def __init__(self, parent=None):
        super(Firstwindow, self).__init__(parent)
        self.setupUi(self)
        #self.pushButton_2.clicked.connect(self.hide)
        self.pushButton.clicked.connect(self.hide)

    def registerweb(self): #redirects user to React website
        webbrowser.open('www.google.com')


class NonRegwindow(QtWidgets.QDialog, Ui_NonRegUserScreen): #sets up window for non registered users
    def __init__(self, parent=None):
        super(NonRegwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)
    
    def register(self): #registers new user.
        userUP= self.lineEdit.text().upper()
        if userUP == "": #does not allow user to create a file without a name. Works fine, but does not look good
            self.entername.setText("You must enter a name!")
        if userUP != "":
            sql = "SELECT COUNT(*) as C FROM Username WHERE username=?"
            crsr = db.cursor()
            res = crsr.execute(sql, (userUP))
            row = crsr.fetchone()
            if row.C == 0:
                sql = "INSERT INTO username (Username) VALUES (?)"    
                crsr = db.cursor()
                crsr.execute(sql, (userUP))
                crsr.commit()
                manager.openchoice()
                crsr.close()
            else:
                self.entername.setText("You must enter an unique name!")
            

class Regwindow(QtWidgets.QDialog, Ui_RegUserScreen): #Sets up window for registered users
    
    def __init__(self, parent=None):
        super(Regwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)

    def openuser(self): #ensures user account actually exists and contains data
        user= self.lineEdit.text()
        password = self.lineEdit2.text()
        if user == "": #does not allow user to create a file without a name. Works fine, but does not look good
            self.entername.setText("You must enter a name!")
        if user != "":
            sql = "SELECT COUNT(*) as C FROM loginfo WHERE username=? AND password=?"
            crsr = db.cursor()
            res = crsr.execute(sql, (user,password))
            row = crsr.fetchone()
            if row.C == 0:
                self.entername.setText("Password or username is incorrect!")
            else:
                manager.openchoice()
            crsr.close()
                
            

class Choose(QtWidgets.QDialog, Ui_Choose): #Sets up window with different option, so user can choose what they would like to do.
    def __init__(self, parent=None):
        super(Choose, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_3.clicked.connect(self.hide)
        

class Measure1(QtWidgets.QDialog, Ui_measure1): #sets up screen where user types their measurements
    def __init__(self, parent=None):
        super(Measure1, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)


    def PushMeasurement(self): #Adds measurements to user's file.
        weight = self.spinweight.text()
        waist = self.spinwaist.text()
        arms = self.spinarms.text()
        thighs = self.spinthighs.text()
        user = self.entername_6.text().upper()

        sql = "SELECT username FROM loginfo U WHERE U.username=?"
        crsr = db.cursor()
        res = crsr.execute(sql, (user))
        for row in res:
            ID = (row.__getattribute__('username'))
        crsr.close()

        sql = "INSERT INTO measurement (UserID, Weight, Waist, Arms, Thighs) VALUES (?,?,?,?,?)"
        crsr = db.cursor()
        crsr.execute(sql,(ID,weight,waist,arms,thighs))
        crsr.commit()
        crsr.close()
        

        manager.upmeasure2()
        time.sleep(1)
        manager.openmeasure2()



class Measure2(QtWidgets.QDialog, Ui_measure2): #sets ups screen were we show user's results
    def __init__(self, parent=None):
        super(Measure2, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.hide)

    def updatetable(self): #Reads user's file to calculate average then update table in the current screen
        manager.average("Weight", self.wecur.text(),self.weavg.setText)
        manager.average("Waist", self.wacur.text(),self.waavg.setText)
        manager.average("Arms", self.arcur.text(),self.aravg.setText)
        manager.average("Thighs", self.thcur.text(),self.thavg.setText)
        self.initial()

    def initial(self): #uses a deque to acquire first ever entry fo each of the measurements
        manager.initial("Weight", self.weini.setText)
        manager.initial("Waist", self.waini.setText)
        manager.initial("Arms", self.arini.setText)
        manager.initial("Thighs", self.thini.setText)



class EnterEx(QtWidgets.QDialog, Ui_EnterEx):
    def __init__(self, parent=None):
        super(EnterEx, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.comboBox_2.clear) #Clears combobox so it does not stack all entries created by updatecombox fxn.
        self.pushButton.clicked.connect(self.appendex)
        

    def appendex(self): #fxn used to append user work out entries
        if self.comboBox.currentText() == "" or self.comboBox_2.currentText() == "": #This does not let user to create a "blank" workout
            self.label_6.setText("You must fill all boxes!")
        else:
            user = self.entername.text()
            group = self.comboBox.currentText()
            exercise = self.comboBox_2.currentText()
            sets = self.spinBox.text()
            reps= self.spinBox_2.text()
            weight = self.spinBox_3.text()
            sql = "INSERT INTO exercises (UserID, musgroup, exercise, sets, reps, weight) VALUES (?,?,?,?,?,?)"
            
            crsr = db.cursor()
            crsr.execute(sql,(user,group,exercise,sets,reps,weight))
            crsr.commit()
            crsr.close()

            self.label_6.setText("Entry for " + (self.comboBox_2.currentText()) + " was registered") #informs user that entry was added
            self.comboBox.setCurrentIndex(0) #reverts combox index to "", so user has to actively change it prior to making another entry


class ViewEx1(QtWidgets.QDialog, Ui_viewex1): # Creates window were user can choose which workout history they would like to inspect
    def __init__(self, parent = None):
        super(ViewEx1, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.viewexcheck)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.comboBox_2.clear) #once again, clears combox to avoid stacking


    def viewexcheck(self): #ensures user fill all boxes, lead to functions that update and show next window
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


class Manager: #Used to easily manage all windows. Some functions where left within specific's window class to avoid over complicating the code
    def __init__(self):

        #Sets up all windows so i can access all windows through Manager
        self.first = Firstwindow()
        self.second = NonRegwindow()
        self.third = Regwindow()
        self.choose = Choose()
        self.measure1 = Measure1()
        self.measure2 = Measure2()
        self.enterex = EnterEx()
        self.viewex1 = ViewEx1()
        self.viewex2 = ViewEx2()
    
        #Here are button press related items. Either to go or update a different screen
        self.first.pushButton.clicked.connect(self.third.show)
        self.first.pushButton_2.clicked.connect(self.first.registerweb)
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


    def openchoice(self): # Passes user's name to all necessary windows. PyQt does not let you access a label unless its not "hiding"
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

    def openmeasure2(self): #function used to open/close measure 1 and 2. Used as proof of concept, These can also be called from the window's classes themselves
        self.measure1.hide()
        self.measure2.show()

    def upmeasure2(self): #updates measure2 window table
        self.measure2.wecur.setText(self.measure1.spinweight.text())
        self.measure2.wacur.setText(self.measure1.spinwaist.text())
        self.measure2.arcur.setText(self.measure1.spinarms.text())
        self.measure2.thcur.setText(self.measure1.spinthighs.text())


    def average(self, n, o, add): #used to calculate average on measure2 window
        userUP = self.measure2.entername_8.text().upper()
        sql = "SELECT username FROM loginfo U WHERE U.Username=?"
        crsr = db.cursor()
        res = crsr.execute(sql, (userUP))
        for row in res:
            ID = (row.__getattribute__('username'))
        crsr.close()
        
        avg = 0
        hm = 0

        sql = "SELECT " + n + " FROM measurement M where M.UserID=?"
        crsr = db.cursor()
        res = crsr.execute(sql, (ID))
        for row in res:
            num = (row.__getattribute__(n))
            hm = hm + float(num)
            avg = avg + 1
        
        resavg = hm / avg
        avgtot = (float(o) - float(resavg))
        avgtotd = "{:.2f}".format(avgtot)
        add(str(avgtotd))

    def initial(self, n, add): #Created a deque so i can retrieve the first ever entry for a specific measurement
        userUP = self.measure2.entername_8.text().upper()
        sql = "SELECT username FROM loginfo U where U.Username=?"
        crsr = db.cursor()
        res = crsr.execute(sql, (userUP))
        for row in res:
            id = (row.__getattribute__('username'))
        crsr.close()

        measure = collections.deque()
        sql = "SELECT " + n + " FROM measurement M WHERE M.UserID=?"
        crsr = db.cursor()
        res = crsr.execute(sql, (id))
        for row in res:
            hm = (row.__getattribute__(n))
            measure.append(hm)

        l = measure.popleft()
        add(str(l))

    def UpdateComBox(self): #updates combobox entries so user does not have to retype/minimizes risk of user mistyping a workout they have already done
        self.enterex.comboBox_2.clear()
        user = self.enterex.entername.text()
        group = self.enterex.comboBox.currentText()
        items = []
        sql = "SELECT exercise FROM exercises e where e.musgroup=? and e.UserID=?"
        crsr = db.cursor()
        res = crsr.execute(sql, (group,user))
        for row in res:
            ans = (row.__getattribute__("exercise"))
            if ans not in items:
                items.append(ans)
        self.enterex.comboBox_2.addItems(items)
        self.enterex.comboBox_2.setCurrentIndex(0)
    

  
    def UpdateComBox2(self): #updates combobox 2 with all workouts for a specific muscle group based on combobox 1.
        self.viewex1.comboBox_2.clear()
        user = self.viewex1.entername.text()
        group = self.viewex1.comboBox.currentText()
        items = []
        sql = "SELECT exercise FROM exercises e where e.musgroup=? and e.UserID=?"
        crsr = db.cursor()
        res = crsr.execute(sql, (group,user))
        for row in res:
            ans = (row.__getattribute__("exercise"))
            if ans not in items:
                items.append(ans)
        self.viewex1.comboBox_2.addItems(items)
        self.viewex1.comboBox_2.setCurrentIndex(0)

      

    def UpdateViewEx2(self): #Used to update items in viewex2 window. Reads items in the file, create objects under a class and then retrieves their info
        user = self.viewex1.entername.text()
        exer = self.viewex1.comboBox_2.currentText()
        sql = 'SELECT * FROM exercises e WHERE e.userID=? AND e.exercise=?'
        crsr = db.cursor()
        res = crsr.execute(sql,(user,exer))
        musclist = []
        for row in res:
            sets = row.__getattribute__('sets')
            reps = row.__getattribute__('reps')
            weight = row.__getattribute__('weight')
            musc = MuscleGroup(sets,reps,weight)
            musclist.append(musc)
        crsr.close()
      

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

        for item in musclist:
            x = "Sets: " + str(item.sets) + "    |   Reps: " + str(item.reps) + "    |   Weight: " + str(item.weight) + "\n"
            self.viewex2.textBrowser.append(x)
    
     

if __name__ == '__main__':
    import sys
    connect = 'DRIVER={MySQL ODBC 8.0 Unicode Driver}; SERVER=fittracker2.cx4y93gaxeqj.us-west-2.rds.amazonaws.com; PORT=3306; DATABASE=nice; UID=admin; PASSWORD=AVjtUqkbVOJRzeOQGAAh;'
    db = pyodbc.connect(connect)
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())