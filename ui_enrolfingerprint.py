# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enrolfingerprint.ui'
#
# Created: Fri Oct 20 15:54:54 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_enrolFingerWindow(object):
    def setupUi(self, enrolFingerWindow):
        enrolFingerWindow.setObjectName("enrolFingerWindow")
        enrolFingerWindow.resize(1115, 819)
        enrolFingerWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(enrolFingerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        self.fprint1 = QtWidgets.QLabel(enrolFingerWindow)
        self.fprint1.setMaximumSize(QtCore.QSize(320, 240))
        self.fprint1.setText("")
        self.fprint1.setPixmap(QtGui.QPixmap("images/finger-scan.gif"))
        self.fprint1.setScaledContents(True)
        self.fprint1.setObjectName("fprint1")
        self.gridLayout.addWidget(self.fprint1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)
        self.fprint3 = QtWidgets.QLabel(enrolFingerWindow)
        self.fprint3.setMaximumSize(QtCore.QSize(320, 240))
        self.fprint3.setText("")
        self.fprint3.setPixmap(QtGui.QPixmap("images/finger-scan.gif"))
        self.fprint3.setScaledContents(True)
        self.fprint3.setObjectName("fprint3")
        self.gridLayout.addWidget(self.fprint3, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 4, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(enrolFingerWindow)
        self.label_5.setStyleSheet("font: 75 18pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 5, QtCore.Qt.AlignHCenter)
        self.fprint2 = QtWidgets.QLabel(enrolFingerWindow)
        self.fprint2.setMaximumSize(QtCore.QSize(320, 240))
        self.fprint2.setText("")
        self.fprint2.setPixmap(QtGui.QPixmap("images/finger-scan.gif"))
        self.fprint2.setScaledContents(True)
        self.fprint2.setObjectName("fprint2")
        self.gridLayout.addWidget(self.fprint2, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 6, 2, 1, 1)
        self.exitButton = QtWidgets.QPushButton(enrolFingerWindow)
        self.exitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 5, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.retranslateUi(enrolFingerWindow)
        QtCore.QMetaObject.connectSlotsByName(enrolFingerWindow)

    def retranslateUi(self, enrolFingerWindow):
        _translate = QtCore.QCoreApplication.translate
        enrolFingerWindow.setWindowTitle(_translate("enrolFingerWindow", "Form"))
        self.label_5.setText(_translate("enrolFingerWindow", "Place your finger on the sensor (1/3)"))
        self.exitButton.setText(_translate("enrolFingerWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    enrolFingerWindow = QtWidgets.QWidget()
    ui = Ui_enrolFingerWindow()
    ui.setupUi(enrolFingerWindow)
    enrolFingerWindow.show()
    sys.exit(app.exec_())

