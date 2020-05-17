from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setFixedSize(431, 552)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setStyleSheet("\n"
                             "QDialog{\n"
                             "    background-color: #2f2e36;\n"
                             "} \n"
                             "\n"
                             "QPushButton {    \n"
                             "    background-color: #3a3f48;\n"
                             "    color: white;\n"
                             "    font-size:15px;\n"
                             "    font-family: arial;\n"
                             "    font-weight: bold;\n"
                             "    border: none;\n"
                             "}\n"
                             "\n"
                             "QPushButton::hover {\n"
                             "    background-color: #383641;\n"
                             "    color: white;\n"
                             "}\n"
                             "\n"
                             "QPushButton::pressed {\n"
                             "    background-color: #484a53;\n"
                             "    color: #1fa0f2;\n"
                             "}\n"
                             "\n"
                             "\n"
                             "QTextEdit {\n"
                             "    background-color: #34323b;\n"
                             "    color: white;\n"
                             "    border: none;\n"
                             "}\n"
                             "\n"
                             "QLineEdit {\n"
                             "    background-color: #303a4c;\n"
                             "    color: white;\n"
                             "}\n"
                             "\n"
                             "")
        Dialog.setModal(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 420, 161, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(260, 170, 161, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 110, 161, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 490, 371, 51))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 411, 31))
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777167, 16777215))
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 110, 231, 41))
        self.textEdit_4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 170, 231, 41))
        self.textEdit_5.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_5.setObjectName("textEdit_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 411, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 230, 161, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_6 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 230, 231, 41))
        self.textEdit_6.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(10, 290, 231, 41))
        self.textEdit_7.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_7.setObjectName("textEdit_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 290, 161, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit_8 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_8.setGeometry(QtCore.QRect(10, 350, 231, 41))
        self.textEdit_8.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_8.setObjectName("textEdit_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 350, 161, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("", "Easy Test"))
        Dialog.setWindowIcon(QtGui.QIcon("ico/icon.ico"))
        self.pushButton.setText(_translate("Dialog", "Получить ответ"))
        self.lineEdit_2.setToolTip(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:10pt;\">Введите здесь числа.</span></p></body></html>"))
        self.lineEdit.setToolTip(_translate("Dialog",
                                            "<html><head/><body><p><span style=\" font-size:10pt;\">Введите здесь числа.</span></p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:10pt;\">Введите здесь числа.</span></p></body></html>"))
        self.lineEdit_4.setToolTip(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:10pt;\">Введите здесь числа.</span></p></body></html>"))
        self.lineEdit_5.setToolTip(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:10pt;\">Введите здесь числа.</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "Задача 1"))
        self.pushButton_2.setText(_translate("Dialog", "Задача 2"))
        self.pushButton_4.setText(_translate("Dialog", "Задача 3"))
        self.pushButton_5.setText(_translate("Dialog", "Задача 4"))
        self.pushButton_6.setText(_translate("Dialog", "Задача 5"))
