# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created: Sun Sep 10 11:23:28 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inventoryWindow(object):
    def setupUi(self, inventoryWindow):
        inventoryWindow.setObjectName("inventoryWindow")
        inventoryWindow.resize(1164, 672)
        inventoryWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"")
        self.centralwidget = QtWidgets.QWidget(inventoryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setHorizontalSpacing(14)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.partImage = QtWidgets.QLabel(self.centralwidget)
        self.partImage.setMaximumSize(QtCore.QSize(130, 130))
        self.partImage.setText("")
        self.partImage.setPixmap(QtGui.QPixmap("images/atmega328.jpg"))
        self.partImage.setScaledContents(True)
        self.partImage.setObjectName("partImage")
        self.gridLayout.addWidget(self.partImage, 3, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.partName = QtWidgets.QLabel(self.centralwidget)
        self.partName.setStyleSheet("font: 20pt \"Noto Sans\";")
        self.partName.setObjectName("partName")
        self.gridLayout.addWidget(self.partName, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.partQty = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partQty.setFont(font)
        self.partQty.setObjectName("partQty")
        self.gridLayout.addWidget(self.partQty, 8, 1, 1, 1)
        self.partCategory = QtWidgets.QLabel(self.centralwidget)
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
        self.addToCartButton = QtWidgets.QPushButton(self.centralwidget)
        self.addToCartButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addToCartButton.setObjectName("addToCartButton")
        self.gridLayout.addWidget(self.addToCartButton, 9, 0, 1, 1)
        self.partBox = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partBox.setFont(font)
        self.partBox.setObjectName("partBox")
        self.gridLayout.addWidget(self.partBox, 7, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.partShelf = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partShelf.setFont(font)
        self.partShelf.setObjectName("partShelf")
        self.gridLayout.addWidget(self.partShelf, 6, 1, 1, 1)
        self.cartButton = QtWidgets.QPushButton(self.centralwidget)
        self.cartButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cartButton.setObjectName("cartButton")
        self.gridLayout.addWidget(self.cartButton, 10, 0, 1, 2)
        self.qtySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtySpinBox.sizePolicy().hasHeightForWidth())
        self.qtySpinBox.setSizePolicy(sizePolicy)
        self.qtySpinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.qtySpinBox.setStyleSheet("")
        self.qtySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.qtySpinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.qtySpinBox.setObjectName("qtySpinBox")
        self.gridLayout.addWidget(self.qtySpinBox, 9, 1, 1, 1)
        self.partID = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partID.setFont(font)
        self.partID.setObjectName("partID")
        self.gridLayout.addWidget(self.partID, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 2)
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridLayout.addWidget(self.descriptionLabel, 4, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.categoryView = QtWidgets.QListView(self.centralwidget)
        self.categoryView.setMinimumSize(QtCore.QSize(350, 0))
        self.categoryView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.categoryView.setAlternatingRowColors(True)
        self.categoryView.setObjectName("categoryView")
        self.gridLayout_2.addWidget(self.categoryView, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.itemListView = QtWidgets.QListView(self.centralwidget)
        self.itemListView.setMinimumSize(QtCore.QSize(350, 0))
        self.itemListView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.itemListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.itemListView.setAlternatingRowColors(True)
        self.itemListView.setObjectName("itemListView")
        self.gridLayout_2.addWidget(self.itemListView, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 4)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 1, 1, 1, 1)
        inventoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(inventoryWindow)
        QtCore.QMetaObject.connectSlotsByName(inventoryWindow)
        inventoryWindow.setTabOrder(self.categoryView, self.itemListView)
        inventoryWindow.setTabOrder(self.itemListView, self.addToCartButton)
        inventoryWindow.setTabOrder(self.addToCartButton, self.cartButton)
        inventoryWindow.setTabOrder(self.cartButton, self.qtySpinBox)

    def retranslateUi(self, inventoryWindow):
        _translate = QtCore.QCoreApplication.translate
        inventoryWindow.setWindowTitle(_translate("inventoryWindow", "MainWindow"))
        self.partName.setText(_translate("inventoryWindow", "ATMega328"))
        self.partQty.setText(_translate("inventoryWindow", "5"))
        self.partCategory.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Microcontroller</span></p></body></html>"))
        self.addToCartButton.setText(_translate("inventoryWindow", "Add to Cart"))
        self.partBox.setText(_translate("inventoryWindow", "5"))
        self.label_12.setText(_translate("inventoryWindow", "Available Quantity"))
        self.partShelf.setText(_translate("inventoryWindow", "3"))
        self.cartButton.setText(_translate("inventoryWindow", "View Cart"))
        self.partID.setText(_translate("inventoryWindow", "035"))
        self.label_4.setText(_translate("inventoryWindow", "Shelf"))
        self.label_5.setText(_translate("inventoryWindow", "Box"))
        self.label_3.setText(_translate("inventoryWindow", "ID"))
        self.descriptionLabel.setText(_translate("inventoryWindow", "Description"))
        self.label_6.setText(_translate("inventoryWindow", "Category"))
        self.label_2.setText(_translate("inventoryWindow", "Inventory Browser"))
        self.label_7.setText(_translate("inventoryWindow", "Item"))

