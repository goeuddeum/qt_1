from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import * 
import sys

items = [
    '사과',
    '두리안',
    '스타후르츠',
    '라임'
]


class MainWindow(QWidget):

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        
        # LineEdit
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setReadOnly(True)

        self.lineEditEditable=QLineEdit(self)
        #self.lineEditEditable.setValidator(QIntValidator(self))
        #self.lineEditEditable.setValidator(QIntValidator(100,999,self))
        #self.lineEditEditable.setValidator(QIntValidator(self))
       #self.lineEditEditable.setValidator(QIntValidator(-0.1,100,2,self))
        
        #validator = QDoubleValidator(self)
        #validator.setDecimals(2)
        #self.lineEditEditable.setValidator(validator)

        #self.lineEditEditable.setPlaceholderText('숫자만 입력해')

        regExp = QRegExp("[A-Za-z][1-9][0-9]{0,2}")

        self.lineEditEditable.setValidator(QRegExpValidator(regExp,self))

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setPlaceholderText("비밀번호를 입력해")
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        # ComboBox
        self.comboBox = QComboBox(self)

        for item in items:
            self.comboBox.addItem(item)

        self.comboBox.setEditable(True)
        self.comboBox.currentIndexChanged.connect(self.onSelected)

        layout = QVBoxLayout(self)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.passwordEdit)
        layout.addWidget(self.comboBox)

        self.resize(500,500)


    def onSelected(self, selected):
        print('selected', selected)
        
        #if selected == 0:
        #    item ='사과'

        item = items(selected)
        print('item',item)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()