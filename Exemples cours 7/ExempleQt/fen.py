# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MonApp(object):
    def setupUi(self, MonApp):
        MonApp.setObjectName("MonApp")
        MonApp.resize(400, 300)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(MonApp)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 20, 331, 201))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btnQuit = QtWidgets.QPushButton(MonApp)
        self.btnQuit.setGeometry(QtCore.QRect(270, 260, 99, 27))
        self.btnQuit.setObjectName("btnQuit")
        self.btnEcrire = QtWidgets.QPushButton(MonApp)
        self.btnEcrire.setGeometry(QtCore.QRect(130, 230, 99, 27))
        self.btnEcrire.setObjectName("btnEcrire")

        self.retranslateUi(MonApp)
        QtCore.QMetaObject.connectSlotsByName(MonApp)

    def retranslateUi(self, MonApp):
        _translate = QtCore.QCoreApplication.translate
        MonApp.setWindowTitle(_translate("MonApp", "Mon application"))
        self.btnQuit.setText(_translate("MonApp", "Quitter"))
        self.btnEcrire.setText(_translate("MonApp", "Écrire"))

