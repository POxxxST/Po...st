#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import MyQLineEdit
import MyButton
import os

style = os.path.join(os.path.dirname(__file__), 'style.css')


class MyCalculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def Menu(self):

        combo = QComboBox()
        combo.addItems(["Просто", "Программист", "Геометрия"])
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

        self.btnMax = MyButton.Example()
        self.vboxBot.addWidget(self.btnMax, stretch=1)
        self.btnMax.btn_clicked.connect(self.fun)

        self.btnProg = MyButton.ExampleProg()
        self.vboxBot.addWidget(self.btnProg)
        self.btnProg.btn_clicked.connect(self.fun)

        self.btnGeo = MyButton.ExampleGeomet()
        self.vboxBot.addWidget(self.btnGeo)
        self.btnGeo.btn_clicked.connect(self.fun)

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
            self.btnGeo.hide()
            self.btnProg.hide()
            self.btnMax.show()
        elif text == 'Программист':
            self.btnMax.hide()
            self.btnGeo.hide()
            self.btnProg.show()
        else:
            self.btnProg.hide()
            self.btnMax.hide()
            self.btnGeo.show()


class Calculator:
    def __init__(self, line_edit):
        self.line_edit = line_edit
        self.state = State1(self)
        self.left_operant = 0
        self.right_operant = 0
        self.operator = 0
        self.result = 0
        self.switch = True
        self.switchOper = False
        self.switchSt4 = True

    def handle(self, key):
        if key.isdigit() or key == '.':
            self.state.handle(key)
        elif key == '=' or key == 'C' or key == 'CE' or key == '<-':
            self.state = State3(self)
            self.state.handle(key)
        elif key == 'sin' or key == 'cos' or key == 'tan' or key == 'bin' or key == 'oct' or key == 'hex' or key == 'fac' or key == 'fib':
            self.state = State4(self)
            self.state.handle(key)
        else:
            self.state = State2(self)
            self.state.handle(key)

    def logic(self, key):
        left_operant = float(self.left_operant)
        right_operant = float(self.right_operant)
        if self.operator == '+':
            self.result = left_operant + right_operant
            if self.result.is_integer():
                self.result = str(int(self.result))
            self.result = str(self.result)
            self.line_edit.label.insert(key)
            self.line_edit.l_edit.setText(self.result)
            self.switch = False
            self.state = State1(self)
        elif self.operator == '-':
            self.result = left_operant - right_operant
            if self.result.is_integer():
                self.result = str(int(self.result))
            self.result = str(self.result)
            self.line_edit.label.insert(key)
            self.line_edit.l_edit.setText(self.result)
            self.switch = False
            self.state = State1(self)
        elif self.operator == '*':
            self.result = left_operant * right_operant
            if self.result.is_integer():
                self.result = str(int(self.result))
            self.result = str(self.result)
            self.line_edit.label.insert(key)
            self.line_edit.l_edit.setText(self.result)
            self.switch = False
            self.state = State1(self)
        elif self.operator == '/':
            self.result = left_operant / right_operant
            if self.result.is_integer():
                self.result = str(int(self.result))
            self.result = str(self.result)
            self.line_edit.label.insert(key)
            self.line_edit.l_edit.setText(self.result)
            self.switch = False
            self.state = State1(self)
        elif self.operator == '**':
            self.result = left_operant ** right_operant
            if self.result.is_integer():
                self.result = str(int(self.result))
            self.result = str(self.result)
            self.line_edit.label.insert(key)
            self.line_edit.l_edit.setText(self.result)
            self.switch = False
            self.state = State1(self)


class State1:
    def __init__(self, calc):
        self.calc = calc

    def change_state(self, key):
        self.calc.state = State2(self.calc)
        self.calc.handle(key)

    def change_edit(self, key):
        text = self.calc.line_edit.l_edit.text()
        if text == '0':
            self.calc.line_edit.l_edit.setText(key)
        elif text == '+' or text == '-' or text == '/' or text == '*' or text == '**':
            self.calc.operator = self.calc.line_edit.l_edit.text()
            self.calc.line_edit.label.insert(self.calc.operator)
            self.calc.line_edit.l_edit.setText(key)
        elif self.calc.result == text:
            self.calc.left_operant = 0
            self.calc.right_operant = 0
            self.calc.operator = 0
            self.calc.result = 0
            self.calc.line_edit.l_edit.clear()
            self.calc.line_edit.label.clear()

            self.calc.line_edit.l_edit.setText(key)
        else:
            self.calc.line_edit.l_edit.insert(key)
        self.calc.switchOper = True
        self.calc.switchSt4 = True

    def handle(self, key):
        if key.isdigit() or key == '.':
            self.change_edit(key)
        else:
            self.change_state(key)


