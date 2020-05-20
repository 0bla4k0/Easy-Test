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

def introduction():
    '''
    Hello there! To create formulas for tests
    you have to go 205 line. Please keep track of
    data types. Then you will already ready to put answer
    in box, you have to change data type to STR.
    For example:
    ui.textEdit.setText(str(int(a+b)) + " this answer " + " :^) ")
    '''



class control_the_programm():
    '''
    To avoid errors, don't change
    the structure of the programme.
    '''

    def message_box(self):
        '''
        This function creates a message box
        which tells you about documentation
        to this program and how to use it.
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Справка")
        msg.setWindowIcon(QtGui.QIcon("ico/help.ico"))
        msg.setText("Чтобы перейти к нужному заданию, нужно нажать на номер задания в верхней шапке. \n"
                    "После введите числа в правых столбиках и нажмите кнопку 'Получить ответ'. \n"
                    "\nЕсли все понятно, нажмите 'OK'.\n"
                    "\nЕсли вы хотите делать свои тесты в этой программе, нажмите 'Show Details'.")
        msg.setInformativeText("© 0bla4k0, 2020")
        msg.setDetailedText("Скопируйте и после перейдите по ссылке, чтобы ознакомиться"
                            " с работой программы и ее документацией: https://vk.com/oblachko6")
        x = msg.exec()

    def name_of_programm(self):
        '''
        This function creates a name for
        the program that is at the top.
        It reads the name from the TXT file,
        which created in folder called "txt".
        '''
        name = open("txt/test_name.txt", 'r', encoding='utf-8')
        name_line = name.readline()
        ui.textEdit_2.setText(name_line)

    def clear_lines(self):
        '''
        This function clears all boxes
        from previous task.
        '''
        ui.lineEdit_2.clear()
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
        '''
        This function helps the next function
        creates number of variables based on the
        number of conditions.
        Also, it pastes conditions from txt file
        in boxes.
        '''
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
        '''
        If something go wrong, programme will
        tell you about it.
        '''
        ui.textEdit.setText("\n                                             Введите цифры!")
        pass

    def take_numbers_from_boxes(self):
        '''
        This function creates number of
        variables to create formulas in the future.
        For example, if you 5 conditions in the test,
        the programme will create 5 variables.
        '''
        global a, b, c, d, e
        if test_lines == 5:
            try:
                a = ui.lineEdit_2.text()
                b = ui.lineEdit.text()
                c = ui.lineEdit_3.text()
                d = ui.lineEdit_4.text()
                e = ui.lineEdit_5.text()
                if (len(a)) or (len(a) * len(b) * len(c) * len(d) * len(e)) == 0:
                    easy_test.warning()
                a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)
            except ValueError:
                easy_test.warning()

        if test_lines == 4:
            try:
                a = ui.lineEdit_2.text()
                b = ui.lineEdit.text()
                c = ui.lineEdit_3.text()
                d = ui.lineEdit_4.text()
                if len(a) * len(b) * len(c) * len(d) == 0:
                    easy_test.warning()
                a, b, c, d = int(a), int(b), int(c), int(d)
            except ValueError:
                easy_test.warning()

        if test_lines == 3:
            try:
                a = ui.lineEdit_2.text()
                b = ui.lineEdit.text()
                c = ui.lineEdit_3.text()
                if len(a) * len(b) * len(c) == 0:
                    easy_test.warning()
                a, b, c = int(a), int(b), int(c)
            except ValueError:
                easy_test.warning()

        if test_lines == 2:
            try:
                a = ui.lineEdit_2.text()
                b = ui.lineEdit.text()
                if len(a) * len(b) == 0:
                    easy_test.warning()
                a, b = int(a), int(b)
            except ValueError:
                easy_test.warning()

        if test_lines == 1:
            try:
                a = ui.lineEdit_2.text()
                if len(a) == 0:
                    easy_test.warning()
                a = int(a)
            except ValueError:
                easy_test.warning()

    def txt_tasks(self, y):
        '''
        This functions takes number of the task from button,
        then this number go here, open certain txt file, puts
        conditions in the list from each line. After that,
        variable x counts how many conditions, then this x
        goes in "def create_conditions".
        '''
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
            formula = None
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
            formula =  None
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
            formula = None
            ui.textEdit.setText(str(formula))
        except  ValueError:
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
            formula = None
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
            formula = None
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
