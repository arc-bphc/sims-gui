# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enrol.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_enrolWindow(object):
    def setupUi(self, enrolWindow):
        enrolWindow.setObjectName("enrolWindow")
        enrolWindow.resize(1015, 595)
        enrolWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(enrolWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(enrolWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.buttonBox = QtWidgets.QDialogButtonBox(enrolWindow)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.roomNumber = QtWidgets.QLineEdit(enrolWindow)
        self.roomNumber.setObjectName("roomNumber")
        self.gridLayout_2.addWidget(self.roomNumber, 4, 1, 1, 1)
        self.phoneCall = QtWidgets.QLineEdit(enrolWindow)
        self.phoneCall.setObjectName("phoneCall")
        self.gridLayout_2.addWidget(self.phoneCall, 2, 1, 1, 1)
        self.name = QtWidgets.QLineEdit(enrolWindow)
        self.name.setEnabled(True)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(enrolWindow)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(enrolWindow)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 5, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(enrolWindow)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.phoneWhatsApp = QtWidgets.QLineEdit(enrolWindow)
        self.phoneWhatsApp.setObjectName("phoneWhatsApp")
        self.gridLayout_2.addWidget(self.phoneWhatsApp, 3, 1, 1, 1)
        self.pin = QtWidgets.QLineEdit(enrolWindow)
        self.pin.setMaxLength(4)
        self.pin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pin.setObjectName("pin")
        self.gridLayout_2.addWidget(self.pin, 6, 1, 1, 1)
        self.email = QtWidgets.QLineEdit(enrolWindow)
        self.email.setObjectName("email")
        self.gridLayout_2.addWidget(self.email, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(enrolWindow)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(enrolWindow)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(enrolWindow)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(enrolWindow)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)

        self.retranslateUi(enrolWindow)
        QtCore.QMetaObject.connectSlotsByName(enrolWindow)
        enrolWindow.setTabOrder(self.name, self.email)
        enrolWindow.setTabOrder(self.email, self.phoneCall)
        enrolWindow.setTabOrder(self.phoneCall, self.phoneWhatsApp)
        enrolWindow.setTabOrder(self.phoneWhatsApp, self.roomNumber)
        enrolWindow.setTabOrder(self.roomNumber, self.pin)

    def retranslateUi(self, enrolWindow):
        _translate = QtCore.QCoreApplication.translate
        enrolWindow.setWindowTitle(_translate("enrolWindow", "Form"))
        self.label_5.setText(_translate("enrolWindow", "Enrol User"))
        self.label_7.setText(_translate("enrolWindow", "Phone (Calling)"))
        self.label_9.setText(_translate("enrolWindow", "Name"))
        self.label_8.setText(_translate("enrolWindow", "Phone (WhatsApp)"))
        self.label_10.setText(_translate("enrolWindow", "Room Number"))
        self.label_2.setText(_translate("enrolWindow", "PIN"))
        self.label_6.setText(_translate("enrolWindow", "Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    enrolWindow = QtWidgets.QWidget()
    ui = Ui_enrolWindow()
    ui.setupUi(enrolWindow)
    enrolWindow.show()
    sys.exit(app.exec_())

