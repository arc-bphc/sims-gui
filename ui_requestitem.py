# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'requestitem.ui'
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

class Ui_requestItemWindow(object):
    def setupUi(self, requestItemWindow):
        requestItemWindow.setObjectName(_fromUtf8("requestItemWindow"))
        requestItemWindow.resize(1119, 629)
        requestItemWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
""))
        self.gridLayout_3 = QtGui.QGridLayout(requestItemWindow)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 3)
        self.project = QtGui.QLineEdit(requestItemWindow)
        self.project.setObjectName(_fromUtf8("project"))
        self.gridLayout_2.addWidget(self.project, 0, 3, 1, 1)
        self.item = QtGui.QLineEdit(requestItemWindow)
        self.item.setObjectName(_fromUtf8("item"))
        self.gridLayout_2.addWidget(self.item, 1, 3, 1, 1)
        self.price = QtGui.QLineEdit(requestItemWindow)
        self.price.setObjectName(_fromUtf8("price"))
        self.gridLayout_2.addWidget(self.price, 2, 3, 1, 1)
        self.label_7 = QtGui.QLabel(requestItemWindow)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(requestItemWindow)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(requestItemWindow)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(requestItemWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 4, 1, 1, 3, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.label = QtGui.QLabel(requestItemWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 24pt \"Noto Sans\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 1, 1, 1, 1)

        self.retranslateUi(requestItemWindow)
        QtCore.QMetaObject.connectSlotsByName(requestItemWindow)

    def retranslateUi(self, requestItemWindow):
        requestItemWindow.setWindowTitle(_translate("requestItemWindow", "Form", None))
        self.label_7.setText(_translate("requestItemWindow", "Price", None))
        self.label_5.setText(_translate("requestItemWindow", "Project", None))
        self.label_6.setText(_translate("requestItemWindow", "Item", None))
        self.label.setText(_translate("requestItemWindow", "Purchase Request Form", None))

