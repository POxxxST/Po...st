#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Example(QWidget):
    btn_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['CE', 'C', '<-', '**',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            self.button = QPushButton(name)
            self.button.clicked.connect(self.namber_click)

            grid.addWidget(self.button, *position)

    def namber_click(self):
        sender = self.sender()
        self.btn_clicked.emit(sender.text())


class ExampleProg(QWidget):
    btn_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['bin', 'oct', 'hex', 'fib',
                'CE', 'C', '<-', '**',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(6) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            self.button = QPushButton(name)
            self.button.clicked.connect(self.namber_click)

            if name == 'bin':
                self.button.setToolTip("преобразование целого числа в двоичную систему")
            elif name == 'oct':
                self.button.setToolTip("преобразование целого числа в восьмеричную систему")
            elif name == 'hex':
                self.button.setToolTip("преобразование целого числа в шестнадцатеричную систему")
            elif name == 'fib':
                self.button.setToolTip("преобразование целого числа в число фибоначи")

            grid.addWidget(self.button, *position)

    def namber_click(self):
        sender = self.sender()
        self.btn_clicked.emit(sender.text())


class ExampleGeomet(QWidget):
    btn_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['cos', 'sin', 'tan', 'fac',
                'CE', 'C', '<-', '**',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(6) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            self.button = QPushButton(name)
            self.button.clicked.connect(self.namber_click)
            if name == 'cos' or name == 'sin' or name == 'tan':
                self.button.setToolTip("X указывается в радианах")
            elif name == 'fac':
                self.button.setToolTip('факториал числа')
            grid.addWidget(self.button, *position)

    def namber_click(self):
        sender = self.sender()
        self.btn_clicked.emit(sender.text())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())