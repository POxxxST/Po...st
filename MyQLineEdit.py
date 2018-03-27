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

        self.label = QLineEdit("")
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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    calculator = LEdit()
    calculator.setWindowTitle("LEdit")
    calculator.setGeometry(300, 300, 320, 250)

    calculator.show()
    sys.exit(app.exec_())