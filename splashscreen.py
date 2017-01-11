import sys
from PyQt4 import QtCore, QtGui
from ui_mainwindow import Ui_splashScreen
from userprofile import userProfile

class splashScreen(Ui_splashScreen):
    def __init__(self, widget):
        Ui_splashScreen.__init__(self)
        self.setupUi(widget)
        self.pushButton.clicked.connect(lambda: self.launchWindow(widget))
        self.profileWidget = QtGui.QDialog()
    def launchWindow(self, widget):
        prog = userProfile(self.profileWidget)
        self.profileWidget.show()
        widget.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    winddowWidget = QtGui.QMainWindow()
    prog = splashScreen(winddowWidget)
#    winddowWidget.showFullScreen()
    winddowWidget.show()
    sys.exit(app.exec_())
