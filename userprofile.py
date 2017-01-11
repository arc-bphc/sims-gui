from PyQt4 import QtCore, QtGui
from ui_userprofile import Ui_userWindow

class userProfile(Ui_userWindow):
    def __init__(self, widget):
        Ui_userWindow.__init__(self)
        self.setupUi(widget)
        self.editDetailsButton.clicked.connect(self.launchEditDetails)
    def launchEditDetails(self):
        print "da"
