#!/usr/bin/env python

import sys
import json

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui_mainwindow import Ui_splashScreen
from ui_userprofile import Ui_userWindow
from ui_resetpin import Ui_resetPinWindow
from ui_finger import Ui_loginWindow
from ui_requestitem import Ui_requestItemWindow
from ui_editdetails import Ui_editDetailsWindow
from ui_inventory import Ui_inventoryWindow
from ui_cart import Ui_cartWindow
from ui_about import Ui_aboutWindow
from ui_adminpanel import Ui_adminWindow
from ui_enrol import Ui_enrolWindow

from sql.user_details import user_info
from sql.reset_pin import resetPin
from sql.view_cart import view_cart
from sql.inventory import selectFromInventory
from sql.purchase import purchaseRequests
from sql.enrollUser import enrollUser

from fingerprint_sensor.finger_download import *

class userDetails():
    def __init__(self, _name = "ARC-User-X", _userId = 1, _isAdmin = True):
        self._name = _name
        self._userId = _userId
        self.isAdmin = _isAdmin

    def getName(self):
        return self._name

    def getUserId(self):
        return self._userId

    def isAdmin():
        return isAdmin

class mainWindow(QWidget):
    def __init__(self, widget):
        super(mainWindow, self).__init__()

        self.loadConfig()

        self.windowWidget = widget
        self.windowWidget.setStyleSheet("QPushButton {padding: 10px}\nQWidget {background-color: white}\n* {font: 16pt}\n")
        self.windowWidget.setWindowTitle("Smart Inventory Management System")
