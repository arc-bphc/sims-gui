import sys
from PyQt4 import QtCore, QtGui
from ui_mainwindow import Ui_splashScreen
from userprofile import userProfile

class splashScreen(Ui_splashScreen):
    def __init__(self, window):
        Ui_splashScreen.__init__(self)
        self.setupUi(window)
        self.pushButton.clicked.connect(self.launchWindow)
        self.f = QtGui.QDialog()

    def launchWindow(self):
        j = userProfile(self.f)
        self.f.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    x = QtGui.QMainWindow()
    prog = splashScreen(x)
    x.show()
    sys.exit(app.exec_())
