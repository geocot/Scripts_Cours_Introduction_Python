from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Démo")
        self.setGeometry(500,400,500,300)
        self.ajoutTableView()
        self.show()

    def ajoutTableView(self):
        self.tableWidget = QTableWidget()

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)

        self.tableWidget.setColumnWidth(0,200)

        self.tableWidget.setItem(0,0,QTableWidgetItem("Nom"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Rang"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Distance soleil"))

        self.tableWidget.setItem(1,0,QTableWidgetItem("Mercure"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("1"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("70 000 000"))

        self.tableWidget.setItem(2,0,QTableWidgetItem("Vénus"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("2"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("109 000 000"))

        self.vBoite = QVBoxLayout()
        self.vBoite.addWidget(self.tableWidget)
        self.setLayout(self.vBoite)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())