from PyQt4 import QtCore, QtGui
import sys
from ui_mainwindow import Ui_splashScreen
from ui_userprofile import Ui_userWindow

class mainWindow(QtGui.QWidget):
    def __init__(self, widget):
        super(mainWindow, self).__init__()

        self.splashScreen = QtGui.QMainWindow()
        self.userProfile = QtGui.QDialog()
        self.resetPin = QtGui.QWidget()
        self.fingerprint = QtGui.QDialog()
        self.requestItem = QtGui.QWidget()
        self.editDetails = QtGui.QWidget()
        self.inventory = QtGui.QMainWindow()

        self.StackWidget = QtGui.QStackedWidget(self)
        self.createStackedPages()

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.StackWidget)
        widget.setLayout(hbox)

        self.StackWidget.setCurrentIndex(0)

    def printString(self):
        print "HellowORld"

    def createStackedPages(self):
        Ui_userWindow().setupUi(self.userProfile)

        #f = self.splashScreen.gridLayout
        #self.pushButton.clicked.connect(lambda: self.printString())
        self.StackWidget.addWidget(self.splashScreen)
        self.StackWidget.addWidget(self.userProfile)
        self.StackWidget.addWidget(self.resetPin)
        self.StackWidget.addWidget(self.fingerprint)
        self.StackWidget.addWidget(self.requestItem)
        self.StackWidget.addWidget(self.editDetails)
        self.StackWidget.addWidget(self.inventory)

    def setupSplashScreen(self):
        Ui_splashScreen().setupUi(self.splashScreen)
        button = self.splashScreen.findChild(QtGui.QPushButton, "pushButton")
        button.clicked.connect(lambda: self.launchUserProfile())

    def launchUserProfile(self):
        self.StackWidget.setCurrentIndex(1)

def main():
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    prog = mainWindow(widget)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
'''
        self.StackedWidget = QtGui.QStackedWidget(self)
        self.StackedWidget.addWidget(self.stack1)

        self.StackedWidget.setCurrentIndex(0)

            def stack1UI(self):
                inst = Ui_resetPinWindow()
                widg = QtGui.QWidget()
                inst.setupUi(widg)
                layout = QtGui.QHBoxLayout()
                layout.addWidget(widg)
                self.stack1.setLayout(layout)

'''
