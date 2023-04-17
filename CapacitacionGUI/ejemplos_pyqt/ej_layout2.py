import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget

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
        caja = QGridLayout()
        
        ####boton = QPushButton("Presioname", lambda clicked: print("Acción con Lambda Expressions"))
        b00 = QPushButton("0,0")
        b01 = QPushButton("0,1")
        b02 = QPushButton("0,2")
        b10 = QPushButton("1,0")
        b11 = QPushButton("1,1")
        b12 = QPushButton("1,2")
        b20 = QPushButton("2,0")
        b21 = QPushButton("2,1")
        b22 = QPushButton("2,2")
        #boton3 = QPushButton("Boton3")
        #boton.clicked.connect(self.reaccionar)
        
        # Se agregan los componentes al layout definido
        caja.addWidget(b00, 0,0)
        caja.addWidget(b01, 0,1)
        caja.addWidget(b02, 0,2)
        caja.addWidget(b10, 1,0)
        caja.addWidget(b11, 1,1)
        caja.addWidget(b12, 1,2)
        caja.addWidget(b20, 2,0)
        caja.addWidget(b21, 2,1)
        caja.addWidget(b22, 2,2)
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