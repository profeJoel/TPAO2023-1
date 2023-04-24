import sys
from random import randint
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class OtraVentana(QWidget):
    """
        Es la clase de cualquier ventana que se quiera desplegar
    """
    def __init__(self):
        super().__init__()
        capa = QVBoxLayout()
        self.setWindowTitle("Ventana Secundaria")
        self.texto_1 = QLabel(f"Esta es otra ventana con random: {randint(0,100)}")
        capa.addWidget(self.texto_1)
        self.setLayout(capa)


# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        #self.ventana_secundaria = None # opción de ventana no creada y desplegada en btn
        self.ventana_secundaria = OtraVentana() # En toda la aplicación va a existir una sola ventana secundaria
        self.contador_clicks = 0
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(400,200))
        
        ####boton = QPushButton("Presioname", lambda clicked: print("Acción con Lambda Expressions"))
        boton = QPushButton("Lanzar Nueva Ventana")
        boton.clicked.connect(self.reaccionar)
        
        self.setCentralWidget(boton)
        
    #Primera forma de manejar eventos
    def reaccionar(self):
        # Opción de ventana Persistente hasta el cierre de la aplicación
        """
        if self.ventana_secundaria is None:
            self.ventana_secundaria = OtraVentana() # Se crea una sola en toda la ejecución del programa
        self.ventana_secundaria.show() # permite desplegar la ventana en pantalla
        """
        # Opción 2 de ventana que se crea y se elimina cada vez que se lanza el evento del boton
        """
        if self.ventana_secundaria is None:
            self.ventana_secundaria = OtraVentana() # Se crea una sola en toda la ejecución del programa
            self.ventana_secundaria.show() # permite desplegar la ventana en pantalla
        else:
            self.ventana_secundaria = None # se cierra la ventana pero puede quedar una referencia a una ventana desplegada.
        """
         
        # Opción 2 de ventana que se crea y se elimina cada vez que se lanza el evento del boton
        """
        if self.ventana_secundaria is None:
            self.ventana_secundaria = OtraVentana() # Se crea una sola en toda la ejecución del programa
            self.ventana_secundaria.show() # permite desplegar la ventana en pantalla
        else:
            self.ventana_secundaria.close() # se asegura que la ventana ya no está en ejecución
            self.ventana_secundaria = None
        """
        
        # Opción 3
        # self.ventana_secundaria.show()
        
        #Opción 4 -> desplegando ventanas con show y hide
        if self.ventana_secundaria.isVisible():
            self.ventana_secundaria.hide() # hace que la ventana sea invisible: visible = False
        else:
            self.ventana_secundaria.show() # hace que la ventan sea visible: visible = True

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()