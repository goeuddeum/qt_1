from PySide2.QtWidgets import *
# from PyQt5.QtWidgets import *

from PySide2.QtGui import *
from PySide2.QtCore import *

import sys
import time
import json


#jsonStr = '''{
#    "author":"goed",
#    "users":[
#        {
#            "id":"yh",
#            "pw":"1234asdf"
#    
#        }
#    ],
#    "userCount":1
#
#}'''

localDatabase = {}

users = []


class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.idLineEdit = QLineEdit(self)
        self.idLineEdit.setPlaceholderText('아이디를 입력')

        # 유효성확인 설정 (영문 대소문자, 4-16자)
        idRegExp = QRegExp('[A-Za-z]{4,16}')
        idValidator = QRegExpValidator(idRegExp, self)
        self.idLineEdit.setValidator(idValidator)

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setPlaceholderText('비밀번호 입력')
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        passwordRegExp = QRegExp('[A-Za-z0-9]{8,20}')
        passwordValidator = QRegExpValidator(passwordRegExp, self)
        self.passwordLineEdit.setValidator(passwordValidator)

        self.visiblePasswordCheckBox = QCheckBox('비밀번호표시', self)
        self.visiblePasswordCheckBox.toggled.connect(self.onToggledPassword)

        # comboBox = QComboBox()

        self.signInButton = QPushButton('로그인', self)
        self.signInButton.clicked.connect(self.onClickSignIn)

        self.signUpButton = QPushButton('등록', self)
        self.signUpButton.clicked.connect(self.onClickSignUp)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.signUpButton)
        buttonLayout.addWidget(self.signInButton)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.idLineEdit)
        mainLayout.addWidget(self.passwordLineEdit)
        mainLayout.addWidget(self.visiblePasswordCheckBox)
        mainLayout.addLayout(buttonLayout) #위젯을 추가하는것이 아닌 별도의 레이아웃을 추가

    pass

    def onToggledPassword(self, toggled):
        if toggled:
            self.passwordLineEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordLineEdit.setEchoMode(QLineEdit.Password)

    def onClickSignUp(self):

        inputId = self.idLineEdit.text()
        inputPW = self.passwordLineEdit.text()
        print('onClickSignUp inputId:', inputId)
        print('onClickSignUp inputPW:', inputPW)

        # 등록진행
        self.onSignUp(inputId, inputPW)

    def onSignUp(self, id, pw):

        # 파일db, .json

        # markup -> XML
        # k:v -> json
        # 관계형DB
        # NoSQL

        # [goed]
        # {
        #     "author":"",
        #     "users":[
        #         {
        #             "id":"",
        #             "pw":"",
        #             "created":0,
        #             "modified":0
        #         },
        #         {
        #             "id":"",
        #             "pw":"",
        #             "created":0,
        #             "modified":0
        #         },
        #         {
        #             "id":"",
        #             "pw":"",
        #             "created":0,
        #             "modified":0
        #         }
        #     ]
        # }

        now = time.time()

        user = {
            'id':id,
            'pw':pw,
            'created':now,
            'modified':now,
        }

        # TODO:이미 가입된 사용자가 없는지 확인
        already = False
        for ab in users:
            if ab['id'] == id:
                already = True
                break
        if already:
            print('이미 존재하는 사용자입니다.')
            return

        users.append(user)
        localDatabase['users'] = users

        # TODO:localDatabase -> json 파일로 생성 후 저장
        with open('./db.json', 'w') as f:
            json.dump(localDatabase, f, indent=2)

        pass

    def onClickSignIn(self):
        print('onClickSignIn')

        inputId = self.idLineEdit.text()
        inputPW = self.passwordLineEdit.text()

        print('onClickSignIn inputId:', inputId)
        print('onClickSignIn inputPW:', inputPW)

        self.onSignIn(inputId, inputPW)

        
    #로그인만 처리하는 함수
    def onSignIn(self, id, pw):

        isAuth = False
        for user in users:
            userId = user['id']
            userPw = user['pw']

            if id == userId and pw == userPw:   
                # 인증됨
                isAuth = True
                break
        
        # isAuth 를 기준으로 로그인 상태를 갱신
        print('isAuth: ', isAuth)

        return isAuth


def prepare():
    # 파일데이터를 읽어와 메모리에 준비
    with open('./db.json') as f:
        localDatabase = json.load(f)
        
    #json 포멧의 문자열을 읽어서 파싱하여 딕셔너리 자료형으로 구성
    #localDatabase = json.loads(jsonStr)


    global users
    users = localDatabase.get('users',[])
    print('users', users)

if __name__ == '__main__':
    prepare()
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()