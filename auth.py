# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formauth(object):
    def setupUi(self, Formauth):
        Formauth.setObjectName("Formauth")
        Formauth.resize(402, 184)
        Formauth.setMinimumSize(QtCore.QSize(402, 184))
        Formauth.setMaximumSize(QtCore.QSize(402, 184))
        self.centralwidget = QtWidgets.QWidget(Formauth)
        self.centralwidget.setObjectName("centralwidget")
        self.Login = QtWidgets.QLineEdit(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.Login.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Login.setObjectName("Login")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(10, 60, 381, 31))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.signin = QtWidgets.QPushButton(self.centralwidget)
        self.signin.setGeometry(QtCore.QRect(10, 110, 151, 51))
        self.signin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signin.setObjectName("signin")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(240, 140, 151, 21))
        self.create.setObjectName("create")
        Formauth.setCentralWidget(self.centralwidget)

        self.retranslateUi(Formauth)
        QtCore.QMetaObject.connectSlotsByName(Formauth)

    def retranslateUi(self, Formauth):
        _translate = QtCore.QCoreApplication.translate
        Formauth.setWindowTitle(_translate("Formauth", "MainWindow"))
        self.Login.setPlaceholderText(_translate("Formauth", "Логин:"))
        self.password.setPlaceholderText(_translate("Formauth", "Пароль:"))
        self.signin.setText(_translate("Formauth", "Войти"))
        self.create.setText(_translate("Formauth", "Добавить учётную запись"))
