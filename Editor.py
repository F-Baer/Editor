from PyQt5.QtWidgets import QApplication, QMainWindow
from formular import Ui_MeinFormular

class Hauptfenster(QMainWindow, Ui_MeinFormular):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_Beenden.triggered.connect(self.action_close)
    
        self.show()

    def action_close(self):
        self.close()
    
app = QApplication([])
fenster = Hauptfenster()

app.exec()

