import sys
from PyQt4 import QtCore, QtGui
from pybutton import Ui_Form

class MyGuiProg(Ui_Form):
    def __init__(self, form):
        Ui_Form.__init__(self)
        self.setupUi(form)
        self.pushButton.clicked.connect(self.printMessage)
    def printMessage(self):
        print "hello"

if __name__ == '__main__':
    #print "mainfxn"
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    prog = MyGuiProg(Form)
    Form.show()
    sys.exit(app.exec_())
