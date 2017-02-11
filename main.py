#write top layouts by hand
from PyQt4 import QtCore, QtGui
import sys

from ui_mainwindow import Ui_splashScreen
from ui_userprofile import Ui_userWindow
from ui_resetpin import Ui_resetPinWindow
from ui_finger import Ui_loginWindow
from ui_requestitem import Ui_requestItemWindow
from ui_editdetails import Ui_editDetailsWindow
from ui_inventory import Ui_inventoryWindow
from ui_cart import Ui_cartWindow

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
        self.arcHeader = QtGui.QWidget()
        self.cart = QtGui.QWidget()

        self.username = "ARC-User-X"

        self.setupHeaderWidget(self.arcHeader)

        self.StackWidget = QtGui.QStackedWidget(self)
        self.HomeWidget = QtGui.QStackedWidget(self)
        self.screenWidget = QtGui.QWidget()
        self.createStackedPages()

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.arcHeader)
        vbox.addWidget(self.StackWidget)
        self.screenWidget.setLayout(vbox)

        windowVBox = QtGui.QVBoxLayout()
        windowVBox.addWidget(self.HomeWidget)
        widget.setLayout(windowVBox)

        self.HomeWidget.setCurrentIndex(0)
        self.StackWidget.setCurrentIndex(0)

    def setupHeaderWidget(self, widget):
        hbox = QtGui.QHBoxLayout()
        #hbox.addWidget(QtGui.QRadioButton("Hello"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        #setting up gui
        backButton = QtGui.QPushButton()
        backButton.setFlat(True)
        backButton.setIcon(icon)
        backButton.setIconSize(QtCore.QSize(32, 32))

        arcLogo = QtGui.QLabel()
        arcLogo.setMinimumSize(QtCore.QSize(0, 0))
        arcLogo.setMaximumSize(QtCore.QSize(175, 150))
        arcLogo.setPixmap(QtGui.QPixmap("images/arclogo.png"))
        arcLogo.setScaledContents(True)

        userWidget = QtGui.QWidget()
        userHBox = QtGui.QHBoxLayout()
        userIcon = QtGui.QLabel()
        comboBox = QtGui.QComboBox()

        userIcon.setMinimumSize(QtCore.QSize(0, 40))
        userIcon.setMaximumSize(QtCore.QSize(50, 50))
        userIcon.setPixmap(QtGui.QPixmap("index.png"))
        userIcon.setScaledContents(True)
        comboBox.setMinimumSize(QtCore.QSize(200, 40))
        comboBox.setMaximumSize(QtCore.QSize(300, 16777215))

        comboBox.addItem(self.username)
        comboBox.addItem("Logout")

        userHBox.addWidget(userIcon)
        userHBox.addWidget(comboBox)
        userWidget.setLayout(userHBox)

        hbox.addWidget(backButton)
        hbox.addWidget(arcLogo)
        hbox.addWidget(userWidget)
        hbox.setAlignment(backButton, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        hbox.setAlignment(arcLogo, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        hbox.setAlignment(userWidget, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        widget.setLayout(hbox)
        widget.setStyleSheet("QPushButton {padding: 10px}\nQWidget {background-color: white}\n")

        backButton.clicked.connect(self.goBack)


    def createStackedPages(self):
        self.setupWindows()
        #self.StackWidget.addWidget(self.splashScreen)
        self.StackWidget.addWidget(self.userProfile)
        self.StackWidget.addWidget(self.resetPin)
        self.StackWidget.addWidget(self.fingerprint)
        self.StackWidget.addWidget(self.requestItem)
        self.StackWidget.addWidget(self.editDetails)
        self.StackWidget.addWidget(self.inventory)
        self.StackWidget.addWidget(self.cart)

        self.HomeWidget.addWidget(self.splashScreen)
        self.HomeWidget.addWidget(self.screenWidget)

    def setupSplashScreen(self):
        Ui_splashScreen().setupUi(self.splashScreen)
        button = self.splashScreen.findChild(QtGui.QPushButton, "pushButton")

        button.clicked.connect(lambda: self.unlockScreen())

    def setupUserProfile(self):
        Ui_userWindow().setupUi(self.userProfile)
        inventoryButton = self.userProfile.findChild(QtGui.QPushButton, "inventoryButton")
        editDetailsButton = self.userProfile.findChild(QtGui.QPushButton, "editDetailsButton")
        requestButton = self.userProfile.findChild(QtGui.QPushButton, "requestButton")
        resetPinButton = self.userProfile.findChild(QtGui.QPushButton, "resetPinButton")
        cartButton = self.userProfile.findChild(QtGui.QPushButton, "cartButton")
        welcomeLabel = self.userProfile.findChild(QtGui.QLabel, "welcomeLabel")

        inventoryButton.clicked.connect(lambda: self.launchWindow(5))
        editDetailsButton.clicked.connect(lambda: self.launchWindow(4))
        requestButton.clicked.connect(lambda: self.launchWindow(3))
        resetPinButton.clicked.connect(lambda: self.launchWindow(1))
        cartButton.clicked.connect(lambda: self.launchWindow(6))

        welcomeLabel.setText("Welcome, " + self.username)

    def setupResetPin(self):
        Ui_resetPinWindow().setupUi(self.resetPin)
        buttonBox = self.resetPin.findChild(QtGui.QDialogButtonBox, "buttonBox")
        buttonBox.rejected.connect(lambda: self.launchWindow(0))

    def setupFingerprint(self):
        Ui_loginWindow().setupUi(self.fingerprint)

    def setupRequestItem(self):
        Ui_requestItemWindow().setupUi(self.requestItem)
        buttonBox = self.requestItem.findChild(QtGui.QDialogButtonBox, "buttonBox")
        buttonBox.rejected.connect(lambda: self.launchWindow(0))

    def setupEditDetails(self):
        Ui_editDetailsWindow().setupUi(self.editDetails)
        buttonBox = self.editDetails.findChild(QtGui.QDialogButtonBox, "buttonBox")
        buttonBox.rejected.connect(lambda: self.launchWindow(0))

    def setupInventory(self):
        Ui_inventoryWindow().setupUi(self.inventory)
        buttonBox = self.inventory.findChild(QtGui.QDialogButtonBox, "buttonBox")
        cartButton = self.inventory.findChild(QtGui.QPushButton, "cartButton")

        buttonBox.rejected.connect(lambda: self.launchWindow(0))
        cartButton.clicked.connect(lambda: self.launchWindow(6))


    def setupCart(self):
        Ui_cartWindow().setupUi(self.cart)

    def comboAction(self, x):
        if (x == 1):
            self.launchWindow(0)

    def launchWindow(self, value):
        self.StackWidget.setCurrentIndex(value)

    def goBack(self):
        self.StackWidget.setCurrentIndex(0)

    def unlockScreen(self):
        self.HomeWidget.setCurrentIndex(1)

    def setupWindows(self):
        self.setupSplashScreen()
        self.setupUserProfile()
        self.setupResetPin()
        self.setupFingerprint()
        self.setupRequestItem()
        self.setupEditDetails()
        self.setupInventory()
        self.setupCart()

def main():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('13015184_719298964879056_6631447530178360880_n.png'))
    widget = QtGui.QWidget()
    widget.setStyleSheet("QPushButton {padding: 10px}\nQWidget {background-color: white}\n")
    widget.setWindowTitle("Smart Inventory Management System")
    prog = mainWindow(widget)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
