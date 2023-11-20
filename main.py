from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
from random import randint


class WindowMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        canvas = QPixmap(1000, 1000)
        self.label.setPixmap(canvas)

    def mouseMoveEvent(self, e):
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(225, 225, 0))
        painter.setPen(pen)
        painter.drawEllipse(e.x(), e.y() + 200, randint(1, 100), randint(1, 100))
        painter.end()
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WindowMain()
    ex.show()
    sys.exit(app.exec())