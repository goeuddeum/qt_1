import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

if __name__=='__main__':
    app = QApplication(sys.argv)

    form = QWidget()

    spin = QSpinBox()
    spin.setRange(0,100)
    

    slider = QSlider(Qt.Horizontal)
    slider.setRange(0,100)
    

    progressBar = QProgressBar()
    progressBar.setAlignment(Qt.AlignCenter)
    progressBar.setRange(0,100)

    spin.valueChanged.connect(slider.setValue)
    spin.valueChanged.connect(progressBar.setValue)
    progressBar.valueChanged.connect(spin.setValue)

    layout = QHBoxLayout()
    layout.addWidget(spin)
    layout.addWidget(slider)
    layout.addWidget(progressBar)

    form.setLayout(layout)
    form.setWindowTitle('SpinSliderProgressDemo')
    

    form.show()

    QApplication
    screens = QApplication.screens()
    print('screens: ',screens)

    formSize = form.sizeHint()
    print('formSize: ', formSize)

    screenSize = screens[1].availableSize()

    # screenSize = QApplication.primaryScreen().availableSize()
    print('screenSize: ',screenSize)

    #form.move(screenSize//2)
    form.move((screenSize.width()//2) * (formSize.width()//2),
              (screenSize.heigh()//2) * (formSize.height()//2)
              )


    app.exec_()
