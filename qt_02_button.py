import PySide2.QtCore
from PySide2.QtWidgets import (
    QApplication,QWidget,QPushButton,
    QCheckBox,QRadioButton,QVBoxLayout,QGroupBox)

import sys

class MyForm(QWidget):
    def __init__(self, parent=None):
        # 부모(Qwidget)이 기본 가져야할 값을 초기화        
        QWidget.__init__(self,parent)

        # Qt

        self.setWindowTitle('Button Demo')
        #self.resize(500,500)
        
        # 푸시버튼(클릭 가능 버튼)
        self.button = QPushButton('&Ok', self )
        self.button.clicked.connect(self.okButtonClicked)
        # 체크박스
        self.checkBox = QCheckBox('&Case sensitivity',self)
        self.checkBox.toggled.connect(self.onCaseSensitivity)
        # 라디오버튼
        box = QGroupBox('sex', self)
        self.radioButton1 = QRadioButton("Male",box)
        self.radioButton2 = QRadioButton("Female",box)
        self.radioButton1.setChecked(True)
        ## 라디오버튼 레이아웃
        groupBoxlayout = QVBoxLayout(box)
        groupBoxlayout.addWidget(self.radioButton1)
        groupBoxlayout.addWidget(self.radioButton2)
        self.radioButton1.toggled.connect(self.onMale)

        # 레이아웃
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.button)
        mainlayout.addWidget(self.checkBox)
        mainlayout.addWidget(box)        

        self.setLayout(mainlayout)
    
    def okButtonClicked(self):
        print('okButtonClicked')

    def onCaseSensitivity(self, toggle):
        print('onCaseSeonsitivity',toggle)

    def onMale(self,toggle):
        print('onMale',toggle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    form = MyForm()
    form.show()
    
    app.exec_()