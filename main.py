#!/usr/bin/env python3

import sys
import json

from threading import Thread
import sqlite3

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
from ui_editusers import Ui_editUsersWindow
from ui_enrolfingerprint import Ui_enrolFingerWindow

from sql.user_details import user_info
from sql.reset_pin import resetPin
from sql.view_cart import view_cart
from sql.inventory import selectFromInventory
from sql.purchase import purchaseRequests
from sql.enrollUser import enrollUser
from sql.editUsers import editUsers
from sql.insert_data_users import db

from fingerprint_sensor.finger_download import *
from fingerprint_sensor.FPS import *

database_path='./sql/'
dbs=db(database_path+'SIMS.db')

# Objects from this class are used for the active user in the application
# At a time, only one user can be logged in.
# NOTE: Make this a singleton in the future?

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

# Event Filter

def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

# The mainWindow class handles all the GUI widgets and logic

class mainWindow(QWidget):
    def __init__(self, widget):
        super(mainWindow, self).__init__()

        self.loadConfig()

        self.windowWidget = widget
        self.windowWidget.setStyleSheet("QPushButton {padding: 10px}\nQWidget {background-color: white}\n* {font: 16pt}\n")
        self.windowWidget.setWindowTitle("Smart Inventory Management System")
#        self.windowWidget.resize(1280, 800)

        self.userId = None

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
        self.editUsers = QWidget()
        self.enrolFingerprint = QWidget()

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
        self.HomeWidget.addWidget(self.finger)

        vbox = QVBoxLayout()
        vbox.addWidget(self.arcHeader)
        vbox.addWidget(self.StackWidget)
        self.screenWidget.setLayout(vbox)

        windowVBox = QVBoxLayout()
        windowVBox.addWidget(self.HomeWidget)

        self.windowWidget.setLayout(windowVBox)

        self.HomeWidget.setCurrentIndex(0)
        self.StackWidget.setCurrentIndex(0)

    # The widget on top with the back button, ARC logo, and user options
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
        arcLogo.setMaximumSize(QSize(117, 100))
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

    # Config is loaded from the config.json file present in the same dir
    def loadConfig(self):
        with open('config.json') as data_file:
            data = json.load(data_file)

        self.device = data['Settings']['device']
        self.fprintEnabled = data['Settings']['fingerprint']['enabled']
        self.sensorPath = data['Settings']['fingerprint']['sensorPath']
        self.baudRate = data['Settings']['fingerprint']['baudRate']
        self.userImagePath = data['Settings']['images']['user-images-path']
        self.userImagesPrefix = data['Settings']['images']['user-images-prefix']
        self.inventoryImagesPath = data['Settings']['images']['inventory-images-path']
        self.inventoryImagesPrefix = data['Settings']['images']['inventory-images-prefix']
        self.resourceImagesPath = data['Settings']['images']['resource-images-path']
        self.databasePath = data['Settings']['database']['path']
        print ('Loading config from \'config.json\'')

    def handleComboBox(self, val):
        if val == 0:
            self.StackWidget.setCurrentIndex(0)
        if val == 1:
            self.HomeWidget.setCurrentIndex(2)
        if val == 2:
            self.StackWidget.setCurrentIndex(7)

    # The widgets are arranged in a QStackedWidget. They are layered on
    # top of one another in the order in which they are added to the StackWidget
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
        self.StackWidget.addWidget(self.editUsers)
        self.StackWidget.addWidget(self.enrolFingerprint)

    # Each widget has a setup function which modifies the QWidget defined
    # in the mainWindow class by calling the setupUi method of the autogenerated
    # UI->Python files. We connect the actions of each widget through Qt's signal/slots
    def setupSplashScreen(self):
        Ui_splashScreen().setupUi(self.splashScreen)
        self.pinEntry = False

        clickable(self.splashScreen).connect(lambda: self.unlockScreen())


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
        self.fingerprintObject = fsensor(self.sensorPath, self.baudRate)

        fingerLabel = self.finger.findChild(QLabel, "fingerLabel")
        # fingerData = None
        self.scanFingerprint = QMovie("images/finger-scan.gif")
        self.scanFingerprint.setScaledSize(QSize(320, 240))
        self.scanFingerprint.start()
        fingerLabel.setMovie(self.scanFingerprint)
        Thread(target=self.scanFinger).start()

    # Fingerprint login is supported here. We only take the sensor's word
    # for whether the fingerprint provided is valid.
    def unlockScreen(self):
        if self.fprintEnabled == True:
            self.setupFinger()
            self.HomeWidget.setCurrentIndex(3)
            auth = True
        else:
            auth = True
            self.HomeWidget.setCurrentIndex(1)

        if auth == True:
            userInfo = user_info(self.databasePath)
            userData = userInfo.get_user_info(1)
            print(userData)
            self.user = userDetails(userData[0],1,True) #CHANGE THIS ASAP!!
            self.createStackedPages()

    def scanFinger(self):
        correctFingerprint = QPixmap("images/finger-correct.gif")
        wrongFingerprint = QPixmap("images/finger-wrong.gif")

        fingerLabel = self.finger.findChild(QLabel, "fingerLabel")
        # loggedIn = False
        # while(loggedIn == False):
        fingerId = self.fingerprintObject.Search()
        if (fingerId == None):
            print('NOT FOUND')
            fingerLabel.setPixmap(wrongFingerprint)
            time.sleep(1)
            # fingerLabel.setMovie(self.scanFingerprint)
            self.HomeWidget.setCurrentIndex(0)
        else:
            print('FOUND')
            fingerLabel.setPixmap(correctFingerprint)
            time.sleep(1)
            userInfoObject = user_info(self.databasePath)
            # loggedIn = True
            self.userId = userInfoObject.identify_user(fingerId)
            print(fingerId)
            # fingerData = fingerId
            self.HomeWidget.setCurrentIndex(1)

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
        editUsersButton = self.admin.findChild(QPushButton, "editUsersButton")

        enrolUserButton.clicked.connect(lambda: self.launchWindow(8))
        editUsersButton.clicked.connect(lambda: self.launchWindow(9))

    def launchEnrolFingerprint(self):
        self.launchWindow(10)
        self.setupEnrolFingerprint()

    def setupEnrol(self):
        Ui_enrolWindow().setupUi(self.enrol)

        enrollUserObject = enrollUser(self.databasePath)
        userInfoObject = user_info(self.databasePath)

        buttonBox = self.enrol.findChild(QDialogButtonBox, "buttonBox")
        name = self.enrol.findChild(QLineEdit, "name")
        userID = self.enrol.findChild(QLineEdit, "userID")
        email = self.enrol.findChild(QLineEdit, "email")
        phoneCall = self.enrol.findChild(QLineEdit, "phoneCall")
        phoneWhatsApp = self.enrol.findChild(QLineEdit, "phoneWhatsApp")
        roomNumber = self.enrol.findChild(QLineEdit, "roomNumber")
        pin = self.enrol.findChild(QLineEdit, "pin")
        inventoryAccess = self.enrol.findChild(QCheckBox, "inventoryAccess")
        labAccess = self.enrol.findChild(QCheckBox, "labAccess")
        adminPriv = self.enrol.findChild(QCheckBox, "adminPriv")
        biometricButton = self.enrol.findChild(QPushButton, "biometricButton")
        # buttonBox.accepted.connect()
        self.ftemplate=None
        biometricButton.clicked.connect(lambda: self.launchEnrolFingerprint())
        buttonBox.rejected.connect(lambda: self.launchWindow(0))

        if self.user.isAdmin == True:
            buttonBox.rejected.connect(lambda: self.launchWindow(0))
            buttonBox.accepted.connect(lambda: enrollUserObject.enrollNewUser(str(name.text()), \
                                                            str(email.text()), str(phoneCall.text()), \
                                                            str(phoneWhatsApp.text()), str(roomNumber.text()), \
                                                            str(pin.text()),  adminPriv.isChecked(), \
                                                            labAccess.isChecked(), inventoryAccess.isChecked()))

            buttonBox.accepted.connect(lambda: enrollUserObject.storeFingerprint(userInfoObject.getUserID(), self.ftemplate[0], self.ftemplate[1]))
            buttonBox.accepted.connect(lambda: self.fingerprintObject.SetTemplate(self.ftemplate[1],self.ftemplate[0]))
            buttonBox.accepted.connect(lambda: self.showMsgBox('Database successfully updated!'))
            buttonBox.accepted.connect(lambda: self.launchWindow(0))
        else:
            buttonBox.rejected.connect(lambda: self.launchWindow(0))
            buttonBox.accepted.connect(lambda: self.showMsgBox('You are not authorized to do this!'))

    def setupEditUsers(self):
        Ui_editUsersWindow().setupUi(self.editUsers)

        self.editUsersObject = editUsers(self.databasePath)
        self.userInfoObject = user_info(self.databasePath)
        print(self.editUsersObject.listUser())

        username = self.editUsers.findChild(QLabel, "username")
        name = self.editUsers.findChild(QLineEdit, "name")
        email = self.editUsers.findChild(QLineEdit, "email")
        phoneCall = self.editUsers.findChild(QLineEdit, "phoneCall")
        phoneWhatsApp = self.editUsers.findChild(QLineEdit, "roomNumber")

        adminCheckBox = self.editUsers.findChild(QCheckBox, "adminCheckBox")
        labCheckBox = self.editUsers.findChild(QCheckBox, "labCheckBox")
        inventoryCheckBox = self.editUsers.findChild(QCheckBox, "inventoryCheckBox")

        biometricButton = self.editUsers.findChild(QPushButton, "biometricButton")
        saveButton = self.editUsers.findChild(QPushButton, "saveButton")

        userView = self.editUsers.findChild(QListView, "userView")
        self.userList = self.editUsersObject.listUser()
        self.userModel = QStandardItemModel()
        userView.setModel(self.userModel)
        for item in self.userList:
            self.userModel.appendRow(QStandardItem(item[1]))
        userView.clicked.connect(self.updateEditUserInfo)

        self.ftemplate = None
        biometricButton.clicked.connect(lambda: self.launchEnrolFingerprint())

        if self.user.isAdmin == True:
            saveButton.clicked.connect(lambda: self.showMsgBox('Database successfully updated!'))
        else:
            saveButton.clicked.connect(lambda: self.showMsgBox('You are not authorized to do this!'))

    def updateEditUserInfo(self, nameId):
        print(self.userModel.item(nameId.row()).text())

        username = self.editUsers.findChild(QLabel, "username")
        name = self.editUsers.findChild(QLineEdit, "name")
        email = self.editUsers.findChild(QLineEdit, "email")
        phoneCall = self.editUsers.findChild(QLineEdit, "phoneCall")
        phoneWhatsApp = self.editUsers.findChild(QLineEdit, "phoneWhatsApp")
        roomNumber = self.editUsers.findChild(QLineEdit, "roomNumber")
        adminCheckBox = self.editUsers.findChild(QCheckBox, "adminCheckBox")
        labCheckBox = self.editUsers.findChild(QCheckBox, "labCheckBox")
        inventoryCheckBox = self.editUsers.findChild(QCheckBox, "inventoryCheckBox")
        userImage = self.editUsers.findChild(QLabel, "userImage")

        res = self.userInfoObject.get_user_info(self.userList[nameId.row()][0])

        username.setText(res[0])
        name.setText(res[0])
        email.setText(res[4])
        phoneCall.setText(res[1])
        phoneWhatsApp.setText(res[2])
        roomNumber.setText(res[3])
        userImage.setPixmap(QPixmap(self.userImagePath + self.userImagesPrefix + \
                                    str(self.user.getUserId()) + '.jpg'))


    def setupEnrolFingerprint(self):
        Ui_enrolFingerWindow().setupUi(self.enrolFingerprint)

        fingerprintWidgets = []
        fingerprintWidgets.append(self.enrolFingerprint.findChild(QLabel, "fprint1"))
        fingerprintWidgets.append(self.enrolFingerprint.findChild(QLabel, "fprint2"))
        fingerprintWidgets.append(self.enrolFingerprint.findChild(QLabel, "fprint3"))
        exitButton = self.enrolFingerprint.findChild(QPushButton, "exitButton")
        fingerprintButton = self.enrolFingerprint.findChild(QPushButton, "fingerprintButton")

        exitButton.clicked.connect(lambda: self.exitFingerEnroll())
        for fprint in fingerprintWidgets:
            # fprint.setMovie(scanFingerprint)
            fprint.setPixmap(QPixmap("images/fingerprint-icon.jpg"))

        finger_ids=dbs.selectQuery('fingerprint',['FINGERPRINT_ID'],['SENSOR IS NOT 2'])
        finger_ids=set([i[0] for i in finger_ids])
        all_index=set(range(1,max(finger_ids)+1))
        index=min(all_index-finger_ids)
        print(index)

        # self.fingerprintObject = fsensor(self.sensorPath, self.baudRate)
        self.fingerprintObject.resetEnrollIndex()

        scanFingerprint = QMovie("images/finger-scan.gif")
        scanFingerprint.setScaledSize(QSize(320, 240))

        threads=[]
        self.fingerprintObject.stop=False
        t=Thread(target=self.setFingerprintStates,args=(fingerprintWidgets,index,scanFingerprint,threads,))
        threads.append(t)
        # fingerprintWidgets[0].setMovie(scanFingerprint)
        t.start()

    def setFingerprintStates(self, fingerprintWidgets,index,scanFingerprint,threads):
        curr_enroll=self.fingerprintObject.getCurrentEnrollIndex()

        fingerprintWidgets[curr_enroll].setMovie(scanFingerprint)
        scanFingerprint.start()

        defaultFingerprint= QPixmap("images/fingerprint-icon.jpg")
        correctFingerprint = QPixmap("images/finger-correct.gif")
        wrongFingerprint = QPixmap("images/finger-wrong.gif")
        # scanFingerprint = QMovie("images/finger-scan.gif")
        # scanFingerprint.setScaledSize(QSize(320, 240))
        if curr_enroll==0:
            for i in fingerprintWidgets[1:]:
                i.setPixmap(defaultFingerprint)

        ret=self.fingerprintObject.enroll(index)
        if ret==True:
            fingerprintWidgets[curr_enroll].setPixmap(correctFingerprint)
            if curr_enroll<2:
                fingerprintWidgets[self.fingerprintObject.getCurrentEnrollIndex()].setMovie(scanFingerprint)
                scanFingerprint.start()
                t=Thread(target=self.setFingerprintStates,args=(fingerprintWidgets,index,scanFingerprint,threads,))
                threads.append(t)
                t.start()
                return
            elif curr_enroll==2:
                template=self.fingerprintObject.GetTemplate(index)[1]
                self.fingerprintObject.DeleteID(index)
                self.ftemplate=[index,template]
            else:
                pass
        else:
            print("sensor response"+str(ret))
            if curr_enroll==2:
                for i in fingerprintWidgets:
                    i.setPixmap(wrongFingerprint)
            else:
                fingerprintWidgets[curr_enroll].setPixmap(wrongFingerprint)
            return

        # t.start()


        # if fingerprintObject.getCurrentEnrollIndex() == 0:
        #     fingerprintWidgets[0].setMovie(scanFingerprint)
        #     scanFingerprint.start()
        #     if fingerprintObject.enroll(index)==True:
        #         fingerprintWidgets[0].setPixmap(correctFingerprint)
        #         fingerprintWidgets[1].setMovie(scanFingerprint)
        #         if fingerprintObject.enroll(index)==True:
        #             fingerprintWidgets[0].setPixmap(correctFingerprint)
        #             fingerprintWidgets[1].setPixmap(correctFingerprint)
        #             fingerprintWidgets[2].setMovie(scanFingerprint)
        #             if fingerprintObject.enroll(index)==True:
        #                 fingerprintWidgets[0].setPixmap(correctFingerprint)
        #                 fingerprintWidgets[1].setPixmap(correctFingerprint)
        #                 fingerprintWidgets[2].setPixmap(correctFingerprint)
        #                 self.showMsgBox('Fingerprint Registered!')
        #                 return True
        #             else:
        #                 self.showMsgBox('Try Again')
        #                 return False
        #         else:
        #             self.showMsgBox('Try Again')

    def exitFingerEnroll(self):
        self.fingerprintObject.stop=True
        print("stopping enrollment")
        self.launchWindow(8)

    def removeFromCartAction(self, listView, partID):
        if len(listView.selectedIndexes()) != 0:
            self.viewCart.removeFromCart(self.user.getUserId(), partID)
            self.updateViewCart()

    # Logging out closes and reopens the application
    def logoutUser(self):
        self.windowWidget.close()
        self.windowWidget = QWidget()
        mainWindow(self.windowWidget)
        if self.device == 'desktop':
            self.windowWidget.show()
        else:
            self.windowWidget.showMaximized()

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
        if currentPwd:
            result = resetPinObject.compareEnteredPin(self.user.getUserId(), currentPwd, newPwd)
            if result == 0:
                self.showMsgBox('Wrong PIN!')
            else:
                self.showMsgBox('PIN successfully updated!')
                self.launchWindow(0)
        else:
            self.showMsgBox('Enter Current Password')

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
        self.setupEditUsers()

    def showMsgBox(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Result")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def getDevice(self):
        return self.device

    def loginWithPIN(self):
        if self.pinEntry == False:
            self.pinEntry = True
            self.pinBox.show()
        else:
            print("To be implemented soon")

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
