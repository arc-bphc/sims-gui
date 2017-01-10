#!/usr/local/bin/python
import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_splashScreen

class splashScreen(Ui_splashScreen):
    def __init__(self, window):
        Ui_splashScreen.__init__(self)
        self.setupUi(window)
        self.pushButton.clicked.connect(self.launchWindow)
    def launchWindow(self):
        print "hello"

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    prog = splashScreen(window)
    window.show()
    sys.exit(app.exec_())
