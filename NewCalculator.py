#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import MyQLineEdit
import MyButton
import MyButtonProg
import MyCalendar
import os

style = os.path.join(os.path.dirname(__file__), 'style.css')


class MyCalculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def Menu(self):

        combo = QComboBox()
        combo.addItems(["Просто", "Програмист", "Геометрия", "Календарь"])
        combo.activated[str].connect(self.onActivated)

        cb = QCheckBox('Show title', self)
        cb.stateChanged.connect(self.my_style)

        self.QLE = MyQLineEdit.LEdit()

        self.vbox = QVBoxLayout()
        self.vboxDown = QVBoxLayout()
        self.vboxTop = QVBoxLayout()
        self.vboxBot = QHBoxLayout()

        self.vboxDown.addWidget(combo)
        self.vboxDown.addWidget(cb)
        self.vboxTop.addWidget(self.QLE)

        self.vbox.addLayout(self.vboxDown)
        self.vbox.addLayout(self.vboxTop)
        self.vbox.addLayout(self.vboxBot)
        self.vbox.addStretch()

        self.setLayout(self.vbox)
        self.calculate = Calculator(self.QLE)

        self.onActivated('Просто')

    def my_style(self, state):
        if state == Qt.Checked:
            self.setStyleSheet(open(style).read())
        else:
            self.setStyleSheet(None)

    def fun(self, key):
        self.calculate.handle(key)

    def onActivated(self, text):
        if text == 'Просто':
            self.btnMax = MyButton.Example()
            self.vboxBot.addWidget(self.btnMax)
            self.btnMax.btn_clicked.connect(self.fun)
        elif text == 'Програмист':
            self.btnMax = MyButton.ExampleProg()
            self.vboxBot.addWidget(self.btnMax)
            self.btnMax.btn_clicked.connect(self.fun)
        elif text == 'Геометрия':
            self.btnMax = MyButton.ExampleGeomet()
            self.vboxBot.addWidget(self.btnMax)
            self.btnMax.btn_clicked.connect(self.fun)
        elif text == 'Календарь':
            print("Hello")
            self.calen = MyCalendar.Calendar()
            self.vboxBot.addWidget(self.calen)



class Calculator:
    def __init__(self, line_edit):
        self.line_edit = line_edit
        self.state = State1(self)

    def handle(self, key):
        self.state.handle(key)


class State1:
    def __init__(self, calc):
        self.calc = calc
        self.nam = ['<-', '', '+', '-', '*', '/', '**']

    def change_state(self, key):
        if key == '=' or key == 'C' or key == 'CE':
            self.calc.state = State3(self.calc)
            self.calc.handle(key)
        else:
            self.calc.state = State2(self.calc)
            self.calc.handle(key)

    def change_edit(self, key):
        self.calc.line_edit.namber(key)

    def handle(self, key):
        if key.isdigit() or key == '.':
            self.change_edit(key)
        elif key == '=' or key == 'C' or key == 'CE':
            self.change_state(key)
        else:
            for i in self.nam:
                if key == i:
                    self.change_state(key)


class State2:
    def __init__(self, calc):
        self.calc = calc
        self.nam = ['<-', '**', '+', '-', '*', '/']

    def change_state(self, key):
        if key == 'C' or key == 'CE':
            self.calc.state = State3(self.calc)
            self.calc.handle(key)
        else:
            self.calc.state = State1(self.calc)
            self.calc.handle(key)

    def change_edit(self, key):
        if self.calc.line_edit.prov(key):
            if key == '+':
                self.calc.line_edit.operat(key)
            elif key == '-':
                self.calc.line_edit.operat(key)
            elif key == '*':
                self.calc.line_edit.operat(key)
            elif key == '/':
                self.calc.line_edit.operat(key)
            elif key == '<-':
                self.calc.line_edit.back()
            elif key == '**':
                self.calc.line_edit.operat(key)

    def handle(self, key):
        if key.isdigit() or key == '.':
            self.change_state(key)
        elif key == 'C' or key == 'CE':
            self.change_state(key)
        else:
            for i in self.nam:
                if key == i:
                    self.change_edit(key)


class State3:
    def __init__(self, calc):
        self.calc = calc
        self.nam = ['<-', '**', '+', '-', '*', '/']

    def change_state(self, key):
        self.calc.state = State2(self.calc)
        self.calc.handle(key)

    def change_edit(self, key):
        if key == '=':
            self.calc.line_edit.equally(key)
        elif key == 'CE' or key == 'C':
            self.calc.line_edit.namC(key)

    def handle(self, key):
        if key == '=':
            self.change_edit(key)
            self.change_state(key)
        elif key == 'CE' or key == 'C':
            self.change_edit(key)
        elif key.isdigit() or key == '.':
            self.change_state(key)
        else:
            pass


def menu():
    app = QApplication(sys.argv)

    calculator = MyCalculator()
    calculator.Menu()
    calculator.setWindowTitle("CALCULATOR")
    calculator.setGeometry(300, 300, 320, 250)

    calculator.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    menu()
