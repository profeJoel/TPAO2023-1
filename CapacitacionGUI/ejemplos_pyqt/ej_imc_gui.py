import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(400,200))
        #caja = QHBoxLayout()
        caja_grande = QVBoxLayout()
        caja = QGridLayout()
        
        #Componentes de la interfaz
        bienvenida = QLabel("Bienvenida")
        masa = QLabel("Masa (kg)")
        estatura = QLabel("estatura (m)")
        self.entrada_masa = QLineEdit()
        self.entrada_estatura = QLineEdit()
        boton = QPushButton("Calcular IMC")
        self.resultado = QLabel("")
        
        boton.clicked.connect(self.calcular_imc)
        
        # Se agregan los componentes al layout definido
        caja.addWidget(masa, 0,0)
        caja.addWidget(estatura, 0,1)
        caja.addWidget(self.entrada_masa, 1,0)
        caja.addWidget(self.entrada_estatura, 1,1)
        
        
        caja_grande.addWidget(bienvenida)
        caja_grande.addLayout(caja)
        caja_grande.addWidget(boton)
        caja_grande.addWidget(self.resultado)
        #asigna el layout a la ventana

        ventana = QWidget()
        ventana.setLayout(caja_grande)
        self.setCentralWidget(ventana)
        
        
        
    #Primera forma de manejar eventos
    def calcular_imc(self):
        m = int(self.entrada_masa.text())
        e = float(self.entrada_estatura.text())
        imc = m / e**2
        self.resultado.setText(f"IMC = {imc}")
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()