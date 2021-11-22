import sys

import sqlite3
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.show)
        self.con = sqlite3.connect("coffee.sqlite")

    def show(self):
        cur = self.con.cursor()
        que = 'SELECT * FROM coffee'
        result = cur.execute(que).fetchall()

        # Заполнили размеры таблицы
        self.resultWidget.setRowCount(len(result))
        self.resultWidget.setColumnCount(len(result[0]))
        # Устанавливаем заголовки таблицы
        self.resultWidget.setHorizontalHeaderLabels(
            ["id", "название сорта", "степень обжарки", "молотый/в зернах", "описание вкуса", "Цена", "объем упаковки"])
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                flag = False
                if j == 3:
                    val2 = cur.execute('SELECT title from "ground / beans" WHERE id =' + str(int(val))).fetchall()[0][0]
                    self.resultWidget.setItem(i, j, QTableWidgetItem(str(val2)))
                    flag = True
                if not flag:
                    self.resultWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.resultWidget.resizeColumnsToContents()
        header = self.resultWidget.horizontalHeader()
        header.setStretchLastSection(False)
        header.setStretchLastSection(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
