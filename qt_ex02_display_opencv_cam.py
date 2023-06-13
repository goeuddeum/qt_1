import typing
import cv2
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QFrame, QSizePolicy, QPushButton,
    QFileDialog, QMessageBox)
from PySide2.QtGui import QPixmap, QImage
import sys

import cv2
import numpy as np

class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('Cam viewer')

        self.imageLabel = QLabel()
        self.imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setPixmap(QPixmap())

        layout = QVBoxLayout()
        layout.addWidget(self.imageLabel)

        self.setLayout(layout)
        self.resize(QApplication.primaryScreen().availableSize() * 2 / 5)
 
    def displayCam(self):
        cap = cv2.VideoCapture(0)

        if cap.isOpened():
            while True:
                ret, frame = cap.read()
                
                if not ret:
                    break

                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, c = img.shape
                qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qImg)

                self.imageLabel.setPixmap(pixmap)
                #QApplication.processEvents()  # 이벤트 루프를 처리하기 위해 추가

               # if cv2.getWindowProperty('Cam viewer', cv2.WND_PROP_VISIBLE) < 1:  # 'Cam viewer' 창이 닫히면 종료
                #    break


        cap.release()
        #cv2.destroyAllWindows()
        cv2.waitKey(0)
        cv2.destroyWindow('Cam viewer')
        while cv2.getWindowProperty('Cam viewer', cv2.WND_PROP_VISIBLE) >= 1:
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    window.displayCam()

    sys.exit(app.exec_())
