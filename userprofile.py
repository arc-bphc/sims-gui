from PyQt4 import QtCore, QtGui
from ui_userprofile import Ui_userWindow
from inventorywindow import inventoryWindow
from editdetailswindow import editDetailsWindow
class userProfile(Ui_userWindow):
    def __init__(self, widget):
        Ui_userWindow.__init__(self)
        self.setupUi(widget)

        self.inventoryButton.clicked.connect(lambda: self.launchInventory(widget))
        self.editDetailsButton.clicked.connect(lambda: self.launchEditDetails(widget))

        self.winddowWidget = QtGui.QMainWindow()
        self.childWidget = QtGui.QWidget()

    def launchInventory(self, widget):
        prog = inventoryWindow(self.winddowWidget)
        self.winddowWidget.show()
        widget.close()
    def launchEditDetails(self, widget):
        prog = editDetailsWindow(self.childWidget)
        self.childWidget.show()
        widget.close()
