# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemwidget.ui'
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

class Ui_itemWidget(object):
    def setupUi(self, itemWidget):
        itemWidget.setObjectName(_fromUtf8("itemWidget"))
        itemWidget.resize(425, 368)
        itemWidget.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.widget = QtGui.QWidget(itemWidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 241, 235))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 6, 0, 1, 2)
        self.label_8 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 2)

        self.retranslateUi(itemWidget)
        QtCore.QMetaObject.connectSlotsByName(itemWidget)

    def retranslateUi(self, itemWidget):
        itemWidget.setWindowTitle(_translate("itemWidget", "Form", None))
        self.checkBox.setText(_translate("itemWidget", "Add to Cart", None))
        self.label_8.setText(_translate("itemWidget", "&68206165", None))
        self.label_6.setText(_translate("itemWidget", "&3", None))
        self.label_10.setText(_translate("itemWidget", "5", None))
        self.label_7.setText(_translate("itemWidget", "&035", None))
        self.label.setText(_translate("itemWidget", "ID:", None))
        self.label_9.setText(_translate("itemWidget", "&5", None))
        self.label_5.setText(_translate("itemWidget", "Bo&x:", None))
        self.label_3.setText(_translate("itemWidget", "She&lf:", None))
        self.label_2.setText(_translate("itemWidget", "RFID:", None))
        self.label_4.setText(_translate("itemWidget", "&Quantity:", None))
        self.label_11.setText(_translate("itemWidget", "<html><head/><body><p align=\"center\">Arduino UNO</p></body></html>", None))

