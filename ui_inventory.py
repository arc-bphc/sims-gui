# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
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

class Ui_inventoryWindow(object):
    def setupUi(self, inventoryWindow):
        inventoryWindow.setObjectName(_fromUtf8("inventoryWindow"))
        inventoryWindow.resize(1164, 672)
        inventoryWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.centralwidget = QtGui.QWidget(inventoryWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(107, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setHorizontalSpacing(14)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.partImage = QtGui.QLabel(self.centralwidget)
        self.partImage.setMaximumSize(QtCore.QSize(130, 130))
        self.partImage.setText(_fromUtf8(""))
        self.partImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/atmega328.jpg")))
        self.partImage.setScaledContents(True)
        self.partImage.setObjectName(_fromUtf8("partImage"))
        self.gridLayout.addWidget(self.partImage, 3, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.partName = QtGui.QLabel(self.centralwidget)
        self.partName.setStyleSheet(_fromUtf8("font: 20pt \"Noto Sans\";"))
        self.partName.setObjectName(_fromUtf8("partName"))
        self.gridLayout.addWidget(self.partName, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.partQty = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partQty.setFont(font)
        self.partQty.setObjectName(_fromUtf8("partQty"))
        self.gridLayout.addWidget(self.partQty, 8, 1, 1, 1)
        self.partCategory = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.partCategory.setFont(font)
        self.partCategory.setStyleSheet(_fromUtf8("font: italic 16pt \"Noto Sans\";"))
        self.partCategory.setObjectName(_fromUtf8("partCategory"))
        self.gridLayout.addWidget(self.partCategory, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.addToCartButton = QtGui.QPushButton(self.centralwidget)
        self.addToCartButton.setObjectName(_fromUtf8("addToCartButton"))
        self.gridLayout.addWidget(self.addToCartButton, 9, 0, 1, 1)
        self.partBox = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partBox.setFont(font)
        self.partBox.setObjectName(_fromUtf8("partBox"))
        self.gridLayout.addWidget(self.partBox, 7, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.partShelf = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partShelf.setFont(font)
        self.partShelf.setObjectName(_fromUtf8("partShelf"))
        self.gridLayout.addWidget(self.partShelf, 6, 1, 1, 1)
        self.cartButton = QtGui.QPushButton(self.centralwidget)
        self.cartButton.setObjectName(_fromUtf8("cartButton"))
        self.gridLayout.addWidget(self.cartButton, 10, 0, 1, 2)
        self.qtySpinBox = QtGui.QSpinBox(self.centralwidget)
        self.qtySpinBox.setMinimumSize(QtCore.QSize(0, 45))
        self.qtySpinBox.setObjectName(_fromUtf8("qtySpinBox"))
        self.gridLayout.addWidget(self.qtySpinBox, 9, 1, 1, 1)
        self.partID = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partID.setFont(font)
        self.partID.setObjectName(_fromUtf8("partID"))
        self.gridLayout.addWidget(self.partID, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setStyleSheet(_fromUtf8("font: 16pt \"Noto Sans\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.categoryView = QtGui.QListView(self.centralwidget)
        self.categoryView.setMinimumSize(QtCore.QSize(350, 0))
        self.categoryView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.categoryView.setAlternatingRowColors(True)
        self.categoryView.setObjectName(_fromUtf8("categoryView"))
        self.gridLayout_2.addWidget(self.categoryView, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setStyleSheet(_fromUtf8("font: 24pt \"Noto Sans\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.itemListView = QtGui.QListView(self.centralwidget)
        self.itemListView.setMinimumSize(QtCore.QSize(350, 0))
        self.itemListView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.itemListView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.itemListView.setAlternatingRowColors(True)
        self.itemListView.setObjectName(_fromUtf8("itemListView"))
        self.gridLayout_2.addWidget(self.itemListView, 3, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 4)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setStyleSheet(_fromUtf8("font: 16pt \"Noto Sans\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(107, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 1, 1, 1, 1)
        inventoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(inventoryWindow)
        QtCore.QMetaObject.connectSlotsByName(inventoryWindow)

    def retranslateUi(self, inventoryWindow):
        inventoryWindow.setWindowTitle(_translate("inventoryWindow", "MainWindow", None))
        self.partName.setText(_translate("inventoryWindow", "ATMega328", None))
        self.partQty.setText(_translate("inventoryWindow", "5", None))
        self.partCategory.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Microcontroller</span></p></body></html>", None))
        self.addToCartButton.setText(_translate("inventoryWindow", "Add to Cart", None))
        self.partBox.setText(_translate("inventoryWindow", "5", None))
        self.label_12.setText(_translate("inventoryWindow", "Available Quantity", None))
        self.partShelf.setText(_translate("inventoryWindow", "3", None))
        self.cartButton.setText(_translate("inventoryWindow", "View Cart", None))
        self.partID.setText(_translate("inventoryWindow", "035", None))
        self.label_4.setText(_translate("inventoryWindow", "Shelf", None))
        self.label_5.setText(_translate("inventoryWindow", "Box", None))
        self.label_3.setText(_translate("inventoryWindow", "ID", None))
        self.label_6.setText(_translate("inventoryWindow", "Category", None))
        self.label_2.setText(_translate("inventoryWindow", "Inventory Browser", None))
        self.label_7.setText(_translate("inventoryWindow", "Item", None))

