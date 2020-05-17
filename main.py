# modals
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from gui import Ui_Dialog
import sys

# application
app = QtWidgets.QApplication(sys.argv)

#
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

class control_the_programm():

    def message_box(self):
        msg = QMessageBox()
        msg.setWindowTitle("Справка")
        msg.setWindowIcon(QtGui.QIcon("ico/help (2).ico"))
        msg.setText("Чтобы перейти к нужному заданию, нужно нажать на номер задания в верхней шапке. \n"
                    "После введите числа в правых столбиках и нажмите кнопку 'Получить ответ'. \n"
                    "\nЕсли все понятно, нажмите 'OK'.\n"
                    "\nЕсли вы хотите делать свои тесты в этой программе, нажмите 'Show Details'.")
        msg.setInformativeText("© 0bla4k0, 2020")
        msg.setDetailedText("Скопируйте и после перейдите по ссылке, чтобы ознакомиться"
                            " с работой программы и ее документацией: https://vk.com/oblachko6")
        x = msg.exec()

    def name_of_programm(self):
        name = open("txt/test_name.txt", 'r', encoding='utf-8')
        name_line = name.readline()
        ui.textEdit_2.setText(name_line)

        test_lines = 0

    def clear_lines(self):
        ui.lineEdit_2.clear()  # cleaning lines for the next task
        ui.lineEdit.clear()
        ui.textEdit.clear()
        ui.lineEdit_3.clear()
        ui.lineEdit_4.clear()
        ui.lineEdit_5.clear()
        ui.textEdit_4.clear()
        ui.textEdit_5.clear()
        ui.textEdit_6.clear()
        ui.textEdit_7.clear()
        ui.textEdit_8.clear()

    def creat_conditions(self, x, task1_array):
        if x == 5:
            ui.textEdit_4.setText(task1_array[0])
            ui.textEdit_5.setText(task1_array[1])
            ui.textEdit_6.setText(task1_array[2])
            ui.textEdit_7.setText(task1_array[3])
            ui.textEdit_8.setText(task1_array[4])
        elif x == 4:
            ui.textEdit_4.setText(task1_array[0])
            ui.textEdit_5.setText(task1_array[1])
            ui.textEdit_6.setText(task1_array[2])
            ui.textEdit_7.setText(task1_array[3])
        elif x == 3:
            ui.textEdit_4.setText(task1_array[0])
            ui.textEdit_5.setText(task1_array[1])
            ui.textEdit_6.setText(task1_array[2])
        elif x == 2:
            ui.textEdit_4.setText(task1_array[0])
            ui.textEdit_5.setText(task1_array[1])
        elif x == 1:
            ui.textEdit_4.setText(task1_array[0])
        global test_lines
        test_lines = len(task1_array)

    def warning(self):
        ui.textEdit.setText("\n                                             Введите цифры!")
        pass

    def take_numbers_from_boxes(self):
        global a, b, c, d, e
        if test_lines == 5:
            try:
                a = ui.lineEdit_2.text()
                b = ui.lineEdit.text()
                c = ui.lineEdit_3.text()
                d = ui.lineEdit_4.text()
                e = ui.lineEdit_5.text()
                a1 = len(a)
                b1 = len(b)
                c1 = len(c)
                d1 = len(d)
                e1 = len(e)
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                if a1 * b1 * c1 * d1 * e1 == 0 or a * b * c * d * e == 0:
                    easy_test.warning()
            except ValueError:
                easy_test.warning()

        if test_lines == 4:
            try:
                a = ui.lineEdit_2.text()
                b = ui.lineEdit.text()
                c = ui.lineEdit_3.text()
                d = ui.lineEdit_4.text()
                a1 = len(a)
                b1 = len(b)
                c1 = len(c)
                d1 = len(d)
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                if a1 * b1 * c1 * d1 == 0 or a * b * c * d == 0:
                    easy_test.warning()
            except ValueError:
                easy_test.warning()

        if test_lines == 3:
            try:
                a = ui.lineEdit_2.text()
                b = ui.lineEdit.text()
                c = ui.lineEdit_3.text()
                a1 = len(a)
                b1 = len(b)
                c1 = len(c)
                a = int(a)
                b = int(b)
                c = int(c)
                if a1 * b1 * c1 == 0 or a * b * c == 0:
                    easy_test.warning()
            except ValueError:
                easy_test.warning()

        if test_lines == 2:
            try:
                a = ui.lineEdit_2.text()
                b = ui.lineEdit.text()
                a1 = len(a)
                b1 = len(b)
                a = int(a)
                b = int(b)
                if a1 * b1 == 0 or a * b == 0:
                    easy_test.warning()
            except ValueError:
                easy_test.warning()

        if test_lines == 1:
            try:
                a = ui.lineEdit_2.text()
                a1 = len(a)
                a = int(a)
                if a1 == 0 or a == 0:
                    easy_test.warning()
            except ValueError:
                easy_test.warning()

    def txt_tasks(self, y):
        easy_test.clear_lines()
        task1_array = []
        z = "txt/task" + str(y) + ".txt"
        with open(z, 'r', encoding='utf-8') as task1:
            for task1_line in task1:
                task1_array.append(task1_line)
        x = len(task1_array)
        easy_test.creat_conditions(x, task1_array)

easy_test = control_the_programm()

easy_test.message_box()
easy_test.name_of_programm()

# THE_FIRST_TASK
def bp1():
    easy_test.txt_tasks(1)

    def bp():
        easy_test.take_numbers_from_boxes()
        try:
            formula = 0
            ui.textEdit.setText(str(formula))
        except ValueError:
            easy_test.warning()
        except TypeError:
            easy_test.warning()

    ui.pushButton.clicked.connect(bp)


# THE_SECOND_TASK
def bp2():
    easy_test.txt_tasks(2)

    def bp():
        easy_test.take_numbers_from_boxes()
        try:
            formula = 0                            #
            ui.textEdit.setText(str(formula))
        except ValueError:
            easy_test.warning()
        except TypeError:
            easy_test.warning()

    ui.pushButton.clicked.connect(bp)


# THE_THIRD_TASK
def bp3():
    easy_test.txt_tasks(3)

    def bp():
        easy_test.take_numbers_from_boxes()
        try:
            formula = 0                            #
            ui.textEdit.setText(str(formula))
        except ValueError:
            easy_test.warning()
        except TypeError:
            easy_test.warning()

    ui.pushButton.clicked.connect(bp)


# THE_FOURTH_TASK
def bp4():
    easy_test.txt_tasks(4)

    def bp():
        easy_test.take_numbers_from_boxes()
        try:
            formula = 0                           #
            ui.textEdit.setText(str(formula))
        except ValueError:
            easy_test.warning()
        except TypeError:
            easy_test.warning()

    ui.pushButton.clicked.connect(bp)


# THE_FIFTH_TASK
def bp5():
    easy_test.txt_tasks(5)

    def bp():
        easy_test.take_numbers_from_boxes()
        try:
            formula = 0                            #
            ui.textEdit.setText(str(formula))
        except ValueError:
            easy_test.warning()
        except TypeError:
            easy_test.warning()

    ui.pushButton.clicked.connect(bp)


# BUTTONS
ui.pushButton_3.clicked.connect(bp1)
ui.pushButton_2.clicked.connect(bp2)
ui.pushButton_4.clicked.connect(bp3)
ui.pushButton_5.clicked.connect(bp4)
ui.pushButton_6.clicked.connect(bp5)

#
sys.exit(app.exec_())
