from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QDir

from formular import Ui_MeinFormular

class Hauptfenster(QMainWindow, Ui_MeinFormular):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_Beenden.triggered.connect(self.action_close)
        self.action_Neu.triggered.connect(self.action_neu)
        self.action_Speichern.triggered.connect(self.action_save)
        self.action_Oeffnen.triggered.connect(self.action_open)
        
        self.show()

    def action_close(self):
        self.close()
    
    def action_neu(self):
        meine_abfrage = QMessageBox.question(self,
                         "Abfrage",                    
                         "Wollen sie wirklich eine neue Datei anlegen?")
        if meine_abfrage == QMessageBox.Yes:
            self.textEdit.clear()

    def action_save(self):
        dateiname = QFileDialog.getSaveFileName(self,
                    "Datei speichern",
                    QDir.currentPath(),
                    "Textdateien (*.txt)")
        if dateiname[0] != "":
            with open(dateiname[0], "w") as datei:
                datei.writelines(self.textEdit.toPlainText())
            self.statusBar.showMessage("Die Datei wurde gespeichert.", 5000)

    def action_open(self):
        dateiname = QFileDialog.getOpenFileName(self,
                    "Datei laden",
                    QDir.currentPath(),
                    "Textdateien (*.txt)")
        if dateiname[0] != "":
            with open(dateiname[0], "r") as datei:
                text = ""
                for zeile in datei:
                    text = text + zeile
                    self.textEdit.setPlainText(text)

            self.statusBar.showMessage("Die Datei wurde geladen.", 5000)

    
app = QApplication([])
fenster = Hauptfenster()

app.exec()

