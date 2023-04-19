import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedLayout, QVBoxLayout, QHBoxLayout, QWidget

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(400,200))
        #caja = QHBoxLayout()
        #caja = QVBoxLayout()
        caja = QStackedLayout()
        
        ####boton = QPushButton("Presioname", lambda clicked: print("Acción con Lambda Expressions"))
        boton1 = QPushButton("Boton1")
        boton2 = QPushButton("Boton2")
        boton3 = QPushButton("Boton3")
        boton4 = QPushButton("Boton4")
        #boton.clicked.connect(self.reaccionar)
        
        # Se agregan los componentes al layout definido
        caja.addWidget(boton1) # index 0
        caja.addWidget(boton2) # index 1
        caja.addWidget(boton3) # index 2
        caja.addWidget(boton4) # index 3
        
        caja.setCurrentIndex(2)
        
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