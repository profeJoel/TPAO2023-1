import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(400,200))
        
        ####boton = QPushButton("Presioname", lambda clicked: print("Acción con Lambda Expressions"))
        boton = QPushButton("Presioname")
        boton.clicked.connect(self.reaccionar)
        
        self.setCentralWidget(boton)
        
    #Primera forma de manejar eventos
    def reaccionar(self):
        self.contador_clicks += 1
        print(f"Botón Presionado!!!! Contador de Clicks en {self.contador_clicks} clicks")
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()