# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewex1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewex1(object):
    def setupUi(self, viewex1):
        viewex1.setObjectName("viewex1")
        viewex1.resize(600, 400)
        self.comboBox = QtWidgets.QComboBox(viewex1)
        self.comboBox.setGeometry(QtCore.QRect(300, 130, 131, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(viewex1)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 170, 141, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(viewex1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 120, 141, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox_2 = QtWidgets.QComboBox(viewex1)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 180, 131, 22))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.entername = QtWidgets.QLabel(viewex1)
        self.entername.setGeometry(QtCore.QRect(110, 50, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setKerning(False)
        self.entername.setFont(font)
        self.entername.setText("")
        self.entername.setAlignment(QtCore.Qt.AlignCenter)
        self.entername.setObjectName("entername")
        self.pushButton_2 = QtWidgets.QPushButton(viewex1)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 240, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(viewex1)
        self.pushButton.setGeometry(QtCore.QRect(120, 240, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(viewex1)
        self.label_6.setGeometry(QtCore.QRect(120, 330, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(viewex1)
        QtCore.QMetaObject.connectSlotsByName(viewex1)

    def retranslateUi(self, viewex1):
        _translate = QtCore.QCoreApplication.translate
        viewex1.setWindowTitle(_translate("viewex1", "Dialog"))
        self.comboBox.setItemText(1, _translate("viewex1", "Arms"))
        self.comboBox.setItemText(2, _translate("viewex1", "Back"))
        self.comboBox.setItemText(3, _translate("viewex1", "Chest"))
        self.comboBox.setItemText(4, _translate("viewex1", "Legs"))
        self.comboBox.setItemText(5, _translate("viewex1", "Shoulders"))
        self.label_2.setText(_translate("viewex1", "Exercise Name"))
        self.label.setText(_translate("viewex1", "Muscle Group"))
        self.pushButton_2.setText(_translate("viewex1", "Return"))
        self.pushButton.setText(_translate("viewex1", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewex1 = QtWidgets.QDialog()
    ui = Ui_viewex1()
    ui.setupUi(viewex1)
    viewex1.show()
    sys.exit(app.exec_())