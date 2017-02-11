from PyQt4 import QtCore, QtGui
from ui_requestitem import Ui_requestItemWindow

class requestItemWindow(Ui_requestItemWindow):
    def __init__(self, widget):
        Ui_requestItemWindow.__init__(self)
        self.setupUi(widget)
