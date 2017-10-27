# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finger.ui'
#
# Created: Fri Oct 27 21:04:10 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.setEnabled(True)
        loginWindow.resize(977, 708)
        loginWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(loginWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(loginWindow)
        self.label_2.setMaximumSize(QtCore.QSize(400, 160))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/12967978_719298328212453_6846422403842474807_o.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.fingerLabel = QtWidgets.QLabel(loginWindow)
        self.fingerLabel.setMaximumSize(QtCore.QSize(320, 240))
        self.fingerLabel.setText("")
        self.fingerLabel.setPixmap(QtGui.QPixmap("images/finger-scan.gif"))
        self.fingerLabel.setScaledContents(True)
        self.fingerLabel.setObjectName("fingerLabel")
        self.verticalLayout.addWidget(self.fingerLabel, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(loginWindow)
        self.label_3.setStyleSheet("font: 75 18pt \"Noto Sans\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.label_3.setText(_translate("loginWindow", "Place your finger on the sensor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

