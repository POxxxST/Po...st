#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class LEdit(QWidget):

    def __init__(self):
        super().__init__()
        self.left_operand = 0
        self.operator = '0'
        self.right_operand = 0
        self.result = 0

        self.label = QLineEdit("0")
        self.l_edit = QLineEdit("0")                               # создания одностоковое поле
        self.l_edit.setReadOnly(True)                              # Поле доступно только для чтения
        self.label.setReadOnly(True)                              # Поле доступно только для чтения
        self.l_edit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # выравнивание текста в нутри поля
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # выравнивание текста в нутри поля
        self.l_edit.setFrame(False)                                # поле будет отображатся без рамки
        self.label.setFrame(False)                                # поле будет отображатся без рамки
        self.l_edit.setTextMargins(10, 10, 10, 10)                 # задаёт величину отступов между текстом и полем
        self.l_edit.setStyleSheet("background-color: #ccc;")

        fnt = self.l_edit.font()                                   # Изменения шрифта
        fnt.setPointSize(30)                                       # Размер шрифта
        fnt.setBold(True)                                          # Жирность шрифта
        self.l_edit.setFont(fnt)                                   # Устанавливаем все изменения

        self.grid = QVBoxLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.label)
        self.grid.addWidget(self.l_edit)

    def prov(self, key):
        if self.l_edit.text() == key:
            return False
        else:
            return True

    def text_label(self, text):
        text1 = self.label.text()
        text2 = self.l_edit.text()
        if text1 == '0':
            self.label.setText(text)
        else:
            if text2 == '/' or text2 == "0" or text2 == '+' or text2 == '-' or text2 == '*' or text2 == '**':
                pass
            else:
                self.label.insert(text)

    def namber(self, key):
        text = self.l_edit.text()
        if text == '/' or text == "0" or text == '+' or text == '-' or text == '*' or text == '**':
            self.l_edit.setText(key)
            self.text_label(self.operator)
        else:
            self.l_edit.insert(key)

    def operat(self, key):
        self.left_operand = self.l_edit.text()
        self.text_label(self.left_operand)
        self.l_edit.setText(key)
        self.operator = key

    def equally(self, key):
        if key == '=':
            self.right_operand = self.l_edit.text()
            self.text_label(self.right_operand)
            self.text_label(key)
            left_operand = float(self.left_operand)
            right_operand = float(self.right_operand)
            if self.operator == '+':
                result = left_operand + right_operand
                if result.is_integer():
                    result = int(result)
                self.result = str(result)
                self.l_edit.setText(self.result)
            elif self.operator == '-':
                result = left_operand - right_operand
                if result.is_integer():
                    result = int(result)
                self.result = str(result)
                self.l_edit.setText(self.result)
            elif self.operator == '*':
                result = left_operand * right_operand
                if result.is_integer():
                    result = int(result)
                self.result = str(result)
                self.l_edit.setText(self.result)
            elif self.operator == '/':
                result = left_operand / right_operand
                if result.is_integer():
                    result = int(result)
                self.result = str(result)
                self.l_edit.setText(self.result)
            elif self.operator == '**':
                result = left_operand ** right_operand
                if result.is_integer():
                    result = int(result)
                self.result = str(result)
                self.l_edit.setText(self.result)

    def back(self):
        self.l_edit.backspace()

    def namC(self, key):
        if key == 'CE':
            self.l_edit.clear()
        else:
            self.l_edit.clear()
            self.label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    calculator = LEdit()
    calculator.setWindowTitle("LEdit")
    calculator.setGeometry(300, 300, 320, 250)

    calculator.show()
    sys.exit(app.exec_())