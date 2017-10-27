# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'requestitem.ui'
#
# Created: Fri Oct 27 14:43:58 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_requestItemWindow(object):
    def setupUi(self, requestItemWindow):
        requestItemWindow.setObjectName("requestItemWindow")
        requestItemWindow.resize(1119, 629)
        requestItemWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(requestItemWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.project = QtWidgets.QLineEdit(requestItemWindow)
        self.project.setObjectName("project")
        self.gridLayout_2.addWidget(self.project, 0, 3, 1, 1)
        self.item = QtWidgets.QLineEdit(requestItemWindow)
        self.item.setObjectName("item")
        self.gridLayout_2.addWidget(self.item, 1, 3, 1, 1)
        self.price = QtWidgets.QLineEdit(requestItemWindow)
        self.price.setObjectName("price")
        self.gridLayout_2.addWidget(self.price, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(requestItemWindow)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(requestItemWindow)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(requestItemWindow)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(requestItemWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(requestItemWindow)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(requestItemWindow)
        QtCore.QMetaObject.connectSlotsByName(requestItemWindow)

    def retranslateUi(self, requestItemWindow):
        _translate = QtCore.QCoreApplication.translate
        requestItemWindow.setWindowTitle(_translate("requestItemWindow", "Form"))
        self.label_7.setText(_translate("requestItemWindow", "Price"))
        self.label_5.setText(_translate("requestItemWindow", "Project"))
        self.label_6.setText(_translate("requestItemWindow", "Item"))
        self.label.setText(_translate("requestItemWindow", "Purchase Request Form"))

