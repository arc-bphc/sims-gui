from PyQt4 import QtCore, QtGui
from ui_resetpin import Ui_resetPinWindow

class requestItemWindow(Ui_resetPinWindow):
    def __init__(self, widget):
        Ui_resetPinWindow.__init__(self)
        self.setupUi(widget)
