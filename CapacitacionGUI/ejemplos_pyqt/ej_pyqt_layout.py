import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(400,200))
        #caja = QHBoxLayout()
        caja = QVBoxLayout()
        
        ####boton = QPushButton("Presioname", lambda clicked: print("Acción con Lambda Expressions"))
        boton1 = QPushButton("Boton1")
        boton2 = QPushButton("Boton2")
        #boton.clicked.connect(self.reaccionar)
        
        # Se agregan los componentes al layout definido
        caja.addWidget(boton1)
        caja.addWidget(boton2)
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
        
        
        
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