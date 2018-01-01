# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminpanel.ui'
#
# Created: Mon Jan  1 11:52:54 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adminWindow(object):
    def setupUi(self, adminWindow):
        adminWindow.setObjectName("adminWindow")
        adminWindow.resize(640, 480)
        adminWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(adminWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(adminWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(adminWindow)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.enrolUserButton = QtWidgets.QPushButton(adminWindow)
        self.enrolUserButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.enrolUserButton.setObjectName("enrolUserButton")
        self.gridLayout.addWidget(self.enrolUserButton, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.editUsersButton = QtWidgets.QPushButton(adminWindow)
        self.editUsersButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.editUsersButton.setObjectName("editUsersButton")
        self.gridLayout.addWidget(self.editUsersButton, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.Projects = QtWidgets.QPushButton(adminWindow)
        self.Projects.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Projects.setObjectName("Projects")
        self.gridLayout.addWidget(self.Projects, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(adminWindow)
        self.pushButton_4.setMinimumSize(QtCore.QSize(85, 38))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton_3 = QtWidgets.QPushButton(adminWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(85, 38))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(adminWindow)
        self.pushButton_2.setMinimumSize(QtCore.QSize(85, 38))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(adminWindow)
        QtCore.QMetaObject.connectSlotsByName(adminWindow)

    def retranslateUi(self, adminWindow):
        _translate = QtCore.QCoreApplication.translate
        adminWindow.setWindowTitle(_translate("adminWindow", "Form"))
        self.label_5.setText(_translate("adminWindow", "Administration Panel"))
        self.pushButton.setText(_translate("adminWindow", "Edit Inventory"))
        self.enrolUserButton.setText(_translate("adminWindow", "Enrol User"))
        self.editUsersButton.setText(_translate("adminWindow", "Edit Users"))
        self.Projects.setText(_translate("adminWindow", "Projects"))
        self.pushButton_4.setText(_translate("adminWindow", "Shut Down"))
        self.pushButton_3.setText(_translate("adminWindow", "EXIT"))
        self.pushButton_2.setText(_translate("adminWindow", "Restart"))

