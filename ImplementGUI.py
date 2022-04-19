from operator import truediv
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os


class mainwindow(QWidget): #mainwindow will INHERIT everything from QWidget
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.resize(600,200)
        self.setWindowTitle("Weigh Management Software")

        self.label = QLabel(self) #self is the parent
        self.label.setText("Welcome to the Weight Management Software!")
        self.label.move(50,20)

        self.label2 = QLabel(self)
        self.label2.setText("Have you registered before?")
        self.label2.move(50,50)

        self.label3 = QLabel(self)
        self.label3.setText("Please enter your name: ")
        self.label3.move(50,20)
        self.label3.setVisible(False)
        
        self.label4 = QLabel(self)
        self.label4.setText("This name does not seem to be registered.")
        self.label4.move(50,20)
        self.label4.setVisible(False)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label2.setFont(font)
        self.label3.setFont(font)
        self.label4.setFont(font)

       

        self.btn1 = QPushButton(self)
        self.btn1.setText("Yes")
        self.btn1.move(50,100)

        self.btn2 = QPushButton(self)
        self.btn2.setText("No")
        self.btn2.move(150,100)
        
        self.usr = QLineEdit(self)
        self.usr.move(50,60)
        self.usr.setVisible(False)

        self.sbmt = QPushButton(self)
        self.sbmt.setText("Submit")
        self.sbmt.move(50,100)
        self.sbmt.setVisible(False)
        

        self.back = QPushButton(self)
        self.back.setText("Back")
        self.back.move(150,100)
        self.back.setVisible(False)


        self.btn2.clicked.connect(self.User)
        self.btn1.clicked.connect(self.User)
        self.back.clicked.connect(self.restart)
        self.sbmt.clicked.connect(self.getname)


    def User(self):
        self.usr.setVisible(True)
        self.label.setVisible(False)
        self.label2.setVisible(False)
        self.btn1.setVisible(False)
        self.btn2.setVisible(False)
        self.label3.setVisible(True)
        self.sbmt.setVisible(True)
        self.back.setVisible(True)

    def restart(self):
        self.usr.setVisible(False)
        self.label.setVisible(True)
        self.label2.setVisible(True)
        self.btn1.setVisible(True)
        self.btn2.setVisible(True)
        self.label3.setVisible(False)
        self.sbmt.setVisible(False)
        self.back.setVisible(False)
    
    def getname(self):
        name = self.usr.text()
        nameUP = name.upper()
        f = open(nameUP + ".txt", "a") #if start with "r", will give an error if file does not exist
        f.close()
        f = open(nameUP + ".txt", "r")
        if f.readline() == "": #
            self.label3.setVisible(False)
            self.label4.setVisible(True)
            f.close()
            os.remove(nameUP + ".txt")
        else: 
            self.label3.setVisible(False)
            self.label4 = QLabel(self)
            self.label4.setText("Welcome back, " + name)
            self.label4.move(50,20)
        f.close()


             


def main():
    app = QApplication(sys.argv)
    w = mainwindow()
    w.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    main()