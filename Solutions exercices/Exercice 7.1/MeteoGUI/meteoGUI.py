# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meteoGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import objMeteo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.objM = objMeteo.Meteo('https://meteo.gc.ca/rss/city/qc-133_f.xml')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 150)
        MainWindow.setMinimumSize(QtCore.QSize(400, 150))
        MainWindow.setMaximumSize(QtCore.QSize(400, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 331, 31))
        self.label.setObjectName("label")
        self.btnMAJour = QtWidgets.QPushButton(self.centralwidget)
        self.btnMAJour.setGeometry(QtCore.QRect(160, 70, 75, 23))
        self.btnMAJour.setObjectName("btnMAJour")
        self.btnMAJour.clicked.connect(self._afficheMeteo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Météo"))
        self.label.setText(_translate("MainWindow", ""))
        self.btnMAJour.setText(_translate("MainWindow", "Lire Météo"))

    def _afficheMeteo(self):
        self.label.setText(self.objM.getMeteo())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
