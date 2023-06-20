from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import sys

class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setupUI()

    def setupUI(self):

        listWidget = QListWidget(self)
        listWidget.setAlternatingRowColors(True)

        itemA = QListWidgetItem()
        itemA.setText("A")

        listWidget.addItem(itemA)
        listWidget.addItem("B")

        layout = QVBoxLayout(self)
        layout.addWidget(listWidget)

        itemC = QListWidgetItem()
        itemC.setText('C')

        #삽입(0,1,2 ...)
        listWidget.insertItem(1, itemC)
        listWidget.insertItem(3, 'D')

        #꺼내기
        take = listWidget.takeItem(3)
        #꺼낸거 넣기
        listWidget.insertItem(0, take)
        
        listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        listWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.acceptDrops)

        itemE = QListWidgetItem()
        itemE.setFlags(itemE.flag()|Qt.ItemIsEditable)
        itemE.setText('E')

        listWidget.addItem(itemE)

        listWidget.setDragEnabled(True)
        listWidget.viewport().setAcceptDrops(True)
        listWidget.setDropIndicatorShown(True)
        listWidget.setDefaultDropAction(Qt.MoveAction)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()