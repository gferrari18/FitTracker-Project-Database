# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measure1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_measure1(object):
    def setupUi(self, measure1):
        measure1.setObjectName("measure1")
        measure1.resize(800, 700)
        self.entername = QtWidgets.QLabel(measure1)
        self.entername.setGeometry(QtCore.QRect(10, 30, 781, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setKerning(False)
        self.entername.setFont(font)
        self.entername.setAlignment(QtCore.Qt.AlignCenter)
        self.entername.setObjectName("entername")
        self.horizontalLayoutWidget = QtWidgets.QWidget(measure1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 141, 591))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.entername_2 = QtWidgets.QLabel(measure1)
        self.entername_2.setGeometry(QtCore.QRect(140, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setKerning(False)
        self.entername_2.setFont(font)
        self.entername_2.setAlignment(QtCore.Qt.AlignCenter)
        self.entername_2.setObjectName("entername_2")
        self.entername_3 = QtWidgets.QLabel(measure1)
        self.entername_3.setGeometry(QtCore.QRect(140, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setKerning(False)
        self.entername_3.setFont(font)
        self.entername_3.setAlignment(QtCore.Qt.AlignCenter)
        self.entername_3.setObjectName("entername_3")
        self.entername_4 = QtWidgets.QLabel(measure1)
        self.entername_4.setGeometry(QtCore.QRect(140, 270, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setKerning(False)
        self.entername_4.setFont(font)
        self.entername_4.setAlignment(QtCore.Qt.AlignCenter)
        self.entername_4.setObjectName("entername_4")
        self.entername_5 = QtWidgets.QLabel(measure1)
        self.entername_5.setGeometry(QtCore.QRect(140, 350, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setKerning(False)
        self.entername_5.setFont(font)
        self.entername_5.setAlignment(QtCore.Qt.AlignCenter)
        self.entername_5.setObjectName("entername_5")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(measure1)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 150, 661, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(measure1)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(140, 230, 661, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(measure1)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(140, 310, 661, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(measure1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(420, 110, 241, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinweight = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinweight.setMaximum(10000.0)
        self.spinweight.setSingleStep(0.5)
        self.spinweight.setObjectName("spinweight")
        self.verticalLayout.addWidget(self.spinweight)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(measure1)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(420, 190, 241, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spinwaist = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.spinwaist.setMaximum(10000.0)
        self.spinwaist.setSingleStep(0.5)
        self.spinwaist.setObjectName("spinwaist")
        self.verticalLayout_2.addWidget(self.spinwaist)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(measure1)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(420, 270, 241, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spinarms = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.spinarms.setMaximum(10000.0)
        self.spinarms.setSingleStep(0.5)
        self.spinarms.setObjectName("spinarms")
        self.verticalLayout_3.addWidget(self.spinarms)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(measure1)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(420, 350, 241, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.spinthighs = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.spinthighs.setMaximum(10000.0)
        self.spinthighs.setSingleStep(0.5)
        self.spinthighs.setObjectName("spinthighs")
        self.verticalLayout_4.addWidget(self.spinthighs)
        self.pushButton = QtWidgets.QPushButton(measure1)
        self.pushButton.setGeometry(QtCore.QRect(160, 490, 181, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(measure1)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 490, 181, 61))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(measure1)
        QtCore.QMetaObject.connectSlotsByName(measure1)

    def retranslateUi(self, measure1):
        _translate = QtCore.QCoreApplication.translate
        measure1.setWindowTitle(_translate("measure1", "Dialog"))
        self.entername.setText(_translate("measure1", "Enter measurements using numbers:"))
        self.entername_2.setText(_translate("measure1", "Weight"))
        self.entername_3.setText(_translate("measure1", "Waist"))
        self.entername_4.setText(_translate("measure1", "Arms(Avg.)"))
        self.entername_5.setText(_translate("measure1", "Thighs(Avg.)"))
        self.pushButton.setText(_translate("measure1", "Submit"))
        self.pushButton_2.setText(_translate("measure1", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    measure1 = QtWidgets.QDialog()
    ui = Ui_measure1()
    ui.setupUi(measure1)
    measure1.show()
    sys.exit(app.exec_())