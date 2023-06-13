from PySide2.QtWidgets import *

import sys

names = (
    '이재권',
    'jkon',
    '권',
    '콘',
    'kon',
    '재권',
)

nameIndex = 0

def onClick():
    global nameIndex

    nameIndex += 1
    label.setText(names[nameIndex])

if __name__ == '__main__':

    global label
    
    app = QApplication(sys.argv)

    #메인윈도우
    window = QWidget()
    window.resize(500,500)
    window.move(500, 500)
    window.setWindowTitle('call myname')
    #메인안에 Qlaabel + Qbutton
    label = QLabel('nameIndex',window)
    button = QPushButton('확인', window)

    layout = QBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)
    
     
    window.show()
    #Qbutton 클릭시 동작할 함수
    button.clicked.connect(onClick)

    app.exec_()