#        self.windowWidget.resize(1280, 800)

        self.splashScreen = QMainWindow()
        self.userProfile = QDialog()
        self.resetPin = QWidget()
        self.fingerprint = QDialog()
        self.requestItem = QWidget()
        self.editDetails = QWidget()
        self.inventory = QMainWindow()
        self.arcHeader = QWidget()
        self.cart = QWidget()
        self.finger = QDialog()
        self.about = QWidget()
        self.admin = QWidget()
        self.enrol = QWidget()

        self.currentPage = 0
        self.previousPage = 0

        self.StackWidget = QStackedWidget(self)
        self.HomeWidget = QStackedWidget(self)
        self.screenWidget = QWidget()

        self.setupAbout()
        self.setupSplashScreen()

        self.HomeWidget.addWidget(self.splashScreen)
        self.HomeWidget.addWidget(self.screenWidget)
        self.HomeWidget.addWidget(self.about)

        vbox = QVBoxLayout()
        vbox.addWidget(self.arcHeader)
        vbox.addWidget(self.StackWidget)
        self.screenWidget.setLayout(vbox)

        windowVBox = QVBoxLayout()
        windowVBox.addWidget(self.HomeWidget)

        self.windowWidget.setLayout(windowVBox)

        self.HomeWidget.setCurrentIndex(0)
        self.StackWidget.setCurrentIndex(0)

    def setupHeaderWidget(self, widget):
        hbox = QHBoxLayout()
        icon = QIcon()
        icon.addPixmap(QPixmap("images/back.png"), QIcon.Normal, QIcon.Off)

        #setting up gui
        backButton = QPushButton()
        backButton.setFlat(True)
        backButton.setIcon(icon)
        backButton.setIconSize(QSize(48, 48))

        arcLogo = QLabel()
        arcLogo.setMinimumSize(QSize(0, 0))
        arcLogo.setMaximumSize(QSize(175, 150))
        arcLogo.setPixmap(QPixmap('images/arclogo.png'))
        arcLogo.setScaledContents(True)

        userWidget = QWidget()
        userHBox = QHBoxLayout()
        userIcon = QLabel()
        comboBox = QComboBox()

        userIcon.setMinimumSize(QSize(0, 40))
        userIcon.setMaximumSize(QSize(50, 50))
        userIcon.setPixmap(QPixmap(self.userImagePath + self.userImagesPrefix + \
                                    str(self.user.getUserId()) + '.jpg'))
        userIcon.setScaledContents(True)
        comboBox.setMinimumSize(QSize(200, 40))
        comboBox.setMaximumSize(QSize(300, 16777215))

        comboBox.addItem(self.user.getName())
        comboBox.addItem('About')
        if self.user.isAdmin == True:
            comboBox.addItem("Admin Panel")

        comboBox.activated.connect(self.handleComboBox)

        userHBox.addWidget(userIcon)
        userHBox.addWidget(comboBox)
        userWidget.setLayout(userHBox)

        hbox.addWidget(backButton)
        hbox.addWidget(arcLogo)
        hbox.addWidget(userWidget)
        hbox.setAlignment(backButton, Qt.AlignLeft|Qt.AlignTop)
        hbox.setAlignment(arcLogo, Qt.AlignHCenter|Qt.AlignTop)
        hbox.setAlignment(userWidget, Qt.AlignRight|Qt.AlignTop)
        widget.setLayout(hbox)
        widget.setStyleSheet("QPushButton {padding: 10px}\nQWidget {background-color: white}\n")

        backButton.clicked.connect(self.goBack)

    def loadConfig(self):
        with open('config.json') as data_file:
            data = json.load(data_file)

        self.device = data['Settings']['device']
        self.fprintEnabled = data['Settings']['fingerprint']['enabled']
        self.sensorPath = data['Settings']['fingerprint']['sensorPath']
        self.userImagePath = data['Settings']['images']['user-images-path']
        self.userImagesPrefix = data['Settings']['images']['user-images-prefix']
        self.inventoryImagesPath = data['Settings']['images']['inventory-images-path']
        self.inventoryImagesPrefix = data['Settings']['images']['inventory-images-prefix']
        self.resourceImagesPath = data['Settings']['images']['resource-images-path']
        self.databasePath = data['Settings']['database']['path']
        print 'Loading config from \'config.json\''

    def handleComboBox(self, val):
        if val == 0:
            self.StackWidget.setCurrentIndex(0)
        if val == 1:
            self.HomeWidget.setCurrentIndex(2)
        if val == 2:
            self.StackWidget.setCurrentIndex(7)

    def createStackedPages(self):
        self.setupWindows()
        self.StackWidget.addWidget(self.userProfile)
        self.StackWidget.addWidget(self.resetPin)
        self.StackWidget.addWidget(self.fingerprint)
        self.StackWidget.addWidget(self.requestItem)
        self.StackWidget.addWidget(self.editDetails)
        self.StackWidget.addWidget(self.inventory)
        self.StackWidget.addWidget(self.cart)
        self.StackWidget.addWidget(self.admin)
        self.StackWidget.addWidget(self.enrol)

    def setupSplashScreen(self):
        Ui_splashScreen().setupUi(self.splashScreen)
        button = self.splashScreen.findChild(QPushButton, "pushButton")

        button.clicked.connect(lambda: self.unlockScreen())

    def setupAbout(self):
        Ui_aboutWindow().setupUi(self.about)
        closeButton = self.about.findChild(QPushButton, "closeButton")

        closeButton.clicked.connect(lambda: self.HomeWidget.setCurrentIndex(1))

    def setupFingerprint(self):
        Ui_loginWindow.setupUi(self.finger)

    def setupUserProfile(self):
        Ui_userWindow().setupUi(self.userProfile)
        inventoryButton = self.userProfile.findChild(QPushButton, "inventoryButton")
        editDetailsButton = self.userProfile.findChild(QPushButton, "editDetailsButton")
        requestButton = self.userProfile.findChild(QPushButton, "requestButton")
        resetPinButton = self.userProfile.findChild(QPushButton, "resetPinButton")
        cartButton = self.userProfile.findChild(QPushButton, "cartButton")
        lockButton = self.userProfile.findChild(QPushButton, "lockButton")
        logoutButton = self.userProfile.findChild(QPushButton, "logoutButton")
        welcomeLabel = self.userProfile.findChild(QLabel, "welcomeLabel")
        profilePic = self.userProfile.findChild(QLabel, "profilePic")

        inventoryButton.clicked.connect(lambda: self.launchWindow(5))
        editDetailsButton.clicked.connect(lambda: self.launchWindow(4))
        requestButton.clicked.connect(lambda: self.launchWindow(3))
        resetPinButton.clicked.connect(lambda: self.launchWindow(1))
        cartButton.clicked.connect(lambda: self.launchWindow(6))

        logoutButton.clicked.connect(lambda: self.logoutUser())

        welcomeLabel.setText("Welcome, " + self.user.getName())
        profilePic.setPixmap(QPixmap(self.userImagePath + self.userImagesPrefix + \
                                    str(self.user.getUserId()) + '.jpg'))

    def setupResetPin(self):
        Ui_resetPinWindow().setupUi(self.resetPin)
        buttonBox = self.resetPin.findChild(QDialogButtonBox, "buttonBox")
        currentPwd = self.resetPin.findChild(QLineEdit, "currentPwd")
        newPwd = self.resetPin.findChild(QLineEdit, "newPwd")

        buttonBox.accepted.connect(lambda: self.execResetPin(currentPwd.text(), newPwd.text()))
        buttonBox.rejected.connect(lambda: self.launchWindow(0))

    def setupFinger(self):
        Ui_loginWindow().setupUi(self.finger)

    def setupRequestItem(self):
        Ui_requestItemWindow().setupUi(self.requestItem)
        project = self.requestItem.findChild(QLineEdit, "project")
        item = self.requestItem.findChild(QLineEdit, "item")
        price = self.requestItem.findChild(QLineEdit, "price")
        requestItemButton = self.requestItem.findChild(QPushButton, "requestItemButton")
        buttonBox = self.requestItem.findChild(QDialogButtonBox, "buttonBox")

        purchaseRequest = purchaseRequests(self.databasePath)
        buttonBox.accepted.connect(lambda: (purchaseRequest.addToTable(self.user.getUserId(), \
                                    str(project.text()), str(price.text()), \
                                    str(item.text()), 1000),
                                    self.showMsgBox('Request submitted!')))
        buttonBox.rejected.connect(lambda: self.launchWindow(0))

    def setupEditDetails(self):
        Ui_editDetailsWindow().setupUi(self.editDetails)

        buttonBox = self.editDetails.findChild(QDialogButtonBox, "buttonBox")
        buttonBox.rejected.connect(lambda: self.launchWindow(0))
        buttonBox.accepted.connect(lambda: self.saveUserDetails(self.user.getUserId()))
        buttonBox.accepted.connect(lambda: self.showMsgBox('Database successfully updated!'))
        buttonBox.accepted.connect(lambda: self.launchWindow(0))

        userInfo = user_info(self.databasePath)
        userData = userInfo.get_user_info(self.user.getUserId())

        name = self.editDetails.findChild(QLineEdit, "name")
        phoneCall = self.editDetails.findChild(QLineEdit, "phoneCall")
        phoneWhatsApp = self.editDetails.findChild(QLineEdit, "phoneWhatsApp")
        roomNumber = self.editDetails.findChild(QLineEdit, "roomNumber")
        email = self.editDetails.findChild(QLineEdit, "email")

        name.setText(userData[0])
        phoneCall.setText(userData[1])
        phoneWhatsApp.setText(userData[2])
        roomNumber.setText(userData[3])
        email.setText(userData[4])

    def setupInventory(self):
        Ui_inventoryWindow().setupUi(self.inventory)

        self.inventoryDb = selectFromInventory(self.databasePath)
        self.categoryList = self.inventoryDb.getCatagories()
        self.categoryModel = QStandardItemModel()
        self.itemListModel = QStandardItemModel()

        cartButton = self.inventory.findChild(QPushButton, "cartButton")
        categoryView = self.inventory.findChild(QListView, "categoryView")
        itemView = self.inventory.findChild(QListView, "itemListView")
        addToCartButton = self.inventory.findChild(QPushButton, "addToCartButton")
        qtySpinBox = self.inventory.findChild(QSpinBox, "qtySpinBox")
        partQty = self.inventory.findChild(QLabel, "partQty")

        categoryView.setModel(self.categoryModel)
        itemView.setModel(self.itemListModel)

        for item in self.categoryList:
            self.categoryModel.appendRow(QStandardItem(item))

        categoryView.clicked.connect(self.updateInventoryItemList)
        itemView.clicked.connect(self.updateInventoryItemInfo)
        cartButton.clicked.connect(lambda: self.launchWindow(6))
        addToCartButton.clicked.connect(lambda: self.addToCartAction(itemView, qtySpinBox, partQty))

    def setupCart(self):
        Ui_cartWindow().setupUi(self.cart)

        self.viewCart = view_cart(self.databasePath)
        self.model = QStandardItemModel()

        listView = self.cart.findChild(QListView, "listView")
        buttonBox = self.cart.findChild(QDialogButtonBox, "buttonBox")
        openInventory = self.cart.findChild(QPushButton, "openInventory")
        removeCartButton = self.cart.findChild(QPushButton, "removeCartButton")
        partID = self.cart.findChild(QLabel, "partID")
        partQty = self.cart.findChild(QLabel, "partQty")

        listView.setModel(self.model)
        self.updateViewCart()

        removeCartButton.clicked.connect(lambda: self.removeFromCartAction(listView, int(str(partID.text()))))
        listView.clicked.connect(self.displayCartItem)
        openInventory.clicked.connect(lambda: self.launchWindow(5))

    def setupAdmin(self):
        Ui_adminWindow().setupUi(self.admin)

        enrolUserButton = self.admin.findChild(QPushButton, "enrolUserButton")

        enrolUserButton.clicked.connect(lambda: self.launchWindow(8))

    def setupEnrol(self):
        Ui_enrolWindow().setupUi(self.enrol)

        enrollUserObject = enrollUser(self.databasePath)

        buttonBox = self.enrol.findChild(QDialogButtonBox, "buttonBox")
        name = self.enrol.findChild(QLineEdit, "name")
        userID = self.enrol.findChild(QLineEdit, "userID")
        email = self.enrol.findChild(QLineEdit, "email")
        phoneCall = self.enrol.findChild(QLineEdit, "phoneCall")
        phoneWhatsApp = self.enrol.findChild(QLineEdit, "phoneWhatsApp")
        roomNumber = self.enrol.findChild(QLineEdit, "roomNumber")
        pin = self.enrol.findChild(QLineEdit, "pin")


        if self.user.isAdmin == True:
            buttonBox.rejected.connect(lambda: self.launchWindow(0))
            buttonBox.accepted.connect(lambda: enrollUserObject.enrollNewUser(str(name.text()), \
                                                            str(email.text()), str(phoneCall.text()), \
                                                            str(phoneWhatsApp.text()), str(roomNumber.text()), \
                                                            str(pin.text()), str(25)))
