# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enrolfingerprint.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(enrolFingerWindow)
        self.label_5.setStyleSheet("font: 75 18pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(enrolFingerWindow)
        self.label_3.setMaximumSize(QtCore.QSize(320, 240))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/finger-scan.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(enrolFingerWindow)
        self.label_4.setMaximumSize(QtCore.QSize(320, 240))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/finger-scan.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(enrolFingerWindow)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(enrolFingerWindow)
        self.label_2.setMaximumSize(QtCore.QSize(400, 160))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/12967978_719298328212453_6846422403842474807_o.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(enrolFingerWindow)
        self.label.setMaximumSize(QtCore.QSize(320, 240))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/finger-scan.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 2, 1, 1)

        self.retranslateUi(enrolFingerWindow)
        QtCore.QMetaObject.connectSlotsByName(enrolFingerWindow)

    def retranslateUi(self, enrolFingerWindow):
        _translate = QtCore.QCoreApplication.translate
        enrolFingerWindow.setWindowTitle(_translate("enrolFingerWindow", "Form"))
        self.label_5.setText(_translate("enrolFingerWindow", "Place your finger on the sensor (1/3)"))
        self.pushButton.setText(_translate("enrolFingerWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    enrolFingerWindow = QtWidgets.QWidget()
    ui = Ui_enrolFingerWindow()
    ui.setupUi(enrolFingerWindow)
    enrolFingerWindow.show()
    sys.exit(app.exec_())

