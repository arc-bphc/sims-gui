#!/usr/bin/env python3

import sys
import json
import os
import subprocess

import threading
from threading import Thread
from multiprocessing.pool import ThreadPool
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
from ui_archeader import Ui_arcHeader

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
    def __init__(self, _name = "ARC-User-X", _userId = 1, _isAdmin = True, labAccess = True, inventoryAccess = True):
        self._name = _name
        self._userId = _userId
        self._isAdmin = _isAdmin
        self._hasLabAccess = labAccess
        self._hasInventoryAccess = inventoryAccess

    def getName(self):
        return self._name

    def getUserId(self):
        return self._userId

    def isAdmin(self):
        return self._isAdmin

    def hasLabAccess(self):
        return self._hasLabAccess

    def hasInventoryAccess(self):
        return self._hasInventoryAccess

class ScrollArea(QScrollArea):
    
    def __init__(self,parent=None):
        self.widget=QWidget()
        super().__init__(parent)
    
    def addWidget(self,wid):
        wid.setFixedSize(1119,629)
        self.normalHeight=wid.height()
        wid.setFocusPolicy(Qt.NoFocus)
        wid.setParent(self.widget)
        #wid.show()
        #self.widget=wid
        
        self.widget.setFixedWidth(wid.width())
        self.widget.setFixedHeight(wid.height())
        self.widget.setFocusPolicy(Qt.NoFocus)
        self.setFocus()
        
        self.setWidget(self.widget)
        #self.setFocusPolicy(Qt.NoFocus)
        self.setFrameShape(QFrame.Box)
        self.setWidgetResizable(True)
        self.setLineWidth(0)
        self.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.verticalScrollBar().setFixedWidth(0)
        QScroller.grabGesture(self.viewport(), QScroller.LeftMouseButtonGesture)
        
    def focusInEvent(self,event):
        self.widget.setFixedHeight(self.normalHeight)
        super().focusInEvent(event)
    def focusOutEvent(self,event):
        self.widget.setFixedHeight(1000)
        super().focusOutEvent(event)
        
        

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
        
    userIdSignal = pyqtSignal(int)
    userListChanged = pyqtSignal()
    fingerScanning=False
    HeaderWidgetCreated=False
    UserProfileCreated=False
    FingerCreated=False
    ResetPinCreated=False
    RequestItemCreated=False
    EditDetailsCreated=False
    InventoryCreated=False
    CartCreated=False
    AdminCreated=False
    EnrolCreated=False
    EditUsersCreated=False
    EnrolFingerprintCreated=False
    def __init__(self):
        super(mainWindow, self).__init__()

        self.loadConfig()

        self.windowWidget = QWidget()
        self.windowWidget.setStyleSheet("QPushButton {border-width: 1px;border-color: #339;border-style: solid;border-radius: 8;padding: 10px}\nQPushButton:pressed{background:royalblue;border-color:royalblue;border-width:2px}\nQWidget {background-color: white}\n* {font: 16pt}\n")
        self.windowWidget.setWindowFlags(Qt.FramelessWindowHint)
        
