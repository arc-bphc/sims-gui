# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cart.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cartWindow(object):
    def setupUi(self, cartWindow):
        cartWindow.setObjectName("cartWindow")
        cartWindow.resize(1094, 795)
        cartWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"\\")
        self.gridLayout_3 = QtWidgets.QGridLayout(cartWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.partName = QtWidgets.QLabel(cartWindow)
        self.partName.setStyleSheet("font: 20pt \"Noto Sans\";")
        self.partName.setObjectName("partName")
        self.gridLayout.addWidget(self.partName, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.removeCartButton = QtWidgets.QPushButton(cartWindow)
        self.removeCartButton.setObjectName("removeCartButton")
        self.gridLayout.addWidget(self.removeCartButton, 9, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.partID = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partID.setFont(font)
        self.partID.setObjectName("partID")
        self.gridLayout.addWidget(self.partID, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.partShelf = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partShelf.setFont(font)
        self.partShelf.setObjectName("partShelf")
        self.gridLayout.addWidget(self.partShelf, 6, 1, 1, 1)
        self.partQty = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partQty.setFont(font)
        self.partQty.setObjectName("partQty")
        self.gridLayout.addWidget(self.partQty, 8, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.partBox = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partBox.setFont(font)
        self.partBox.setObjectName("partBox")
        self.gridLayout.addWidget(self.partBox, 7, 1, 1, 1)
        self.partCategory = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.partCategory.setFont(font)
        self.partCategory.setStyleSheet("font: italic 16pt \"Noto Sans\";")
        self.partCategory.setObjectName("partCategory")
        self.gridLayout.addWidget(self.partCategory, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.partImage = QtWidgets.QLabel(cartWindow)
        self.partImage.setMaximumSize(QtCore.QSize(130, 130))
        self.partImage.setText("")
        self.partImage.setPixmap(QtGui.QPixmap("images/atmega328.jpg"))
        self.partImage.setScaledContents(True)
        self.partImage.setObjectName("partImage")
        self.gridLayout.addWidget(self.partImage, 3, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.openInventory = QtWidgets.QPushButton(cartWindow)
        self.openInventory.setObjectName("openInventory")
        self.gridLayout.addWidget(self.openInventory, 10, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 2, 1, 1)
        self.listView = QtWidgets.QListView(cartWindow)
        self.listView.setMinimumSize(QtCore.QSize(500, 0))
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setAlternatingRowColors(True)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(cartWindow)
        self.label_6.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 1, 1, 1, 1)

        self.retranslateUi(cartWindow)
        QtCore.QMetaObject.connectSlotsByName(cartWindow)
        cartWindow.setTabOrder(self.listView, self.removeCartButton)
        cartWindow.setTabOrder(self.removeCartButton, self.openInventory)

    def retranslateUi(self, cartWindow):
        _translate = QtCore.QCoreApplication.translate
        cartWindow.setWindowTitle(_translate("cartWindow", "Form"))
        self.partName.setText(_translate("cartWindow", "ATMega32U4"))
        self.label_12.setText(_translate("cartWindow", "Quantity"))
        self.removeCartButton.setText(_translate("cartWindow", "Remove From Cart"))
        self.label_3.setText(_translate("cartWindow", "ID"))
        self.partID.setText(_translate("cartWindow", "035"))
        self.label_5.setText(_translate("cartWindow", "Box"))
        self.partShelf.setText(_translate("cartWindow", "3"))
        self.partQty.setText(_translate("cartWindow", "2"))
        self.label_4.setText(_translate("cartWindow", "Shelf"))
        self.partBox.setText(_translate("cartWindow", "5"))
        self.partCategory.setText(_translate("cartWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Microcontroller</span></p></body></html>"))
        self.openInventory.setText(_translate("cartWindow", "Inventory"))
        self.label_2.setText(_translate("cartWindow", "Cart"))
        self.label_6.setText(_translate("cartWindow", "Item"))

