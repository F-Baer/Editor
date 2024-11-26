# Beim Öffnen einer Datei wird das alte geschriebene nicht gelöscht.
# Nachrichten evtl anzeigen lassen.

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QDir

from formular import Ui_MeinFormular

class Hauptfenster(QMainWindow, Ui_MeinFormular):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dateiname = None 

        self.action_Beenden.triggered.connect(self.action_close)
        self.action_Neu.triggered.connect(self.action_neu)
        self.action_Speichern.triggered.connect(self.action_save)
        self.action_Speichern_unter.triggered.connect(self.action_speichern_unter)
        self.action_Oeffnen.triggered.connect(self.action_open)
        self.action_Info.triggered.connect(self.action_info)
        
        self.show()

    def action_close(self):
        self.close()
    
    def action_neu(self):
        meine_abfrage = QMessageBox.question(self,
                         "Abfrage",                    
                         "Wollen sie wirklich eine neue Datei anlegen?")
        if meine_abfrage == QMessageBox.Yes:
            self.textEdit.clear()
            self.dateiname = None 

    def action_save(self):
        if not self.dateiname:
            self.action_speichern_unter()
        else:
            self.speichern(self.dateiname)

    def action_speichern_unter(self):
        dateiname, _ = QFileDialog.getSaveFileName(self,
                    "Datei speichern",
                    QDir.currentPath(),
                    "Textdateien (*.txt)")
       
        if dateiname:
            self.speichern(dateiname)
            self.dateiname = dateiname

            #self.statusBar.showMessage("Die Datei wurde gespeichert.", 5000)
    
    def speichern(self, dateiname):
        with open(dateiname, "w") as datei:
            datei.writelines(self.textEdit.toPlainText())

            #self.statusBar.showMessage("Die Datei wurde gespeichert.", 5000)

    def action_open(self):
        dateiname, _ = QFileDialog.getOpenFileName(self,
                    "Datei laden",
                    QDir.currentPath(),
                    "Textdateien (*.txt)")
        if dateiname:
            with open(dateiname, "r") as datei:
                text = ""
                for zeile in datei:
                    text = text + zeile
                    self.textEdit.setPlainText(text)
            self.dateiname = dateiname # Einsendeaufgabe 14.2

            #self.statusBar.showMessage("Die Datei wurde geladen.", 5000)

    def action_info(self):
        QMessageBox.information(self,
        "Information",
        "Mini-Editor\nProgramiert von Florian Bär 2024")

    
app = QApplication([])
fenster = Hauptfenster()

app.exec()

