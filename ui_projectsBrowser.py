# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectsBrowser.ui'
#
# Created: Mon Jan  1 14:43:34 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_projectsBrowserWindow(object):
    def setupUi(self, projectsBrowserWindow):
        projectsBrowserWindow.setObjectName("projectsBrowserWindow")
        projectsBrowserWindow.resize(1151, 829)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(projectsBrowserWindow.sizePolicy().hasHeightForWidth())
        projectsBrowserWindow.setSizePolicy(sizePolicy)
        projectsBrowserWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(projectsBrowserWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 1, 1, 1)
        self.status = QtWidgets.QLabel(projectsBrowserWindow)
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.gridLayout_3.addWidget(self.status, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 6, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(projectsBrowserWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.ViewCart = QtWidgets.QPushButton(projectsBrowserWindow)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.ViewCart.setFont(font)
        self.ViewCart.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ViewCart.setObjectName("ViewCart")
        self.gridLayout_2.addWidget(self.ViewCart, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(projectsBrowserWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(projectsBrowserWindow)
        self.name.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.new_2 = QtWidgets.QPushButton(projectsBrowserWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_2.sizePolicy().hasHeightForWidth())
        self.new_2.setSizePolicy(sizePolicy)
        self.new_2.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_2.setIcon(icon)
        self.new_2.setObjectName("new_2")
        self.horizontalLayout.addWidget(self.new_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(projectsBrowserWindow)
        self.deleteButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteButton.setAutoFillBackground(False)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout_2.addWidget(self.deleteButton, 6, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(projectsBrowserWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_2.addWidget(self.saveButton, 5, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lead = QtWidgets.QLabel(projectsBrowserWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lead.setFont(font)
        self.lead.setText("")
        self.lead.setObjectName("lead")
        self.verticalLayout.addWidget(self.lead)
        self.gridLayout_2.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.Inventory = QtWidgets.QPushButton(projectsBrowserWindow)
        self.Inventory.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Inventory.setObjectName("Inventory")
        self.gridLayout_2.addWidget(self.Inventory, 5, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 4, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 7, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 2, 1, 2)
        self.userView = QtWidgets.QListView(projectsBrowserWindow)
        self.userView.setMinimumSize(QtCore.QSize(350, 0))
        self.userView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.userView.setAlternatingRowColors(True)
        self.userView.setObjectName("userView")
        self.gridLayout.addWidget(self.userView, 2, 0, 2, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 4)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(projectsBrowserWindow)
        self.label.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.changeLeadUser = QtWidgets.QPushButton(projectsBrowserWindow)
        self.changeLeadUser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.changeLeadUser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.changeLeadUser.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/usernew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeLeadUser.setIcon(icon1)
        self.changeLeadUser.setCheckable(True)
        self.changeLeadUser.setObjectName("changeLeadUser")
        self.gridLayout_3.addWidget(self.changeLeadUser, 1, 2, 1, 1)

        self.retranslateUi(projectsBrowserWindow)
        QtCore.QMetaObject.connectSlotsByName(projectsBrowserWindow)

    def retranslateUi(self, projectsBrowserWindow):
        _translate = QtCore.QCoreApplication.translate
        projectsBrowserWindow.setWindowTitle(_translate("projectsBrowserWindow", "Form"))
        self.label_10.setText(_translate("projectsBrowserWindow", "<html><head/><body><p>Team Leader</p></body></html>"))
        self.ViewCart.setText(_translate("projectsBrowserWindow", "View Cart"))
        self.label_5.setText(_translate("projectsBrowserWindow", "Name"))
        self.new_2.setText(_translate("projectsBrowserWindow", "New"))
        self.deleteButton.setText(_translate("projectsBrowserWindow", "Delete"))
        self.saveButton.setText(_translate("projectsBrowserWindow", "Save"))
        self.Inventory.setText(_translate("projectsBrowserWindow", "Inventory"))
        self.label.setText(_translate("projectsBrowserWindow", "      Projects List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    projectsBrowserWindow = QtWidgets.QWidget()
    ui = Ui_projectsBrowserWindow()
    ui.setupUi(projectsBrowserWindow)
    projectsBrowserWindow.show()
    sys.exit(app.exec_())
