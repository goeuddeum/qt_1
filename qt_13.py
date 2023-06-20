from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)

        self.items = []
        self.selection = -1

        layout = QVBoxLayout(self)

        # 리스트위젯
        self.listWidget = QListWidget(self)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.itemSelectionChanged.connect(self.onSelectionItem)
        
        #버튼
        addButton = QPushButton('&Add', self)
        deletButton = QPushButton('&Del', self)
        

        addButton.clicked.connect(self.onClickADD)
        deletButton.clicked.connect(self.onClickDelete)


        buttonlayout = QHBoxLayout()
        buttonlayout.addWidget(addButton)
        buttonlayout.addWidget(deletButton)

        layout.addWidget(self.listWidget)
        layout.addLayout(buttonlayout)

    def onSelectionItem(self,selection):
        self.selection = self.listWidget.currentRow()
    

    def onClickADD(self):
        itemSize = len(self.items)

        content = f'item_{itemSize+1}'
        self.items.append(content)

        listItem = QListWidgetItem(content)
        self.listWidget.addItem(listItem)

        self.listWidget.setCurrentRow(itemSize)
        # self.selection = itemSize
        print('selection: ', self.selection)

    def onClickDelete(self):
        self.listWidget.takeItem(self.selection)
        self.items.pop(self.selection)

        print('selection: ', self.selection)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    Window = MainWindow()
    Window.show()

    app.exec_()