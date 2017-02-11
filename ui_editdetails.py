# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdetails.ui'
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

class Ui_editDetailsWindow(object):
    def setupUi(self, editDetailsWindow):
        editDetailsWindow.setObjectName(_fromUtf8("editDetailsWindow"))
        editDetailsWindow.resize(1077, 788)
        editDetailsWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        editDetailsWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.gridLayout_3 = QtGui.QGridLayout(editDetailsWindow)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget = QtGui.QWidget(editDetailsWindow)
        self.widget.setMinimumSize(QtCore.QSize(450, 300))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 1, 451, 291))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(400, 40))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QtCore.QSize(400, 40))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.textEdit_3 = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMaximumSize(QtCore.QSize(400, 40))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.gridLayout.addWidget(self.textEdit_3, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit_4 = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setMaximumSize(QtCore.QSize(400, 40))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.gridLayout.addWidget(self.textEdit_4, 3, 1, 1, 1)
        self.textEdit_5 = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy)
        self.textEdit_5.setMaximumSize(QtCore.QSize(400, 40))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.gridLayout.addWidget(self.textEdit_5, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_10 = QtGui.QLabel(editDetailsWindow)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(editDetailsWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)

        self.retranslateUi(editDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(editDetailsWindow)

    def retranslateUi(self, editDetailsWindow):
        editDetailsWindow.setWindowTitle(_translate("editDetailsWindow", "Form", None))
        self.label_3.setText(_translate("editDetailsWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Phone No. (WhatsApp)</span></p></body></html>", None))
        self.label_2.setText(_translate("editDetailsWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Phone No. (Calling)</span></p></body></html>", None))
        self.label_4.setText(_translate("editDetailsWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Room Number</span></p></body></html>", None))
        self.label_5.setText(_translate("editDetailsWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Personal Email</span></p></body></html>", None))
        self.label.setText(_translate("editDetailsWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Name</span></p></body></html>", None))
        self.label_10.setText(_translate("editDetailsWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Edit User Details</span></p></body></html>", None))

