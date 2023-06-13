from PySide2.QtWidgets import *
#import PySide2.QtWidgets

import sys

if __name__ == '__main__':
    
    #window라는 이름의 QWidget 클래스 (class)의 객체(Obhject) 생성(인스턴스) 
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(289,170)
    window.setWindowTitle('첫번째 프로그램')


    #label라는 이름의 Qlabel클래스의 객체생성
    label = QLabel('Hello Qt') #상위 위젯 설정, 위젯이 소속된 공간
    label.setParent(window) 
    label.move(110,80) #위치정의
    label.setText('jkon')
    
    # 화면에 표시
    window.show()

    app.exec_()




