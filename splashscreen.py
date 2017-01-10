#import sys
from PyQt4 import QtCore, QtGui
from ui_mainwindow import Ui_splashScreen

class splashScreen(Ui_splashScreen):
    def __init__(self, window):
        Ui_splashScreen.__init__(self)
        self.setupUi(window)
        self.pushButton.clicked.connect(self.launchWindow)
    def launchWindow(self):
        print "hello"
