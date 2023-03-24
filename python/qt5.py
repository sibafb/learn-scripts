import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
   


class Test(QMainWindow):
    def __init__(self):
        super().__init__()

        #ref https://www.geeksforgeeks.org/set-title-of-window-in-pyqt5-setwindowtitle/
        title = "hello"
        self.setWindowTitle(title)
        self.setGeometry( 0, 0, 500, 300)

        # Qpushbutton API　https://www.pythonguis.com/docs/qpushbutton/
        # PyQt5　push button tutorial https://www.delftstack.com/ja/tutorial/pyqt5/pyqt5-push-button/
        self.buttonA = QPushButton('Click!!', self)
        # change coloer
        self.buttonA.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        # push event
        self.buttonA.clicked.connect(self.clickCallback)
        self.buttonA.move(100, 50)
        self.buttonClicked = 0
        
        self.labelA = QLabel(self)
        self.labelA.move(110, 100)

        self.buttonClicked = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeoutCallback)
        self.countDown = 0

        self.setGeometry(100, 100, 300, 200)

        self.show()

    def clickCallback(self):
        # setClilckText
        self.buttonClicked += 1
        self.buttonA.setText("clicked : " + str(self.buttonClicked))

        # setLabelText setTimer
        self.timer.start(1000)#ms
        self.countDown = 10
        self.labelA.setText(("Button is clicked!" + str(self.countDown)))

    def timeoutCallback(self):
        if self.countDown > 0 :
            self.timer.start(1000)#ms
            self.countDown -= 1
            self.labelA.setText((""))
        else :
            self.labelA.setText(("Button is clicked!" + str(self.countDown)))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    test = Test()

    sys.exit( app.exec_() )