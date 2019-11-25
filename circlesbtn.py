import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint as r


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.run)
        self.show()

    def run(self):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(250, 218, 94))
        qp.drawEllipse(r(0, 700), r(0, 500), r(10, 400), r(10, 400))
        qp.end()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