class State2:
    def __init__(self, calc):
        self.calc = calc
        self.nam = ['**', '+', '-', '*', '/']

    def change_state(self):
        self.calc.state = State1(self.calc)

    def change_edit(self, key):
        text = self.calc.line_edit.l_edit.text()
        if self.calc.switchOper:
            if text == '+' or text == '-' or text == '/' or text == '*' or text == '**' or text == '':
                pass
            else:
                self.calc.left_operant = self.calc.line_edit.l_edit.text()
                self.calc.line_edit.label.insert(self.calc.left_operant)
                self.calc.line_edit.l_edit.setText(key)
                self.calc.switch = True

        self.change_state()

    def handle(self, key):
        self.change_edit(key)


class State3:
    def __init__(self, calc):
        self.calc = calc

    def change_state(self):
        self.calc.state = State1(self.calc)

    def change_edit(self, key):
        if self.calc.switch:
            if self.calc.line_edit.l_edit.text() == '=':
                self.change_state()
                pass
            elif self.calc.line_edit.l_edit.text() == '0':
                self.change_state()
                pass
            elif self.calc.line_edit.l_edit.text() == '':
                self.change_state()
                pass
            elif self.calc.operator == 0:
                self.change_state()
                pass
            else:
                self.calc.right_operant = self.calc.line_edit.l_edit.text()
                self.calc.line_edit.label.insert(self.calc.right_operant)
                self.calc.line_edit.l_edit.setText(key)
                self.calc.logic(key)

    def handle(self, key):
        if key == '=':
            self.change_edit(key)
        elif key == 'C' or key == 'CE' or key == '<-':
            if key == 'CE':
                self.calc.line_edit.l_edit.clear()
                self.calc.line_edit.l_edit.setText('0')
            elif key == '<-':
                if self.calc.switch:
                    self.calc.line_edit.l_edit.backspace()
                    if self.calc.line_edit.l_edit.text() == '':
                        self.calc.line_edit.l_edit.setText('0')
            else:
                self.calc.line_edit.l_edit.clear()
                self.calc.line_edit.label.clear()
                self.calc.line_edit.l_edit.setText('0')
        self.change_state()


class State4:
    def __init__(self, calc):
        self.calc = calc

    def change_state(self):
        self.calc.state = State1(self.calc)

    def change_edit(self, key):
        if key == 'bin' and self.calc.switchSt4:
            text = int(float(self.calc.line_edit.l_edit.text()))
            self.calc.result = bin(text)
            self.calc.switchOper = False
            self.calc.switchSt4 = False
            self.calc.switch = False
            self.calc.line_edit.l_edit.setText(str(self.calc.result))
        elif key == 'hex' and self.calc.switchSt4:
            text = int(float(self.calc.line_edit.l_edit.text()))
            self.calc.result = hex(text)
            self.calc.switchOper = False
            self.calc.switchSt4 = False
            self.calc.switch = False
            self.calc.line_edit.l_edit.setText(str(self.calc.result))
        elif key == 'oct' and self.calc.switchSt4:
            text = int(float(self.calc.line_edit.l_edit.text()))
            self.calc.result = oct(text)
            self.calc.switchOper = False
            self.calc.switchSt4 = False
            self.calc.switch = False
            self.calc.line_edit.l_edit.setText(str(self.calc.result))
        elif key == 'fib' and self.calc.switchSt4:
            text = int(float(self.calc.line_edit.l_edit.text()))
            def fib(n):
                a = 0
                b = 1
                for __ in range(n):
                    a, b = b, a + b
                return a
            self.calc.result = fib(text)
            self.calc.switchOper = False
            self.calc.switchSt4 = False
            self.calc.switch = False
            self.calc.line_edit.l_edit.setText(str(self.calc.result))

        elif key == 'cos' and self.calc.switchSt4:
            text = int(float(self.calc.line_edit.l_edit.text()))
            self.calc.result = math.cos(text)
            self.calc.switchOper = False
            self.calc.switchSt4 = False
            self.calc.switch = False
            self.calc.line_edit.l_edit.setText(str(self.calc.result))
        elif key == 'sin' and self.calc.switchSt4:
            text = int(float(self.calc.line_edit.l_edit.text()))
            self.calc.result = math.sin(text)
            self.calc.switchOper = False
            self.calc.switchSt4 = False
            self.calc.switch = False
            self.calc.line_edit.l_edit.setText(str(self.calc.result))
        elif key == 'tan' and self.calc.switchSt4:
            text = int(float(self.calc.line_edit.l_edit.text()))
            self.calc.result = math.tan(text)
            self.calc.switchOper = False
            self.calc.switchSt4 = False
            self.calc.switch = False
            self.calc.line_edit.l_edit.setText(str(self.calc.result))
        elif key == 'fac' and self.calc.switchSt4:
            text = int(float(self.calc.line_edit.l_edit.text()))
            self.calc.result = math.factorial(text)
            self.calc.switchOper = False
            self.calc.switchSt4 = False
            self.calc.switch = False
            self.calc.line_edit.l_edit.setText(str(self.calc.result))

    def handle(self, key):

        self.change_edit(key)


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

