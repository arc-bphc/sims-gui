# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created: Mon Jan  1 13:39:44 2018
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cartButton = QtWidgets.QPushButton(self.centralwidget)
        self.cartButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cartButton.setObjectName("cartButton")
        self.horizontalLayout_3.addWidget(self.cartButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setHorizontalSpacing(14)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.partQty = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partQty.setFont(font)
        self.partQty.setText("")
        self.partQty.setObjectName("partQty")
        self.gridLayout.addWidget(self.partQty, 6, 1, 1, 1)
        self.partBox = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partBox.setFont(font)
        self.partBox.setText("")
        self.partBox.setObjectName("partBox")
        self.gridLayout.addWidget(self.partBox, 5, 1, 1, 1)
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.partShelf = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partShelf.setFont(font)
        self.partShelf.setText("")
        self.partShelf.setObjectName("partShelf")
        self.gridLayout.addWidget(self.partShelf, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minus.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minus.setIcon(icon)
        self.minus.setObjectName("minus")
        self.horizontalLayout_2.addWidget(self.minus)
        self.quantity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quantity.setFont(font)
        self.quantity.setScaledContents(False)
        self.quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.quantity.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.quantity.setObjectName("quantity")
        self.horizontalLayout_2.addWidget(self.quantity)
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus.setIcon(icon1)
        self.plus.setObjectName("plus")
        self.horizontalLayout_2.addWidget(self.plus)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 2)
        self.addToCartButton = QtWidgets.QPushButton(self.centralwidget)
        self.addToCartButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addToCartButton.setDefault(False)
        self.addToCartButton.setObjectName("addToCartButton")
        self.gridLayout.addWidget(self.addToCartButton, 13, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 2)
        self.partID = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partID.setFont(font)
        self.partID.setText("")
        self.partID.setObjectName("partID")
        self.gridLayout.addWidget(self.partID, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.partImage = QtWidgets.QLabel(self.centralwidget)
        self.partImage.setMaximumSize(QtCore.QSize(130, 130))
        self.partImage.setText("")
        self.partImage.setPixmap(QtGui.QPixmap("images/default_item.png"))
        self.partImage.setScaledContents(True)
        self.partImage.setObjectName("partImage")
        self.gridLayout.addWidget(self.partImage, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.categoryView = QtWidgets.QListView(self.centralwidget)
        self.categoryView.setMinimumSize(QtCore.QSize(350, 0))
        self.categoryView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.categoryView.setAlternatingRowColors(True)
        self.categoryView.setObjectName("categoryView")
        self.gridLayout_2.addWidget(self.categoryView, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 4)
        self.partName = QtWidgets.QLabel(self.centralwidget)
        self.partName.setStyleSheet("font: 20pt \"Noto Sans\";")
        self.partName.setAlignment(QtCore.Qt.AlignCenter)
        self.partName.setObjectName("partName")
        self.gridLayout_2.addWidget(self.partName, 2, 3, 1, 1)
        self.itemListView = QtWidgets.QListView(self.centralwidget)
        self.itemListView.setMinimumSize(QtCore.QSize(350, 0))
        self.itemListView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.itemListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.itemListView.setAlternatingRowColors(True)
        self.itemListView.setObjectName("itemListView")
        self.gridLayout_2.addWidget(self.itemListView, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 2, 1, 1)
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.gridLayout_3.addWidget(self.status, 1, 1, 1, 1)
        inventoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(inventoryWindow)
        QtCore.QMetaObject.connectSlotsByName(inventoryWindow)
        inventoryWindow.setTabOrder(self.categoryView, self.itemListView)

    def retranslateUi(self, inventoryWindow):
        _translate = QtCore.QCoreApplication.translate
        inventoryWindow.setWindowTitle(_translate("inventoryWindow", "MainWindow"))
        self.cartButton.setText(_translate("inventoryWindow", "View Cart"))
        self.partCategory.setText(_translate("inventoryWindow", "Category"))
        self.label_4.setText(_translate("inventoryWindow", "Shelf:"))
        self.label_3.setText(_translate("inventoryWindow", "ID:"))
        self.quantity.setText(_translate("inventoryWindow", " 1 "))
        self.addToCartButton.setText(_translate("inventoryWindow", "Add to Cart"))
        self.label.setText(_translate("inventoryWindow", "Selected Quantity"))
        self.label_5.setText(_translate("inventoryWindow", "Box:"))
        self.label_12.setText(_translate("inventoryWindow", "Available:"))
        self.label_2.setText(_translate("inventoryWindow", "Inventory Browser"))
        self.label_7.setText(_translate("inventoryWindow", "Item"))
        self.partName.setText(_translate("inventoryWindow", "Item Name"))
        self.label_6.setText(_translate("inventoryWindow", "Category"))

