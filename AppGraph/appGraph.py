from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QDoubleSpinBox
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        #Chargement de la forme
        uic.loadUi('forme.ui', self)

        #Chargement des widgets
        self.listeUnites = self.findChild(QComboBox,'cmBoxUnites')
        self.quitter = self.findChild(QPushButton,'btnQuit')
        self.resultat = self.findChild(QLabel,'lblResultat')
        self.convertir = self.findChild(QPushButton,'btnConvertir')
        self.valeur = self.findChild(QDoubleSpinBox,'dSpinBoxValeur')
        #Chargement des éléments du comboBox
        self.listeUnites.addItem("Celsius -> Fahrenheit")
        self.listeUnites.addItem("Fahrenheit -> Celsius")
        #Events
        self.quitter.clicked.connect(self.fnClose)
        self.convertir.clicked.connect(self.fnConvertir)

        #Affiche fenêtre
        self.show()
    def fnConvertir(self):
        valeur = self.valeur.value()
        if self.listeUnites.currentText() == 'Celsius -> Fahrenheit':
            self.resultat.setText(str(valeur*1.8+32))
        else:
            self.resultat.setText(str((valeur-32)*(5/9)))
    def fnClose(self):
        app.quit()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()