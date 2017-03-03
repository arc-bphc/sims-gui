# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_splashScreen(object):
    def setupUi(self, splashScreen):
        splashScreen.setObjectName("splashScreen")
        splashScreen.resize(977, 731)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(splashScreen.sizePolicy().hasHeightForWidth())
        splashScreen.setSizePolicy(sizePolicy)
        splashScreen.setMaximumSize(QtCore.QSize(1982, 1175))
        splashScreen.setStyleSheet("background-color: white\n"
"")
        self.centralWidget = QtWidgets.QWidget(splashScreen)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setStyleSheet("font: 75 150pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setMaximumSize(QtCore.QSize(492, 192))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/12967978_719298328212453_6846422403842474807_o.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pushButton.setStyleSheet("padding: 10px\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setStyleSheet("font: 75 italic 24pt \"Noto Sans\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        splashScreen.setCentralWidget(self.centralWidget)

        self.retranslateUi(splashScreen)
        QtCore.QMetaObject.connectSlotsByName(splashScreen)

    def retranslateUi(self, splashScreen):
        _translate = QtCore.QCoreApplication.translate
        splashScreen.setWindowTitle(_translate("splashScreen", "Welcome Screen"))
        self.label_2.setText(_translate("splashScreen", "SIMS"))
        self.pushButton.setText(_translate("splashScreen", "Continue"))
        self.label_3.setText(_translate("splashScreen", "Smart Inventory Management System"))

