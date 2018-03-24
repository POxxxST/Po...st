#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Calendar(QWidget):

    def __init__(self):
        super().__init__()

        self.cal = QCalendarWidget()
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel()
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lbl)
        self.vbox.addWidget(self.cal)

        self.setLayout(self.vbox)

    def showDate(self, date):

        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Calendar()
    ex.setGeometry(300, 300, 350, 300)
    ex.setWindowTitle('Calendar')
    ex.show()
    sys.exit(app.exec_())