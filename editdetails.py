from PyQt4 import QtCore, QtGui
from ui_editdetails import Ui_editDetailsWindow

class editDetails(Ui_editDetailsWindow):
    def __init__(self, widget):
        Ui_editDetailsWindow.__init__(self)
        self.setup(widget)
    
