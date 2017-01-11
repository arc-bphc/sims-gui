from PyQt4 import QtCore, QtGui
from ui_inventory import Ui_inventoryWindow

class inventoryWindow(Ui_inventoryWindow):
    def __init__(self, widget):
        Ui_inventoryWindow.__init__(self)
        self.setupUi(widget)
