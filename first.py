import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class New(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('u1.ui', self)
        self.setWindowTitle('Окружности')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        self.li = []

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.new(qp)
            qp.end()

    def paint(self):
        col = (randint(0, 255), randint(0, 255), randint(0, 255))
        x = randint(0, 900)
        y = randint(0, 500)
        r = randint(0, 250)
        he = [col, x, y, r]
        self.li.append(he)
        self.do_paint = True
        self.repaint()

    def new(self, qp):
        # Задаем кисть

        for el in self.li:
            qp.setBrush(QColor(*el[0]))
            x = el[1]
            y = el[2]
            r = el[3]
            qp.drawEllipse(x, y, r, r)




