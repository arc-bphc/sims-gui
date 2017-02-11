# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arc-header.ui'
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

class Ui_arcHeader(object):
    def setupUi(self, arcHeader):
        arcHeader.setObjectName(_fromUtf8("arcHeader"))
        arcHeader.resize(983, 196)
        arcHeader.setAutoFillBackground(False)
        arcHeader.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(arcHeader)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.backButton = QtGui.QPushButton(arcHeader)
        self.backButton.setMinimumSize(QtCore.QSize(50, 50))
        self.backButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ChevronLeft-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(32, 32))
        self.backButton.setFlat(True)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout_2.addWidget(self.backButton, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3 = QtGui.QLabel(arcHeader)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(175, 150))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("13015184_719298964879056_6631447530178360880_n.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.widget = QtGui.QWidget(arcHeader)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 40))
        self.label_4.setMaximumSize(QtCore.QSize(50, 50))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("index.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_2.addWidget(self.widget, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(arcHeader)
        QtCore.QMetaObject.connectSlotsByName(arcHeader)

    def retranslateUi(self, arcHeader):
        arcHeader.setWindowTitle(_translate("arcHeader", "Form", None))