#            buttonBox.accepted.connect(lambda: self.showMsgBox('Database successfully updated!'))
            buttonBox.accepted.connect(lambda: self.launchWindow(0))
        else:
            buttonBox.rejected.connect(lambda: self.launchWindow(0))
            buttonBox.accepted.connect(lambda: self.showMsgBox('You are not authorized to do this!'))

    def removeFromCartAction(self, listView, partID):
        if len(listView.selectedIndexes()) != 0:
            self.viewCart.removeFromCart(self.user.getUserId(), partID)
            self.updateViewCart()

    def logoutUser(self):
        self.windowWidget.close()
        self.windowWidget = QWidget()
        mainWindow(self.windowWidget)
        if self.device == 'desktop':
            self.windowWidget.show()
        else:
            self.windowWidget.showFullScreen()

    def saveUserDetails(self, userId):
        name = self.editDetails.findChild(QLineEdit, "name")
        phoneCall = self.editDetails.findChild(QLineEdit, "phoneCall")
        phoneWhatsApp = self.editDetails.findChild(QLineEdit, "phoneWhatsApp")
        roomNumber = self.editDetails.findChild(QLineEdit, "roomNumber")
        email = self.editDetails.findChild(QLineEdit, "email")

        userInfo = user_info(self.databasePath)
        userInfo.update_user_info([str(name.text()), str(phoneCall.text()), \
                                str(phoneWhatsApp.text()), str(roomNumber.text()), \
                                str(email.text())], userId)

    def addToCartAction(self, itemView, qtySpinBox, partQty):
        if len(itemView.selectedIndexes()) != 0:
            itemName = '\'' + itemView.selectedIndexes()[0].data() + '\''
            itemId = self.inventoryDb.getItemId(itemName)
            self.inventoryDb.addToCart(self.user.getUserId(), self.user.getName(), itemId, qtySpinBox.value(), '123')
            qty = int(str(partQty.text()))-qtySpinBox.value()
            if qty < 0:
                qty = 0
            partQty.setText(str(qty))

    def updateInventoryItemList(self, id):
        self.itemListModel.clear()
        itemList = self.inventoryDb.getItems(id.row())
        for item in itemList:
            self.itemListModel.appendRow(QStandardItem(item))

    def updateInventoryItemInfo(self, id):
        partName = self.inventory.findChild(QLabel, "partName")
        partCategory = self.inventory.findChild(QLabel, "partCategory")
        partID = self.inventory.findChild(QLabel, "partID")
        partShelf = self.inventory.findChild(QLabel, "partShelf")
        partBox = self.inventory.findChild(QLabel, "partBox")
        partQty = self.inventory.findChild(QLabel, "partQty")
        partImage = self.inventory.findChild(QLabel, "partImage")

        itemDetails = self.inventoryDb.getItemInfo(id.row())
        partName.setText(itemDetails[1])
        partCategory.setText(itemDetails[5])
        partID.setText(str(itemDetails[0]))
        partShelf.setText(str(itemDetails[3]))
        partBox.setText(str(itemDetails[4]))
        partQty.setText(str(itemDetails[6]))
        partImage.setPixmap(QPixmap(self.inventoryImagesPath+self.inventoryImagesPrefix + \
                                    str(itemDetails[0])+'.png'))

    def execResetPin(self, currentPwd, newPwd):
        resetPinObject = resetPin(self.databasePath)
        result = resetPinObject.compareEnteredPin(self.user.getUserId(), currentPwd, newPwd)
        if result == 0:
            self.showMsgBox('Wrong PIN!')
        else:
            self.showMsgBox('PIN successfully updated!')
            self.launchWindow(0)

    def updateViewCart(self):
        self.model.clear()
        itemList = self.viewCart.getItemList(self.user.getUserId())
        for item in itemList:
            self.model.appendRow(QStandardItem(item))

    def displayCartItem(self, itemId):
        partName = self.cart.findChild(QLabel, "partName")
        partCategory = self.cart.findChild(QLabel, "partCategory")
        partID = self.cart.findChild(QLabel, "partID")
        partShelf = self.cart.findChild(QLabel, "partShelf")
        partBox = self.cart.findChild(QLabel, "partBox")
        partQty = self.cart.findChild(QLabel, "partQty")
        partImage = self.cart.findChild(QLabel, "partImage")

        itemName = '\'' + itemId.data() + '\''
        itemId = self.inventoryDb.getItemId(itemName)

        itemDetails = self.viewCart.getItemInfo(self.user.getUserId(), itemId)
        partName.setText(itemDetails[1])
        partCategory.setText(itemDetails[5])
        partID.setText(str(itemDetails[0]))
        partShelf.setText(str(itemDetails[3]))
        partBox.setText(str(itemDetails[4]))
        partQty.setText(str(itemDetails[6]))
        partImage.setPixmap(QPixmap(self.inventoryImagesPath+self.inventoryImagesPrefix + \
                                    str(itemDetails[0])+'.png'))

    def launchWindow(self, value):
        self.previousPage = self.currentPage
        self.StackWidget.setCurrentIndex(value)
        self.currentPage = value
        self.updateViewCart()

    def goBack(self):
        self.StackWidget.setCurrentIndex(0)

    def unlockScreen(self):
        button = self.splashScreen.findChild(QPushButton, "pushButton")
        button.setText('Login failed. Try again.'),

        if self.fprintEnabled == True:
            ser=serial.Serial(self.sensorPath,baudrate=57600)
            get_finger()
            auth = Search()[0]
        else:
            auth = 0

        if auth == 0:
            userInfo = user_info(self.databasePath)
            userData = userInfo.get_user_info(1)
            self.user = userDetails(userData[0],1,True) #CHANGE THIS ASAP!!
            self.createStackedPages()
            self.HomeWidget.setCurrentIndex(1)

    def setupWindows(self):
        self.setupHeaderWidget(self.arcHeader)
        self.setupUserProfile()
        self.setupResetPin()
#        self.setupFingerprint()
        self.setupRequestItem()
        self.setupEditDetails()
        self.setupInventory()
        self.setupCart()
        self.setupAdmin()
        self.setupEnrol()

    def showMsgBox(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Result")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def getDevice(self):
        return self.device

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('images/arclogo.png'))

    widget = QWidget()
    prog = mainWindow(widget)
    if prog.getDevice() == 'desktop':
        widget.show()
    else:
        widget.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
