# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_splashScreen(object):
    def setupUi(self, splashScreen):
        splashScreen.setObjectName(_fromUtf8("splashScreen"))
        splashScreen.resize(977, 731)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(splashScreen.sizePolicy().hasHeightForWidth())
        splashScreen.setSizePolicy(sizePolicy)
        splashScreen.setMaximumSize(QtCore.QSize(1982, 1175))
        splashScreen.setStyleSheet(_fromUtf8("background-color: white\n"
""))
        self.centralWidget = QtGui.QWidget(splashScreen)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 150pt \"Noto Sans\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setMaximumSize(QtCore.QSize(492, 192))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/12967978_719298328212453_6846422403842474807_o.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pushButton.setStyleSheet(_fromUtf8("padding: 10px\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setStyleSheet(_fromUtf8("font: 75 italic 24pt \"Noto Sans\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        splashScreen.setCentralWidget(self.centralWidget)

        self.retranslateUi(splashScreen)
        QtCore.QMetaObject.connectSlotsByName(splashScreen)

    def retranslateUi(self, splashScreen):
        splashScreen.setWindowTitle(_translate("splashScreen", "Welcome Screen", None))
        self.label_2.setText(_translate("splashScreen", "SIMS", None))
        self.pushButton.setText(_translate("splashScreen", "Continue", None))
        self.label_3.setText(_translate("splashScreen", "Smart Inventory Management System", None))

