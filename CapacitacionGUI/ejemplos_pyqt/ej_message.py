import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox,  QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel


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
        boton.clicked.connect(self.reaccionar_custom_1)
        
        self.setCentralWidget(boton)
        
    #Primera forma de manejar eventos
    def reaccionar(self):
        # Ejemplo QMessageBox
        ventanita = QMessageBox(self) # Self es el objeto propio y contiene toda la estructura y comportamiento del objeto
        ventanita.setWindowTitle("Ventana Flotante QMessageBox")
        ventanita.setText("Este es un mensaje sin contenido...")
        btn = ventanita.exec()
        
        if btn == QMessageBox.StandardButton.Ok:
            print("Si ok!")
            
        #Primera forma de manejar eventos
    def reaccionar_custom_1(self):
        # Ejemplo QMessageBox
        # Comportamiento o modos de ventana:
        # - about
        # - critical
        # - information
        # - question
        # - warning
        
        btn = QMessageBox.question(
            self,
            "Esta es una ventana modo QUESTION",
            "Es una pregunta?"
            )
        # Lanzar el QMessageBox con un modo permite obviar la execution
        
        if btn == QMessageBox.StandardButton.Yes:
            print("Si")
        else:
            print("NO")

        #Primera forma de manejar eventos
    def reaccionar_custom_2(self):
        # Ejemplo QMessageBox
        # Comportamiento o modos de ventana:
        # - about
        # - critical
        # - information
        # - question
        # - warning
        
        btn = QMessageBox.critical(
            self,
            "Esta es una ventana modo CRITICAL",
            "Archivo no funciona",
            buttons = QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
            defaultButton = QMessageBox.StandardButton.Discard,
            )
        # Lanzar el QMessageBox con un modo permite obviar la execution
        
        if btn == QMessageBox.StandardButton.Discard:
            print("Opción Discard")
        elif btn == QMessageBox.StandardButton.NoToAll:
            print("Opción Not To All")
        else:
            print("Opción Ignore")
            
# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()