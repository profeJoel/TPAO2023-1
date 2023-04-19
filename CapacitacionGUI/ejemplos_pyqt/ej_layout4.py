import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QStackedLayout, QVBoxLayout, QHBoxLayout, QWidget

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(400,200))
        caja_grande = QVBoxLayout()
        caja_superior = QHBoxLayout()
        self.caja_inferior = QStackedLayout()
        
        #Componentes caja superior
        boton1 = QPushButton("1")
        boton2 = QPushButton("2")
        boton3 = QPushButton("3")
        caja_superior.addWidget(boton1)
        caja_superior.addWidget(boton2)
        caja_superior.addWidget(boton3)
        
        boton1.clicked.connect(self.cambiar_a_layout_1)
        boton2.clicked.connect(self.cambiar_a_layout_2)
        boton3.clicked.connect(self.cambiar_a_layout_3)
        
        #Componentes caja inferior
        texto1 = QLabel("Texto 1")
        texto2 = QLabel("Texto 2")
        texto3 = QLabel("Texto 3")
        self.caja_inferior.addWidget(texto1)
        self.caja_inferior.addWidget(texto2)
        self.caja_inferior.addWidget(texto3)
        
        #Agregar los layout interiores al VBox
        caja_grande.addLayout(caja_superior)
        caja_grande.addLayout(self.caja_inferior)
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja_grande)
        self.setCentralWidget(ventana)
        
    def cambiar_a_layout_1(self):
        self.caja_inferior.setCurrentIndex(0)
        
    def cambiar_a_layout_2(self):
        self.caja_inferior.setCurrentIndex(1)
        
    def cambiar_a_layout_3(self):
        self.caja_inferior.setCurrentIndex(2)
        
    #Primera forma de manejar eventos
    def reaccionar(self):
        pass
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()