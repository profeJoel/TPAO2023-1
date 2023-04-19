import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class VentanitaCustomizable(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ventanita flotante customizable")
        
        # Estos botones permitiran enviar información a la ventana principal
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.boton = QDialogButtonBox(QBtn)
        self.boton.accepted.connect(self.accept)
        self.boton.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        mensaje = QLabel("Ventanita desplegada... ¿Quieren terminar la Clase?")
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.boton)
        self.setLayout(self.layout)
        


# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(400,200))
        
        ####boton = QPushButton("Presioname", lambda clicked: print("Acción con Lambda Expressions"))
        boton = QPushButton("Lanzar Dialog")
        boton.clicked.connect(self.reaccionar)
        
        self.setCentralWidget(boton)
        
    #Primera forma de manejar eventos
    def reaccionar(self):
        # Ejemplo dialog simple!!!
        """
        ventanita = QDialog(self)
        ventanita.setWindowTitle("Ventana Flotante")
        ventanita.exec()
        """
        ventanita = VentanitaCustomizable()
        if ventanita.exec():
            print("La respuesta es SI!!")
        else:
            print("La respuesta es NO!!")

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()