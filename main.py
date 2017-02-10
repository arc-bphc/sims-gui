from PyQt4 import QtCore, QtGui
import sys

from ui_mainwindow import Ui_splashScreen
from ui_userprofile import Ui_userWindow
from ui_resetpin import Ui_resetPinWindow
from ui_finger import Ui_loginWindow
from ui_requestitem import Ui_requestItemWindow
from ui_editdetails import Ui_editDetailsWindow
from ui_inventory import Ui_inventoryWindow

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
        self.setupWindows()
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

        button.clicked.connect(lambda: self.launchWindow(1))

    def setupUserProfile(self):
        Ui_userWindow().setupUi(self.userProfile)
        inventoryButton = self.userProfile.findChild(QtGui.QPushButton, "inventoryButton")
        editDetailsButton = self.userProfile.findChild(QtGui.QPushButton, "editDetailsButton")
        requestButton = self.userProfile.findChild(QtGui.QPushButton, "requestButton")
        resetPinButton = self.userProfile.findChild(QtGui.QPushButton, "resetPinButton")
        comboBox = self.userProfile.findChild(QtGui.QComboBox, "comboBox")

        inventoryButton.clicked.connect(lambda: self.launchWindow(6))
        editDetailsButton.clicked.connect(lambda: self.launchWindow(5))
        requestButton.clicked.connect(lambda: self.launchWindow(4))
        resetPinButton.clicked.connect(lambda: self.launchWindow(2))
        comboBox.currentIndexChanged.connect(self.comboAction)

    def setupResetPin(self):
        Ui_resetPinWindow().setupUi(self.resetPin)
        backButton = self.resetPin.findChild(QtGui.QPushButton, "backButton")
        buttonBox = self.resetPin.findChild(QtGui.QDialogButtonBox, "buttonBox")
        comboBox = self.resetPin.findChild(QtGui.QComboBox, "comboBox")

        backButton.clicked.connect(lambda: self.launchWindow(1))
        buttonBox.rejected.connect(lambda: self.launchWindow(1))
        comboBox.currentIndexChanged.connect(self.comboAction)

    def setupFingerprint(self):
        Ui_loginWindow().setupUi(self.fingerprint)
#        backButton = self.resetPin.findChild(QtGui.QPushButton, "backButton")

#        backButton.clicked.connect(lambda: self.launchWindow(1))


    def setupRequestItem(self):
        Ui_requestItemWindow().setupUi(self.requestItem)
        backButton = self.requestItem.findChild(QtGui.QPushButton, "backButton")
        buttonBox = self.requestItem.findChild(QtGui.QDialogButtonBox, "buttonBox")
        comboBox = self.requestItem.findChild(QtGui.QComboBox, "comboBox")

        backButton.clicked.connect(lambda: self.launchWindow(1))
        buttonBox.rejected.connect(lambda: self.launchWindow(1))
        comboBox.currentIndexChanged.connect(self.comboAction)

    def setupEditDetails(self):
        Ui_editDetailsWindow().setupUi(self.editDetails)
        backButton = self.editDetails.findChild(QtGui.QPushButton, "backButton")
        buttonBox = self.editDetails.findChild(QtGui.QDialogButtonBox, "buttonBox")
        comboBox = self.editDetails.findChild(QtGui.QComboBox, "comboBox")

        backButton.clicked.connect(lambda: self.launchWindow(1))
        buttonBox.rejected.connect(lambda: self.launchWindow(1))
        comboBox.currentIndexChanged.connect(self.comboAction)

    def setupInventory(self):
        Ui_inventoryWindow().setupUi(self.inventory)
        backButton = self.inventory.findChild(QtGui.QPushButton, "backButton")
        comboBox = self.inventory.findChild(QtGui.QComboBox, "comboBox")

        backButton.clicked.connect(lambda: self.launchWindow(1))
        comboBox.currentIndexChanged.connect(self.comboAction)

    def comboAction(self, x):
        if (x == 1):
            self.launchWindow(0)

    def launchWindow(self, value):
        self.StackWidget.setCurrentIndex(value)

    def setupWindows(self):
        self.setupSplashScreen()
        self.setupUserProfile()
        self.setupResetPin()
        self.setupFingerprint()
        self.setupRequestItem()
        self.setupEditDetails()
        self.setupInventory()

def main():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('13015184_719298964879056_6631447530178360880_n.png'))
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