#        self.windowWidget.resize(1280, 800)

        self.userId = None

        self.splashScreen = QMainWindow()
        self.userProfile = QDialog()
        self.resetPin = QWidget()
        self.resetPinScroller = ScrollArea()
        self.fingerprint = QDialog()
        self.requestItem = QWidget()
        self.requestItemScroller = ScrollArea()
        self.editDetails = QWidget()
        self.editDetailsScroller = ScrollArea()
        self.inventory = QMainWindow()
        self.arcHeader = QWidget()
        self.cart = QWidget()
        self.finger = QDialog()
        self.about = QWidget()
        self.admin = QWidget()
        self.enrol = QWidget()
        self.enrolScroller = ScrollArea()
        self.editUsers = QWidget()
        self.editUsersScroller = ScrollArea()
        self.enrolFingerprint = QWidget()

        self.currentPage = 0
        self.previousPage = []
        

        self.StackWidget = QStackedWidget(self)
        self.HomeWidget = QStackedWidget(self)
        self.screenWidget = QWidget()

        self.setupAbout()
        self.setupSplashScreen()
        self.scanThread = ThreadPool(processes=1)
        self.setupFinger()

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
        
        self.onAdminPage=False

        self.windowWidget.setLayout(windowVBox)

        self.HomeWidget.setCurrentIndex(0)
        self.createStackedPages()
        
        self.StackWidget.setCurrentIndex(0)
        self.userListChanged.connect(self.updateUserList)
        self.userIdSignal.connect(self.handleAction)

    # The widget on top with the back button, ARC logo, and user options
    def setupHeaderWidget(self, widget):
        if not self.HeaderWidgetCreated:
            Ui_arcHeader().setupUi(self.arcHeader)
            
        arcLogo = self.arcHeader.findChild(QLabel,'label_3')
        arcLogo.setPixmap(QPixmap('images/arclogo.png'))
        
        backButton = self.arcHeader.findChild(QPushButton,'backButton')
        backButton.setFocusPolicy(Qt.NoFocus)
        
        userWidget = self.arcHeader.findChild(QWidget,'widget')
        userWidget.setFocusPolicy(Qt.NoFocus)
        
        userIcon = self.arcHeader.findChild(QLabel,'label_4')
        userImagePath = self.userImagePath + self.userImagesPrefix + \
                                    str(self.user.getUserId()) + '.jpg'
        if QFile.exists(userImagePath):
            userIcon.setPixmap(QPixmap(userImagePath))
        else:
            userIcon.setPixmap(QPixmap('images/default_user.png'))
       
        comboBox = self.arcHeader.findChild(QPushButton,'comboBox')
        comboBox.setFocusPolicy(Qt.NoFocus)
        #for i in self.user.getName().split(' '):
            #if len(i)>3:
                #username=i
                #break
                
        comboBox.setText('USER:'+str(self.user.getUserId()))
        
        if not self.HeaderWidgetCreated:
            backButton.clicked.connect(self.goBack)
            comboBox.clicked.connect(self.handleComboBox)
            self.HeaderWidgetCreated=True
        
        hbox = self.arcHeader.findChild(QHBoxLayout,'horizontalLayout_2')
        userHBox = self.arcHeader.findChild(QHBoxLayout,'horizontalLayout_3')
        
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
        """
        hbox = QHBoxLayout()
        icon = QIcon()
        icon.addPixmap(QPixmap("images/back.png"), QIcon.Normal, QIcon.Off)

        #setting up gui
        backButton = QPushButton()
        backButton.setFlat(True)
        backButton.setIcon(icon)
        backButton.setIconSize(QSize(48, 48))
        backButton.setFocusPolicy(Qt.NoFocus)

        arcLogo = QLabel()
        arcLogo.setMinimumSize(QSize(0, 0))
        arcLogo.setMaximumSize(QSize(117, 100))
        arcLogo.setPixmap(QPixmap('images/arclogo.png'))
        arcLogo.setScaledContents(True)

        userWidget = QWidget()
        userWidget.setFocusPolicy(Qt.NoFocus)
        userHBox = QHBoxLayout()
        userIcon = QLabel()
        comboBox = QPushButton(self.user.getName())
        comboBox.setFocusPolicy(Qt.NoFocus)
        comboBox.setAttribute(Qt.WA_MouseNoMask,True)
        userIcon.setMinimumSize(QSize(0, 40))
        userIcon.setMaximumSize(QSize(50, 50))
        
        userImagePath = self.userImagePath + self.userImagesPrefix + \
                                    str(self.user.getUserId()) + '.jpg'
        if QFile.exists(userImagePath):
            userIcon.setPixmap(QPixmap(userImagePath))
        else:
            userIcon.setPixmap(QPixmap(userImagePath + self.userImagesPrefix + 'default.png'))
        userIcon.setScaledContents(True)
        comboBox.setMinimumSize(QSize(200, 40))
        comboBox.setMaximumSize(QSize(300, 16777215))

        #comboBox.addItem(self.user.getName())
        #comboBox.addItem('About')
        
            #comboBox.addItem("Admin Panel")
        comboBox.clicked.connect(self.handleComboBox)

        #comboBox.activated.connect(self.handleComboBox)

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
        """
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

    def handleComboBox(self):
        print(self.previousPage)
        if (self.StackWidget.currentIndex() == 0) and self.user.isAdmin():
            self.launchWindow(7)
        else:
            self.previousPage=[]
            self.StackWidget.setCurrentIndex(0)

    # The widgets are arranged in a QStackedWidget. They are layered on
    # top of one another in the order in which they are added to the StackWidget
    def createStackedPages(self):
        self.StackWidget.addWidget(self.userProfile)
        self.StackWidget.addWidget(self.resetPinScroller)
        self.StackWidget.addWidget(self.fingerprint)
        self.StackWidget.addWidget(self.requestItemScroller)
        self.StackWidget.addWidget(self.editDetailsScroller)
        self.StackWidget.addWidget(self.inventory)
        self.StackWidget.addWidget(self.cart)
        self.StackWidget.addWidget(self.admin)
        self.StackWidget.addWidget(self.enrolScroller)
        self.StackWidget.addWidget(self.editUsersScroller)
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
        if not self.UserProfileCreated:
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
        
        inventoryButton.setFocusPolicy(Qt.NoFocus)
        editDetailsButton.setFocusPolicy(Qt.NoFocus)
        requestButton.setFocusPolicy(Qt.NoFocus)
        resetPinButton.setFocusPolicy(Qt.NoFocus)
        cartButton.setFocusPolicy(Qt.NoFocus)
        #lockButton.setFocusPolicy(Qt.NoFocus)
        logoutButton.setFocusPolicy(Qt.NoFocus)
        welcomeLabel.setFocusPolicy(Qt.NoFocus)
        profilePic.setFocusPolicy(Qt.NoFocus)

        if not self.UserProfileCreated:
            inventoryButton.clicked.connect(lambda: self.launchWindow(5))
            editDetailsButton.clicked.connect(lambda: self.launchWindow(4))
            requestButton.clicked.connect(lambda: self.launchWindow(3))
            resetPinButton.clicked.connect(lambda: self.launchWindow(1))
            cartButton.clicked.connect(lambda: self.launchWindow(6))
            logoutButton.clicked.connect(lambda:self.logoutUser())
            self.UserProfileCreated=True
        
        for i in self.user.getName().split(' '):
            if len(i)>3:
                username=i
                break
        welcomeLabel.setText("Welcome, " + username)
        #profilePic.setPixmap(QPixmap(self.userImagePath + self.userImagesPrefix + \
                                    #str(self.user.getUserId()) + '.jpg'))
        userImagePath = self.userImagePath + self.userImagesPrefix + \
                                    str(self.user.getUserId()) + '.jpg'
        if QFile.exists(userImagePath):
            profilePic.setPixmap(QPixmap(userImagePath))
        else:
            profilePic.setPixmap(QPixmap('images/default_user.png'))

    def setupResetPin(self):
        if not self.ResetPinCreated:
            Ui_resetPinWindow().setupUi(self.resetPin)
            
        buttonBox = self.resetPin.findChild(QDialogButtonBox, "buttonBox")
        currentPwd = self.resetPin.findChild(QLineEdit, "currentPwd")
        newPwd = self.resetPin.findChild(QLineEdit, "newPwd")
        self.resetPinScroller.addWidget(self.resetPin)
        if not self.ResetPinCreated:
            buttonBox.accepted.connect(lambda: self.execResetPin(currentPwd.text(), newPwd.text()))
            buttonBox.rejected.connect(lambda: self.launchWindow(0))
            self.ResetPinCreated=True

    def setupFinger(self):
        if not self.FingerCreated:
            Ui_loginWindow().setupUi(self.finger)
            self.FingerCreated=True
        fingerLabel = self.finger.findChild(QLabel, "fingerLabel")
        layout = self.finger.findChild(QVBoxLayout,'verticalLayout')
        layout.setAlignment(fingerLabel, Qt.AlignHCenter|Qt.AlignVCenter)
        # fingerData = None
        self.scanFingerprint = QMovie("images/finger-scan.gif")
        self.scanFingerprint.setScaledSize(QSize(320, 240))
        fingerLabel.setMovie(self.scanFingerprint)

        

    def gotResult(self, myresult):
        print(myresult)
        print(threading.current_thread())
        self.userIdSignal.emit(myresult)

    def handleAction(self, myresult):
        print(threading.current_thread())
        print("THERESULT")
        print(myresult)
        if myresult != -1:
            userInfo = user_info(self.databasePath)
            userData = userInfo.get_user_info(myresult)
            self.user = userDetails(userData[0], myresult, userData[5], userData[6], userData[7])
            self.setupWindows()
            self.HomeWidget.setCurrentIndex(1)
        else:
            # self.finger = QWidget()
            self.logoutUser()

    # Fingerprint login is supported here. We only take the sensor's word
    # for whether the fingerprint provided is valid.
    def unlockScreen(self):
        if self.fprintEnabled == True:
            print(threading.current_thread())
            self.fingerprintObject = fsensor(self.sensorPath, self.baudRate)
            self.scanFingerprint.start()
            self.HomeWidget.setCurrentIndex(3)
            self.scanThread.apply_async(self.scanFinger, callback=self.gotResult)
        else:
            self.HomeWidget.setCurrentIndex(1)

    def scanFinger(self):
        correctFingerprint = QPixmap("images/finger-correct.gif")
        wrongFingerprint = QPixmap("images/finger-wrong.gif")
        print(threading.current_thread())

        fingerLabel = self.finger.findChild(QLabel, "fingerLabel")
        # loggedIn = False
        # while(loggedIn == False):
        fingerId = self.fingerprintObject.Search()
        if (fingerId == None):
            print('NOT FOUND')
            fingerLabel.setPixmap(wrongFingerprint)
            time.sleep(1)
            return -1
        else:
            print('FOUND:'+str(fingerId))
            fingerLabel.setPixmap(correctFingerprint)
            time.sleep(1)
            userInfoObject = user_info(self.databasePath)
            # loggedIn = True
            self.userId = userInfoObject.identify_user(fingerId)
            return self.userId
            # print(fingerId)
            # # fingerData = fingerId
            # self.HomeWidget.setCurrentIndex(1)

    def setupRequestItem(self):
        if not self.RequestItemCreated:
            Ui_requestItemWindow().setupUi(self.requestItem)
            
        project = self.requestItem.findChild(QLineEdit, "project")
        item = self.requestItem.findChild(QLineEdit, "item")
        price = self.requestItem.findChild(QLineEdit, "price")
        requestItemButton = self.requestItem.findChild(QPushButton, "requestItemButton")
        buttonBox = self.requestItem.findChild(QDialogButtonBox, "buttonBox")
        
        self.requestItemScroller.addWidget(self.requestItem)
        
        #self.requestItem.setFixedSize(1119,629)
        #parent = QWidget()
        #self.requestItem.setParent(parent)
        #parent.setFixedSize(1119,1200)
        #self.RequestItemScroller = QScrollArea()
        #parent.setFocusPolicy(Qt.NoFocus)
        #self.requestItemScroller.setFocusPolicy(Qt.NoFocus)
        #self.requestItemScroller.setWidget(parent)
        #self.requestItemScroller.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        #self.requestItemScroller.setWidgetResizable(True)
        #self.requestItemScroller.setFrameShape(QFrame.Box)
        #self.requestItemScroller.setLineWidth(0)
        #self.requestItemScroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        purchaseRequest = purchaseRequests(self.databasePath)
        if not self.RequestItemCreated:
            buttonBox.accepted.connect(lambda: (purchaseRequest.addToTable(self.user.getUserId(), \
                                        str(project.text()), str(price.text()), \
                                        str(item.text()), 1000),
                                        self.showMsgBox('Request submitted!')))
            buttonBox.rejected.connect(lambda: self.launchWindow(0))
            self.RequestItemCreated=True

    def setupEditDetails(self):
        if not self.EditDetailsCreated:
            Ui_editDetailsWindow().setupUi(self.editDetails)
            
        buttonBox = self.editDetails.findChild(QDialogButtonBox, "buttonBox")
        if not self.EditDetailsCreated:
            buttonBox.rejected.connect(lambda: self.launchWindow(0))
            buttonBox.accepted.connect(lambda: self.saveUserDetails(self.user.getUserId()))
            buttonBox.accepted.connect(lambda: self.showMsgBox('Database successfully updated!'))
            buttonBox.accepted.connect(lambda: self.launchWindow(0))
            self.EditDetailsCreated=True
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
        self.editDetailsScroller.addWidget(self.editDetails)
    def setupInventory(self):
        if not self.InventoryCreated:
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
        if not self.InventoryCreated:
            categoryView.clicked.connect(self.updateInventoryItemList)
            itemView.clicked.connect(self.updateInventoryItemInfo)
            cartButton.clicked.connect(lambda: self.launchWindow(6))
            addToCartButton.clicked.connect(lambda: self.addToCartAction(itemView, qtySpinBox, partQty))
            self.InventoryCreated=True

    def setupCart(self):
        if not self.CartCreated:
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
        if not self.CartCreated:
            removeCartButton.clicked.connect(lambda: self.removeFromCartAction(listView, int(str(partID.text()))))
            listView.clicked.connect(self.displayCartItem)
            openInventory.clicked.connect(lambda: self.launchWindow(5))
            self.CartCreated=True

    def setupAdmin(self):
        if not self.AdminCreated:
            Ui_adminWindow().setupUi(self.admin)
            
        enrolUserButton = self.admin.findChild(QPushButton, "enrolUserButton")
        editUsersButton = self.admin.findChild(QPushButton, "editUsersButton")
        restartButton = self.admin.findChild(QPushButton, "pushButton_2")
        exitButton = self.admin.findChild(QPushButton, "pushButton_3")
        shutDownButton = self.admin.findChild(QPushButton, "pushButton_4")

        for i in [restartButton,exitButton,shutDownButton]:
            i.setFixedWidth(150)
            print(i.size())
            
        if not self.AdminCreated:
            enrolUserButton.clicked.connect(lambda: self.launchWindow(8))
            editUsersButton.clicked.connect(lambda: self.launchWindow(9))
            restartButton.clicked.connect(lambda: powerDown(True))
            exitButton.clicked.connect(lambda: app.exit())
            shutDownButton.clicked.connect(lambda: powerDown(False))
            self.AdminCreated=True
 

    def launchEnrolFingerprint(self):
        self.launchWindow(10)
        self.setupEnrolFingerprint()

    def setupEnrol(self):
        if not self.EnrolCreated:
            Ui_enrolWindow().setupUi(self.enrol)
            
        self.enrollUserObject = enrollUser(self.databasePath)
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
        self.enrolScroller.addWidget(self.enrol)
        if not self.EnrolCreated:
            biometricButton.clicked.connect(lambda: self.launchEnrolFingerprint())
            buttonBox.rejected.connect(lambda: self.launchWindow(0))
            if self.user.isAdmin() == True:
                buttonBox.rejected.connect(lambda: self.launchWindow(0))
                buttonBox.accepted.connect(lambda: self.saveEnrolUser(str(name.text()),str(email.text()), str(phoneCall.text()), \
                                                                str(phoneWhatsApp.text()), str(roomNumber.text()), \
                                                                str(pin.text()),  adminPriv.isChecked(), \
                                                                labAccess.isChecked(), inventoryAccess.isChecked()))
    
                #buttonBox.accepted.connect(lambda: self.enrollUserObject.storeFingerprint(userInfoObject.getUserID(), self.ftemplate[0], self.ftemplate[1]))
                #buttonBox.accepted.connect(lambda: self.fingerprintObject.SetTemplate(self.ftemplate[1],self.ftemplate[0]))
                #buttonBox.accepted.connect(lambda: self.showMsgBox('Database successfully updated!'))
                #buttonBox.accepted.connect(lambda: self.launchWindow(0))
            else:
                buttonBox.rejected.connect(lambda: self.launchWindow(0))
                buttonBox.accepted.connect(lambda: self.showMsgBox('You are not authorized to do this!'))
            self.EnrolCreated=True

    def saveEnrolUser(self,name,email,phoneCall,phoneWhatsapp,roomNumber,pin,adminAccess,labAccess,inventoryAccess):
        if self.enrollUserObject.enrollNewUser(name,email,phoneCall,phoneWhatsapp,roomNumber,pin,adminAccess,labAccess,inventoryAccess):
            if (not self.ftemplate==None) and (self.fingerprintObject.SetTemplate(self.ftemplate[1],self.ftemplate[0])==True):
                self.enrollUserObject.storeFingerprint(self.userInfoObject.getUserID(), self.ftemplate[0], self.ftemplate[1])
            else:
                print('fingerprint not stored')
            self.showMsgBox('Database successfully updated!')
            #clear the stored template from memory
            self.ftemplate=None
            self.userListChanged.emit()
            self.launchWindow(0)
        else:
            self.showMsgBox('Invalid Values!')

    def updateUserList(self):
        print('resetting')
        self.userModel.clear()
        self.userList = self.editUsersObject.listUser()
        for item in self.userList:
            self.userModel.appendRow(QStandardItem(item[1]))
        self.updateEditUserInfo(None)

    def setupEditUsers(self):
        if not self.EditUsersCreated:
            Ui_editUsersWindow().setupUi(self.editUsers)
            
        self.editUsersObject = editUsers(self.databasePath)
        self.userInfoObject = user_info(self.databasePath)

        username = self.editUsers.findChild(QLabel, "username")
        name = self.editUsers.findChild(QLineEdit, "name")
        email = self.editUsers.findChild(QLineEdit, "email")
        phoneCall = self.editUsers.findChild(QLineEdit, "phoneCall")
        phoneWhatsApp = self.editUsers.findChild(QLineEdit, "phoneWhatsApp")
        roomNumber = self.editUsers.findChild(QLineEdit, "roomNumber")

        adminCheckBox = self.editUsers.findChild(QCheckBox, "adminCheckBox")
        labCheckBox = self.editUsers.findChild(QCheckBox, "labCheckBox")
        inventoryCheckBox = self.editUsers.findChild(QCheckBox, "inventoryCheckBox")

        biometricButton = self.editUsers.findChild(QPushButton, "biometricButton")
        saveButton = self.editUsers.findChild(QPushButton, "saveButton")
        deleteButton = self.editUsers.findChild(QPushButton, "deleteButton")
        deleteButton.setStyleSheet('QPushButton {background-color:#aa0000;color:white;border-width: 1px;border-color: #339;border-style: solid;border-radius: 8;padding: 10px}\nQPushButton:pressed{background:royalblue;border-color:royalblue;border-width:2px}')
        userImage = self.editUsers.findChild(QLabel, "userImage")
        
        userView = self.editUsers.findChild(QListView, "userView")
        self.userList = self.editUsersObject.listUser()
        self.userModel = QStandardItemModel()
        userView.setModel(self.userModel)
        
        
        userImage.setPixmap(QPixmap('images/default_user.png'))
        
        for item in self.userList:
            self.userModel.appendRow(QStandardItem(item[1]))

        self.ftemplate = None
        self.updateUserList()
        
        self.editUsersScroller.addWidget(self.editUsers)
        
        if not self.EditUsersCreated:
            biometricButton.clicked.connect(lambda: self.launchEnrolFingerprint())
            userView.clicked.connect(self.updateEditUserInfo)
            if self.user.isAdmin() == True:
                saveButton.clicked.connect(lambda: self.saveEditUsers(self.selectedUserId,str(name.text()),str(email.text()),str(phoneCall.text()),str(phoneWhatsApp.text()), str(roomNumber.text()),adminCheckBox.isChecked(), labCheckBox.isChecked(), inventoryCheckBox.isChecked()))
                deleteButton.clicked.connect(lambda: self.deleteUser(self.selectedUserId))
            else:
                saveButton.clicked.connect(lambda: self.showMsgBox('You are not authorized to do this!'))
                deleteButton.clicked.connect(lambda: self.showMsgBox('You are not authorized to do this!'))
            self.EditUsersCreated=True
    def saveEditUsers(self,userId,name,email,phoneCall,phoneWhatsapp,roomNumber,adminAccess,labAccess,inventoryAccess):
        if (self.editUsersObject.updateUser([name,email,phoneCall,phoneWhatsapp,roomNumber],userId)):
            self.editUsersObject.adminAccess(userId,adminAccess,labAccess,inventoryAccess)
            if not self.ftemplate==None:
                if self.userInfoObject.getFingerID(userId)==None:
                    print('new finger enrollment')
                    if self.fingerprintObject.SetTemplate(self.ftemplate[1],self.ftemplate[0])==True:
                        self.enrollUserObject.storeFingerprint(userId, self.ftemplate[0], self.ftemplate[1])
                    else:
                        print("enroll to sensor failed")
                else:
                    print('modifying fingerprint '+str(self.userInfoObject.getFingerID(userId)))
                    self.fingerprintObject.DeleteID(self.userInfoObject.getFingerID(userId))
                    if self.fingerprintObject.SetTemplate(self.ftemplate[1],self.userInfoObject.getFingerID(userId))==True:
                        self.editUsersObject.modifyFingerprint(userId, self.ftemplate[1])
                    else:
                        print("enroll to sensor failed")
                self.ftemplate=None
            self.showMsgBox('Database successfully updated!')
        else:
            self.showMsgBox('Database update Failed!/n Invalid Data Entered')

    def deleteUser(self,userId):
        print('called')
        
        if userId == self.user.getUserId():
            self.showMsgBox('You can\'t delete yourself!')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Are you sure you want to delete this user?')
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            ret = msg.exec_()
            
            if ret == QMessageBox.Ok:            
                self.editUsersObject.deleteUser(userId)
                finger_id=self.userInfoObject.getFingerID(userId)
                if not finger_id==None:
                    self.fingerprintObject.DeleteID(finger_id)
                self.userListChanged.emit()

    def updateEditUserInfo(self, nameId):
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
        
        #this part resets all the selected user's details in editusers after deleteUser
        if nameId==None:
            print("resetting list")
            username.setText("UserID")
            name.setText("")
            email.setText("")
            phoneCall.setText("")
            phoneWhatsApp.setText("")
            roomNumber.setText("")
            #userImage.setPixmap(QPixmap(self.userImagePath + self.userImagesPrefix + \
                                        #str(self.selectedUserId) + '.jpg'))
            adminCheckBox.setChecked(False)
            labCheckBox.setChecked(False)
            inventoryCheckBox.setChecked(False)
            return
            
        print(self.userModel.item(nameId.row()).text())
        self.selectedUserId = self.userList[nameId.row()][0]
        res = self.userInfoObject.get_user_info(self.selectedUserId)

        username.setText('User:'+str(self.selectedUserId))
        name.setText(res[0])
        email.setText(res[4])
        phoneCall.setText(res[1])
        phoneWhatsApp.setText(res[2])
        roomNumber.setText(res[3])
        userImagePath = self.userImagePath + self.userImagesPrefix + \
                                    str(self.selectedUserId) + '.jpg'
        if QFile.exists(userImagePath):
            userImage.setPixmap(QPixmap(userImagePath))
        else:
            userImage.setPixmap(QPixmap('images/default_user.png'))
        #userImage.setPixmap(QPixmap(self.userImagePath + self.userImagesPrefix + \
                                    #str(self.selectedUserId) + '.jpg'))
        #userImagePath = self.userImagePath + self.userImagesPrefix + \
                                    #str(self.selectedUserId) + '.jpg'
        #if QFile.exists(userImagePath):
            #userImage.setPixmap(QPixmap(userImagePath))
        #else:
            #userImage.setPixmap(QPixmap('images/default_user.png'))
        adminCheckBox.setChecked(res[5])
        labCheckBox.setChecked(res[6])
        inventoryCheckBox.setChecked(res[7])
        self.ftemplate=None

    def setupEnrolFingerprint(self):
        if not self.EnrolFingerprintCreated:
            Ui_enrolFingerWindow().setupUi(self.enrolFingerprint)
            
        fingerprintWidgets = []
        fingerprintWidgets.append(self.enrolFingerprint.findChild(QLabel, "fprint1"))
        fingerprintWidgets.append(self.enrolFingerprint.findChild(QLabel, "fprint2"))
        fingerprintWidgets.append(self.enrolFingerprint.findChild(QLabel, "fprint3"))
        exitButton = self.enrolFingerprint.findChild(QPushButton, "exitButton")
        fingerprintButton = self.enrolFingerprint.findChild(QPushButton, "fingerprintButton")
        exitButton.setText('Cancel')
        fingerprintText = self.enrolFingerprint.findChild(QLabel,'label_5')
        
        if not self.EnrolFingerprintCreated:        
            exitButton.clicked.connect(lambda: self.exitFingerEnroll())
            self.EnrolFingerprintCreated=True
            
        for fprint in fingerprintWidgets:
            # fprint.setMovie(scanFingerprint)
            fprint.setPixmap(QPixmap("images/fingerprint-icon.jpg"))
        finger_ids=dbs.selectQuery('fingerprint',['FINGERPRINT_ID'])
        finger_ids=set([i[0] for i in finger_ids])
        all_index=set(range(0,200))
        index=min(all_index-finger_ids)
        print(index)

        # self.fingerprintObject = fsensor(self.sensorPath, self.baudRate)
        self.fingerprintObject.resetEnrollIndex()

        scanFingerprint = QMovie("images/finger-scan.gif")
        scanFingerprint.setScaledSize(QSize(320, 240))

        threads=[]
        self.fingerprintObject.stop=False
        self.ftemplate=None
        t=Thread(target=self.setFingerprintStates,args=(fingerprintWidgets,index,scanFingerprint,threads,fingerprintText,))
        threads.append(t)
        # fingerprintWidgets[0].setMovie(scanFingerprint)
        self.fingerScanning=True
        t.start()
    
    #textbox has to be passed to the new threads,spawned wth setFingerStates()
    def setFingerprintStates(self, fingerprintWidgets,index,scanFingerprint,threads,textBox):
        curr_enroll=self.fingerprintObject.getCurrentEnrollIndex()
        
        textBox.setText('Place your finger on the sensor (%s/3)'%(curr_enroll+1))
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
                t=Thread(target=self.setFingerprintStates,args=(fingerprintWidgets,index,scanFingerprint,threads,textBox,))
                threads.append(t)
                t.start()
                return
            elif curr_enroll==2:
                self.fingerScanning=False
                template=self.fingerprintObject.GetTemplate(index)[1]
                self.fingerprintObject.DeleteID(index)
                self.ftemplate=[index,template]
            else:
                pass
        else:
            print("sensor response"+str(ret))
            self.exitFingerEnroll()
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
        #if not self.fingerScanning:
            #self.setupEnrolFingerprint()
            
        #else:
            #button.setText('Retry')
        self.fingerprintObject.stop=True
        self.fingerScanning=False
        print("stopping enrollment")
        

    def removeFromCartAction(self, listView, partID):
        if len(listView.selectedIndexes()) != 0:
            self.viewCart.removeFromCart(self.user.getUserId(), partID)
            self.updateViewCart()


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
        #else:
            #self.showMsgBox('Enter Current Password')

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
        if len(self.previousPage) and value==self.previousPage[-1]:
            self.goBack()
            return
        self.previousPage.append(self.StackWidget.currentIndex())
        self.StackWidget.setCurrentIndex(value)
        self.currentPage = value
        self.updateViewCart()

    def goBack(self):
        if (self.StackWidget.currentIndex()==10) and self.fingerScanning:
            return
        if len(self.previousPage):
            self.StackWidget.setCurrentIndex(self.previousPage[-1])
            self.previousPage.pop(-1)
        else:
            pass
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
            
    def logoutUser(self):
        self.HomeWidget.setCurrentIndex(0)
        self.user=None
        self.previousPage=[]
        self.currentPage=0
        self.setupFinger()
        
def powerDown(restart):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText('Are you sure you want to '+('restart' if restart else 'shut down')+('?'))
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    ret = msg.exec_()
    if ret == QMessageBox.Ok:
        if restart:
            os.system('sudo reboot')
        else:
            os.system('sudo halt')
    else:
        pass
def handleFocus(old,new):
    if type(new)==QLineEdit:
        os.system('florence show')
        ScrollArea.setScrolling(True)
    elif (not type(new)==QLineEdit) and type(old)==QLineEdit:
        os.system('florence hide')
        ScrollArea.setScrolling(False)
    else:
        pass

def startApp():
    global prog
    prog=mainWindow()
    if prog.getDevice() == 'desktop':
        prog.windowWidget.show()
    else:
        
        prog.windowWidget.showMaximized()
        #prog.windowWidget.showFullScreen()  
        



def main():
    global app,prog
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('images/arclogo.png'))
    app.setOverrideCursor(QCursor(Qt.BlankCursor))
    app.focusChanged.connect(handleFocus)
    #widget = QWidget()
    startApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
