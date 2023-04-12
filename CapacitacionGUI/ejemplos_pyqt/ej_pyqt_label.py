import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

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
        
        self.texto = QLabel("Texto de prueba")
        self.boton = QPushButton("Boton1")
        self.boton.clicked.connect(self.reaccionar)
        
        # Se agregan los componentes al layout definido
        caja.addWidget(self.texto)
        caja.addWidget(self.boton)
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
        
        
        
    #Primera forma de manejar eventos
    def reaccionar(self):
        self.texto.setText("Hola")
        self.boton.setText("Presionado")
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()