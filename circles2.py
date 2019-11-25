import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('draw')
        btn = QPushButton('push', self)
        btn.resize(50, 30)
        btn.move(5, 5)
        self.show()


    def run(self):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(r(0, 255), r(0, 255), r(0, 255)))
        qp.drawEllipse(r(0, 700), r(0, 500), r(10, 400), r(10, 400))
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())