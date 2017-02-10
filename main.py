from PyQt4 import QtCore, QtGui
import sys
from ui_mainwindow import Ui_splashScreen
from ui_resetpin import Ui_resetPinWindow

class mainWindow(QtGui.QWidget):
    def __init__(self, widget):
        super(mainWindow, self).__init__()
        self.stack1 = QtGui.QWidget()
        self.x = Ui_resetPinWindow()
        self.x.setupUi(self.stack1)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.stack1)
        #hbox.addWidget(QtGui.QRadioButton("Male"))
        widget.setLayout(hbox)
        print "done"

def main():
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    prog = mainWindow(widget)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
'''
        self.StackedWidget = QtGui.QStackedWidget(self)
        self.StackedWidget.addWidget(self.stack1)

        self.StackedWidget.setCurrentIndex(0)

            def stack1UI(self):
                inst = Ui_resetPinWindow()
                widg = QtGui.QWidget()
                inst.setupUi(widg)
                layout = QtGui.QHBoxLayout()
                layout.addWidget(widg)
                self.stack1.setLayout(layout)

'''
