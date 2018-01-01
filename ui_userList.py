# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userList.ui'
#
# Created: Mon Jan  1 13:39:49 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userList(object):
    def setupUi(self, userList):
        userList.setObjectName("userList")
        userList.resize(1151, 829)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(userList.sizePolicy().hasHeightForWidth())
        userList.setSizePolicy(sizePolicy)
        userList.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(userList)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.userView = QtWidgets.QListView(userList)
        self.userView.setMinimumSize(QtCore.QSize(350, 0))
        self.userView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.userView.setAlternatingRowColors(True)
        self.userView.setObjectName("userView")
        self.verticalLayout.addWidget(self.userView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Select = QtWidgets.QPushButton(userList)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Select.setFont(font)
        self.Select.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Select.setObjectName("Select")
        self.horizontalLayout.addWidget(self.Select)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(userList)
        self.label.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(userList)
        QtCore.QMetaObject.connectSlotsByName(userList)

    def retranslateUi(self, userList):
        _translate = QtCore.QCoreApplication.translate
        userList.setWindowTitle(_translate("userList", "Form"))
        self.Select.setText(_translate("userList", "Select"))
        self.label.setText(_translate("userList", "Users"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userList = QtWidgets.QWidget()
    ui = Ui_userList()
    ui.setupUi(userList)
    userList.show()
    sys.exit(app.exec_())

