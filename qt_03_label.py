import typing
from PySide2.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,
    QLabel,QFrame,QSizePolicy,QPushButton,
    QFileDialog,QMessageBox)
from PySide2.QtGui import QPixmap,QImage
import sys

class MainWindow(QWidget):

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle('Image viewer')

        self.imageLabel = QLabel()
        self.imageLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setPixmap(QPixmap())

        openButton = QPushButton('Load Image')
        openButton.clicked.connect(self.open)

        layout = QVBoxLayout()
        layout.addWidget(self.imageLabel)
        layout.addWidget(openButton)
        # 해당 위젯(윈도우)의 크기를 전체크기의 2배 5분의1로 표시
        self.setLayout(layout)
        self.resize(QApplication.primaryScreen().availableSize()*2/5)

        #primaryScreenSize=QApplication.primaryScreen().availableSize()
        #primaryScreenSize.setWidth(primaryScreenSize.width() /5)
        #primaryScreenSize.setHeight(primaryScreenSize.height() /5)
        #self.resize(primaryScreenSize)

    def open(self):
        #QFileDialog (시스템내 파일 탐색 및 읽기가 가능한 창을 호출, 선택한 파일의 경로를 반환)
        fileName, a =QFileDialog.getOpenFileName(self,'open Image File','.','Images (*.png *.xpm *.jpg)')
        print('fileName: ',fileName)
        # 읽어온 파일의 경로를 기반으로 이미지 객체를 구성하여 화면에 표시! (하는 메소드 호출...)
        self.load(fileName)

    def load(self,fileName):

        image = QImage(fileName)
        
        if image.isNull():
            #경고

            QMessageBox.information(
                self,
                QApplication.applicationName(),
                '불러오지 못했습니다.'+ fileName
                )
            self.setwindowTitle("Image viewer")
            self.imageLabel.setPixmap(QPixmap())

            return

        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.setWindowTitle()

if __name__=='__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()
