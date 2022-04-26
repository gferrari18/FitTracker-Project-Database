from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Choose(object):
    def setupUi(self, Choose):
        Choose.setObjectName("Choose")
        Choose.resize(729, 182)
        self.entername = QtWidgets.QLabel(Choose)
        self.entername.setGeometry(QtCore.QRect(70, 20, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setKerning(False)
        self.entername.setFont(font)
        self.entername.setAlignment(QtCore.Qt.AlignCenter)
        self.entername.setObjectName("entername")
        self.pushButton = QtWidgets.QPushButton(Choose)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(Choose)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 49, 731, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Choose)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 100, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Choose)
        QtCore.QMetaObject.connectSlotsByName(Choose)

    def retranslateUi(self, Choose):
        _translate = QtCore.QCoreApplication.translate
        Choose.setWindowTitle(_translate("Choose", "Dialog"))
        self.entername.setText(_translate("Choose", "Choose an option:"))
        self.pushButton.setText(_translate("Choose", "Measurements"))
        self.pushButton_2.setText(_translate("Choose", "Workouts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Choose = QtWidgets.QDialog()
    ui = Ui_Choose()
    ui.setupUi(Choose)
    Choose.show()
    sys.exit(app.exec_())
