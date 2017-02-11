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
        inventoryWindow.resize(1110, 672)
        inventoryWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.centralwidget = QtGui.QWidget(inventoryWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 4, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 2)
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 3, 2, 1, 2)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 3, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        inventoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(inventoryWindow)
        QtCore.QMetaObject.connectSlotsByName(inventoryWindow)

    def retranslateUi(self, inventoryWindow):
        inventoryWindow.setWindowTitle(_translate("inventoryWindow", "MainWindow", None))
        self.pushButton_4.setText(_translate("inventoryWindow", "Save", None))
        self.label_4.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Selected Items</span></p></body></html>", None))
        self.label_2.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Inventory</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("inventoryWindow", "-", None))
        self.label.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ARC Inventory</span></p></body></html>", None))
        self.pushButton.setText(_translate("inventoryWindow", "+", None))

