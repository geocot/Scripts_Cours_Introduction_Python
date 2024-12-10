from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit,QTableView, QDateEdit, QHeaderView,QMessageBox, QAction, QFileDialog, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt5 import uic
import sys,csv

import Employe

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        #Chargement de la forme
        uic.loadUi('formeMain.ui', self)
        #Chargement des widgets
        self.table = self.findChild(QTableView, 'tableView')
        self.btnSupprime = self.findChild(QPushButton, "btnSupprime")
        self.btnAjout = self.findChild(QPushButton, "btnAjout")
        self.btnRechercher = self.findChild(QPushButton, "btnRechercher")
        self.btnDeselectionner = self.findChild(QPushButton, "btnDeselectionner")
        self.btnQuitter = self.findChild(QPushButton, "btnQuit")
        self.leNom = self.findChild(QLineEdit, "leNom")
        self.lePrenom = self.findChild(QLineEdit, "lePrenom")
        self.leID = self.findChild(QLineEdit, "leID")
        self.leRechercheID = self.findChild(QLineEdit, "leRechercheID")
        self.dateEdit = self.findChild(QDateEdit, "dateEdit")
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #Étendre les colonnes
        self.aquitter = self.findChild(QAction, "actionQuitter")
        self.achargerEmployes = self.findChild(QAction, "actionCharger_des_donn_es")
        self.asauvegardeEmployes = self.findChild(QAction, "actionSauvegarder_des_donn_es")
        self.listeObjEmployes = [] #Liste d'objet employé
        self.tableau=[]
        #Events
        self.btnQuitter.clicked.connect(self.quitter)
        self.btnAjout.clicked.connect(self.ajout)
        self.btnSupprime.clicked.connect(self.supprime)
        self.btnRechercher.clicked.connect(self.rechercher)
        self.btnDeselectionner.clicked.connect(self.deselectionner)
        self.aquitter.triggered.connect(self.quitter) #Menu quitter
        self.achargerEmployes.triggered.connect(self.chargerEmployes)
        self.asauvegardeEmployes.triggered.connect(self.sauvegardeEmployes)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows) #Permet de sélectionner des lignes au lieu de cellules
        self.show()

    def deselectionner(self):
        self.table.setCurrentIndex(QModelIndex())

    def chargerEmployes(self):
        fileName = QFileDialog.getOpenFileName(self, "Base de données", "c:/temp/gestionEmploye", "Fichier texte (*.csv *.txt)")
        print(fileName)
        if fileName:
            with open(fileName[0], newline='') as csvfile:
                listeLigne = csv.reader(csvfile, delimiter=',')
                for row in listeLigne:
                        self.listeObjEmployes.append(Employe.Employe(row[0], row[1], row[2], row[3]))
            self.chargementTableau()

    def sauvegardeEmployes(self):
        if len(self.listeObjEmployes) != 0:
            fileName = QFileDialog.getSaveFileName(self, "Base de données", "c:/temp/gestionEmploye", "Fichier texte (*.csv *.txt)")
            if fileName[0]:
                with open(fileName[0], "w", newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    for e in self.listeObjEmployes:
                        writer.writerow(e.versListe())
        else:
            self.afficheMessage("La table est vide")

    # À partir de la liste d'employé
    # Appelé après le changement de données
    def chargementTableau(self):
        self.tableau.clear()
        for e in self.listeObjEmployes:
            self.tableau.append(e.versListe())
        self.model = TableModel(self.tableau)
        self.table.setModel(self.model)
        self.model.layoutChanged.emit()  # Pour indiquer qu'il y a un changement dans la source des données.
    def supprime(self):
        if len(self.listeObjEmployes) != 0: #Si la table est vide
            indexes = self.table.selectionModel().selectedRows()
            if len(indexes) ==0:
                self.afficheMessage("Aucune sélection")
            else:
                for index in indexes:
                    self.effaceEmployeTableau(index.child(index.row(), 2).data())
            self.chargementTableau()
        else:
            self.afficheMessage("Table vide")


    def effaceEmployeTableau(self, id):
        for e in self.listeObjEmployes:
            if e.id == id:
                self.listeObjEmployes.remove(e)
    def rechercher(self):
        trouve = False
        if self.leRechercheID.text() == "":
            self.afficheMessage("Aucune information à rechercher")
        else:
            for e in self.listeObjEmployes:
                if e.id == self.leRechercheID.text():
                    trouve = True
                    self.table.selectRow(self.listeObjEmployes.index(e))
            if not trouve:
                self.afficheMessage("Rien trouvé")


    def ajout(self):
        prenom = self.lePrenom.text()
        nom = self.leNom.text()
        id = self.leID.text()
        date = self.dateEdit.text()
        if self.verifAjout(prenom, nom, id, date):
            self.listeObjEmployes.append(Employe.Employe(nom, prenom, id, date))
            self.chargementTableau()
        else:
            self.afficheMessage("Les champs sont incomplets pour l'ajout")

    def afficheMessage(self, msg):
        QMessageBox.warning(self, "Oups!", msg)

    def verifAjout(self, prenom, nom, id, date):
        estOK = False
        if prenom!="":
            if nom!="":
                if id !="":
                    estOK=True
        return estOK

    def quitter(self):
            app.quit()


class TableModel(QAbstractTableModel):
    def __init__(self, donnees):
        #super(TableModel, self).__init__()
        super().__init__()
        self._donnees = donnees

    # Implémentation
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            try:
                return self._donnees[index.row()][index.column()]
            except:
                print("problème")
    #Implémentation
    def rowCount(self, parent=QModelIndex()):
            # The length of the outer list.
            return len(self._donnees)
    #Implémentation
    def columnCount(self, parent=QModelIndex()):
            # The following takes the first sub-list, and returns
            # the length (only works if all rows are an equal length)
            return len(self._donnees[0])

    #Implémentation
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Nom", "Prénom", "ID", "Date")[section]



app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()