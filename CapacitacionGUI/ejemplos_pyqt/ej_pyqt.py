import sys
from PyQt6.QtWidgets import QWidget, QApplication

class Ventana(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        
    def inicializarUI(self):
        self.setGeometry(100,100, 500, 500)
        self.setWindowTitle("Hola Mundo")
        self.show() # linea obligatoria
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    programa1 = Ventana()
    sys.exit(app.exec())