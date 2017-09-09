# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'arc-header.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#try:
    # = QtCore.QString.fromUtf8
#except AttributeError:
    #def (s):
        #return s

#try:
    #_encoding = QtWidgets.QApplication.UnicodeUTF8
    #def _translate(context, text, disambig):
        #return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
#except AttributeError:
    #def _translate(context, text, disambig):
        #return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_arcHeader(object):
    def setupUi(self, arcHeader):
        arcHeader.setObjectName(("arcHeader"))
        arcHeader.resize(983, 196)
        arcHeader.setAutoFillBackground(False)
        arcHeader.setStyleSheet(("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(arcHeader)
        #self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName(("horizontalLayout_2"))
        
        self.backButton = QtWidgets.QPushButton(arcHeader)
        #self.backButton.setMinimumSize(QtCore.QSize(50, 50))
        self.backButton.setText((""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(("images/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(48, 48))
        self.backButton.setFlat(True)
        self.backButton.setObjectName(("backButton"))
        #self.horizontalLayout_2.addWidget(self.backButton, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(arcHeader)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(117, 100))
        self.label_3.setText((""))
        self.label_3.setPixmap(QtGui.QPixmap(("13015184_719298964879056_6631447530178360880_n.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(("label_3"))
        #self.horizontalLayout_2.addWidget(self.label_3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.widget = QtWidgets.QWidget(arcHeader)
        self.widget.setObjectName(("widget"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(("horizontalLayout_3"))
        #self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        #self.horizontalLayout.setObjectName(("horizontalLayout"))
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 40))
        self.label_4.setMaximumSize(QtCore.QSize(50, 50))
        self.label_4.setText((""))
        self.label_4.setPixmap(QtGui.QPixmap("index.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox = QtWidgets.QPushButton(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setObjectName("comboBox")
        #self.horizontalLayout_2.addWidget(self.comboBox)
        #self.horizontalLayout_2.addWidget(self.widget, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        #self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.widget.setStyleSheet("QPushButton {padding: 10px}\nQWidget {background-color: white}\n")
        self.retranslateUi(arcHeader)
        QtCore.QMetaObject.connectSlotsByName(arcHeader)

    def retranslateUi(self, arcHeader):
        pass
        #arcHeader.setWindowTitle(_translate("arcHeader", "Form", None))

