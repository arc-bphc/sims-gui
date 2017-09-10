# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editusers.ui'
#
# Created: Sun Sep 10 11:23:32 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editUsersWindow(object):
    def setupUi(self, editUsersWindow):
        editUsersWindow.setObjectName("editUsersWindow")
        editUsersWindow.resize(1151, 829)
        editUsersWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(editUsersWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(editUsersWindow)
        self.saveButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_3.addWidget(self.saveButton, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(editUsersWindow)
        self.label.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 4, QtCore.Qt.AlignHCenter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.email = QtWidgets.QLineEdit(editUsersWindow)
        self.email.setObjectName("email")
        self.gridLayout_2.addWidget(self.email, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(editUsersWindow)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(editUsersWindow)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(editUsersWindow)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(editUsersWindow)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 7, 0, 1, 1)
        self.roomNumber = QtWidgets.QLineEdit(editUsersWindow)
        self.roomNumber.setObjectName("roomNumber")
        self.gridLayout_2.addWidget(self.roomNumber, 7, 1, 1, 1)
        self.phoneWhatsApp = QtWidgets.QLineEdit(editUsersWindow)
        self.phoneWhatsApp.setObjectName("phoneWhatsApp")
        self.gridLayout_2.addWidget(self.phoneWhatsApp, 6, 1, 1, 1)
        self.biometricButton = QtWidgets.QPushButton(editUsersWindow)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.biometricButton.setFont(font)
        self.biometricButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.biometricButton.setObjectName("biometricButton")
        self.gridLayout_2.addWidget(self.biometricButton, 12, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(editUsersWindow)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.phoneCall = QtWidgets.QLineEdit(editUsersWindow)
        self.phoneCall.setObjectName("phoneCall")
        self.gridLayout_2.addWidget(self.phoneCall, 5, 1, 1, 1)
        self.labCheckBox = QtWidgets.QCheckBox(editUsersWindow)
        self.labCheckBox.setObjectName("labCheckBox")
        self.gridLayout_2.addWidget(self.labCheckBox, 8, 1, 1, 1)
        self.inventoryCheckBox = QtWidgets.QCheckBox(editUsersWindow)
        self.inventoryCheckBox.setObjectName("inventoryCheckBox")
        self.gridLayout_2.addWidget(self.inventoryCheckBox, 10, 0, 1, 2)
        self.name = QtWidgets.QLineEdit(editUsersWindow)
        self.name.setEnabled(False)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 3, 1, 1, 1)
        self.adminCheckBox = QtWidgets.QCheckBox(editUsersWindow)
        self.adminCheckBox.setObjectName("adminCheckBox")
        self.gridLayout_2.addWidget(self.adminCheckBox, 8, 0, 1, 1)
        self.username = QtWidgets.QLabel(editUsersWindow)
        self.username.setStyleSheet("font: 20pt \"Noto Sans\";")
        self.username.setObjectName("username")
        self.gridLayout_2.addWidget(self.username, 1, 0, 1, 1)
        self.userImage = QtWidgets.QLabel(editUsersWindow)
        self.userImage.setMinimumSize(QtCore.QSize(75, 75))
        self.userImage.setMaximumSize(QtCore.QSize(130, 130))
        self.userImage.setText("")
        self.userImage.setPixmap(QtGui.QPixmap("images/users/index.png"))
        self.userImage.setScaledContents(True)
        self.userImage.setObjectName("userImage")
        self.gridLayout_2.addWidget(self.userImage, 1, 1, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(editUsersWindow)
        self.deleteButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteButton.setAutoFillBackground(True)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout_2.addWidget(self.deleteButton, 12, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 3, 1, 2)
        self.userView = QtWidgets.QListView(editUsersWindow)
        self.userView.setMinimumSize(QtCore.QSize(350, 0))
        self.userView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.userView.setAlternatingRowColors(True)
        self.userView.setObjectName("userView")
        self.gridLayout.addWidget(self.userView, 3, 1, 2, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 3, 1, 1, 1)

        self.retranslateUi(editUsersWindow)
        QtCore.QMetaObject.connectSlotsByName(editUsersWindow)

    def retranslateUi(self, editUsersWindow):
        _translate = QtCore.QCoreApplication.translate
        editUsersWindow.setWindowTitle(_translate("editUsersWindow", "Form"))
        self.saveButton.setText(_translate("editUsersWindow", "Save Details"))
        self.label.setText(_translate("editUsersWindow", "Edit Users"))
        self.label_9.setText(_translate("editUsersWindow", "Phone (WhatsApp)"))
        self.label_8.setText(_translate("editUsersWindow", "Phone (Calling)"))
        self.label_5.setText(_translate("editUsersWindow", "Name"))
        self.label_11.setText(_translate("editUsersWindow", "Room Number"))
        self.biometricButton.setText(_translate("editUsersWindow", "Biometrics"))
        self.label_10.setText(_translate("editUsersWindow", "Email"))
        self.labCheckBox.setText(_translate("editUsersWindow", "ARC Lab Access"))
        self.inventoryCheckBox.setText(_translate("editUsersWindow", "Inventory Access"))
        self.adminCheckBox.setText(_translate("editUsersWindow", "Administrator"))
        self.username.setText(_translate("editUsersWindow", "User ID"))
        self.deleteButton.setText(_translate("editUsersWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editUsersWindow = QtWidgets.QWidget()
    ui = Ui_editUsersWindow()
    ui.setupUi(editUsersWindow)
    editUsersWindow.show()
    sys.exit(app.exec_())

