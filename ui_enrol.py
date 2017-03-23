# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enrol.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_enrolWindow(object):
    def setupUi(self, enrolWindow):
        enrolWindow.setObjectName(_fromUtf8("enrolWindow"))
        enrolWindow.resize(1015, 595)
        enrolWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.gridLayout_3 = QtGui.QGridLayout(enrolWindow)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(enrolWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(_fromUtf8("font: 24pt \"Noto Sans\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.buttonBox = QtGui.QDialogButtonBox(enrolWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit_2 = QtGui.QLineEdit(enrolWindow)
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 7, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(enrolWindow)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(enrolWindow)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 7, 0, 1, 1)
        self.label_7 = QtGui.QLabel(enrolWindow)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.phoneCall = QtGui.QLineEdit(enrolWindow)
        self.phoneCall.setObjectName(_fromUtf8("phoneCall"))
        self.gridLayout_2.addWidget(self.phoneCall, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(enrolWindow)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(enrolWindow)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.email = QtGui.QLineEdit(enrolWindow)
        self.email.setObjectName(_fromUtf8("email"))
        self.gridLayout_2.addWidget(self.email, 2, 1, 1, 1)
        self.name = QtGui.QLineEdit(enrolWindow)
        self.name.setEnabled(True)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout_2.addWidget(self.name, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(enrolWindow)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.phoneWhatsApp = QtGui.QLineEdit(enrolWindow)
        self.phoneWhatsApp.setObjectName(_fromUtf8("phoneWhatsApp"))
        self.gridLayout_2.addWidget(self.phoneWhatsApp, 4, 1, 1, 1)
        self.label_10 = QtGui.QLabel(enrolWindow)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.roomNumber = QtGui.QLineEdit(enrolWindow)
        self.roomNumber.setObjectName(_fromUtf8("roomNumber"))
        self.gridLayout_2.addWidget(self.roomNumber, 5, 1, 1, 1)
        self.label = QtGui.QLabel(enrolWindow)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.line = QtGui.QFrame(enrolWindow)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)

        self.retranslateUi(enrolWindow)
        QtCore.QMetaObject.connectSlotsByName(enrolWindow)

    def retranslateUi(self, enrolWindow):
        enrolWindow.setWindowTitle(_translate("enrolWindow", "Form", None))
        self.label_5.setText(_translate("enrolWindow", "Enrol User", None))
        self.label_2.setText(_translate("enrolWindow", "PIN", None))
        self.label_7.setText(_translate("enrolWindow", "Phone (Calling)", None))
        self.label_8.setText(_translate("enrolWindow", "Phone (WhatsApp)", None))
        self.label_6.setText(_translate("enrolWindow", "Email", None))
        self.label_9.setText(_translate("enrolWindow", "Name", None))
        self.label_10.setText(_translate("enrolWindow", "Room Number", None))
        self.label.setText(_translate("enrolWindow", "User ID", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    enrolWindow = QtGui.QWidget()
    ui = Ui_enrolWindow()
    ui.setupUi(enrolWindow)
    enrolWindow.show()
    sys.exit(app.exec_())

