import sys
from PyQt5.QtWidgets import QDialog, QApplication
from fen import Ui_MonApp

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MonApp()
        self.ui.setupUi(self)
        self.show()  
    def btnEcrire(self):
        print("Allo")
        txt = w.ui.plainTextEdit.toPlainText()
        txt = txt + "Allo\n"
        w.ui.plainTextEdit.setPlainText(txt)
    def Qtn(self):
        sys.exit(0)

app = QApplication(sys.argv)
w = AppWindow()
w.ui.btnEcrire.clicked.connect(AppWindow.btnEcrire)
w.ui.btnQuit.clicked.connect(AppWindow.Qtn)

sys.exit(app.exec_())