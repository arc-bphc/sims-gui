import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QSize

class GifWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('gif')

        label=QLabel(self)
        gif=QMovie('fingerprint-icon-scanning1.gif')
        gif.setScaledSize(QSize(300,300))
        label.setMovie(gif)
        gif.start()

        self.show()

if __name__=='__main__':

    app=QApplication(sys.argv)
    x=GifWindow()
    sys.exit(app.exec_())


        
