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
            self.vbox.addLayout(self.vboxBot)
            self.btnMax.btn_clicked.connect(self.fun)
            try:
                self.vbox.replaceWidget(self.btnPro, self.btnMax)
                self.vbox.replaceWidget(self.btnGeo, self.btnMax)
            except:
                pass
        elif text == 'Программист':
            self.btnPro = MyButton.ExampleProg()
            self.vboxBot.addWidget(self.btnPro)
            self.vbox.addLayout(self.vboxBot)
            self.btnPro.btn_clicked.connect(self.fun)
            try:
                self.vbox.replaceWidget(self.btnMax, self.btnPro)
                self.vbox.replaceWidget(self.btnGeo, self.btnPro)
            except:
                pass

        elif text == 'Геометрия':
            self.btnGeo = MyButton.ExampleGeomet()
            self.vboxBot.addWidget(self.btnMax)
            self.vbox.addLayout(self.vboxBot)
            self.btnGeo.btn_clicked.connect(self.fun)
            try:
                self.vbox.replaceWidget(self.btnMax, self.btnGeo)
                self.vbox.replaceWidget(self.btnPro, self.btnGeo)
            except:
                pass


class Calculator:
    def __init__(self, line_edit):
        self.nam = ['+', '-', '*', '/', '**']

        self.left_operant = 0
        self.operator = 0
        self.right_operant = 0

        self.line_edit = line_edit
        self.state = State1(self)


    def handle(self, key):
        if key.isdigit() or key == '.':
            self.state = State1(self)
            self.state.handle(key)
        elif key == '=':
            if self.line_edit.getL_edit() == '0':
                pass
            else:
                self.state = State3(self)
                self.state.handle(key)
        elif key == 'C' or key == 'CE' or key == '<-':
            if key == 'CE' or key == 'C':
                self.line_edit.namC(key)
            elif key == '<-':
                self.line_edit.back()
        else:
            if self.line_edit.getL_edit() == '+' or self.line_edit.getL_edit() == '-' or self.line_edit.getL_edit() == '/' or self.line_edit.getL_edit() == '*' or self.line_edit.getL_edit()  == '**':
                pass
            else:
                for i in self.nam:
                    if key == i:
                        self.state = State2(self)
                        self.state.handle(key)

    def logik(self, key):
        left_oper = float(self.left_operant)
        right_oper = float(self.right_operant)
        if self.operator == '+':
            result = left_oper + right_oper
            if result.is_integer():
                result = int(result)
            self.line_edit.setLabel(key)
            self.line_edit.setL_edit(str(result))
        elif self.operator == '-':
            result = left_oper - right_oper
            if result.is_integer():
                result = int(result)
            self.line_edit.setLabel(key)
            self.line_edit.setL_edit(str(result))
        elif self.operator == '/':
            result = left_oper / right_oper
            if result.is_integer():
                result = int(result)
            self.line_edit.setLabel(key)
            self.line_edit.setL_edit(str(result))
        elif self.operator == '*':
            result = left_oper * right_oper
            if result.is_integer():
                result = int(result)
            self.line_edit.setLabel(key)
            self.line_edit.setL_edit(str(result))
        elif self.operator == '**':
            result = left_oper ** right_oper
            if result.is_integer():
                result = int(result)
            self.line_edit.setLabel(key)
            self.line_edit.setL_edit(str(result))


class State1:
    def __init__(self, calc):
        self.calc = calc

    def change_state(self):
        pass

    def change_edit(self):
        pass

    def handle(self, key):
        self.calc.line_edit.setL_edit(key)


class State2:
    def __init__(self, calc):
        self.calc = calc

    def change_state(self, key):
        pass

    def change_edit(self, key):
        pass

    def handle(self, key):
        self.calc.left_operant = self.calc.line_edit.getL_edit()
        self.calc.line_edit.setLabel(self.calc.left_operant)
        self.calc.line_edit.setL_edit(key)
        self.calc.operator = key
        self.calc.line_edit.setLabel(key)


class State3:
    def __init__(self, calc):
        self.calc = calc

    def change_state(self, key):
        pass

    def change_edit(self, key):
        pass

    def handle(self, key):
        self.calc.right_operant = self.calc.line_edit.getL_edit()
        self.calc.line_edit.setLabel(self.calc.right_operant)
        self.calc.line_edit.setL_edit(key)
        self.calc.logik(key)




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
