from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import serial



class MainWindow(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        

        self.nlineedit = QLineEdit(self)
        # 도~도 7음계 버튼
        self.noteButton1 = QPushButton(self)
        self.noteButton1.clicked.connect(self.send1)
        self.noteButton2 = QPushButton(self)
        self.noteButton2.clicked.connect(self.send2)
        self.noteButton3 = QPushButton(self)
        self.noteButton3.clicked.connect(self.send3)
        self.noteButton4 = QPushButton(self)
        self.noteButton4.clicked.connect(self.send4)
        self.noteButton5 = QPushButton(self)
        self.noteButton5.clicked.connect(self.send5)
        self.noteButton6 = QPushButton(self)
        self.noteButton6.clicked.connect(self.send6)
        self.noteButton7 = QPushButton(self)
        self.noteButton7.clicked.connect(self.send7)
        self.noteButton8 = QPushButton(self)
        self.noteButton8.clicked.connect(self.send8)

        layout = QHBoxLayout(self)
        layout.addWidget(self.noteButton1)
        layout.addWidget(self.noteButton2)
        layout.addWidget(self.noteButton3)
        layout.addWidget(self.noteButton4)
        layout.addWidget(self.noteButton5)
        layout.addWidget(self.noteButton6)
        layout.addWidget(self.noteButton7)
        layout.addWidget(self.noteButton8)
        layout.addWidget(self.nlineedit)
        self.noteButton1

    def send1(self):
        inputText = self.nlineedit.text()
        print('inputText:', inputText)
        self.nlineedit.setText('1')
    def send2(self):
        inputText = self.inputLineEdit.text()
    def send3(self):
        inputText = self.inputLineEdit.text()
    def send4(self):
        inputText = self.inputLineEdit.text()
    def send5(self):
        inputText = self.inputLineEdit.text()
    def send6(self):
        inputText = self.inputLineEdit.text()
    def send7(self):
        inputText = self.inputLineEdit.text()
    def send8(self):
        inputText = self.inputLineEdit.text()


        self.resize(500,500)


PORT = '/dev/ttyUSB0'
def prepare():

    global ser

    ser = serial.serial_for_url(PORT, baudrate=9600, timeout=1)
        

if __name__ == '__main__':
    prepare()
    app = QApplication(sys.argv)



    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()
