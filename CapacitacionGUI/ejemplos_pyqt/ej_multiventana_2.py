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
        self.ventana_secundaria_1 = OtraVentana() # En toda la aplicación va a existir una sola ventana secundaria
        self.ventana_secundaria_2 = OtraVentana() # En toda la aplicación va a existir una sola ventana secundaria
        
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(400,200))
        capa = QVBoxLayout()
        
        ####boton = QPushButton("Presioname", lambda clicked: print("Acción con Lambda Expressions"))
        boton1 = QPushButton("Lanzar Nueva Ventana 1")
        # boton1.clicked.connect(self.reaccionar1)
        boton1.clicked.connect(lambda checked: self.reaccionar(self.ventana_secundaria_1))
        boton2 = QPushButton("Lanzar Nueva Ventana 2")
        # boton2.clicked.connect(self.reaccionar2)
        boton2.clicked.connect(lambda checked: self.reaccionar(self.ventana_secundaria_2))
        capa.addWidget(boton1)
        capa.addWidget(boton2)
        
        w = QWidget()
        w.setLayout(capa)
        self.setCentralWidget(w)
        
    #Código unificado de show y hide para cualquier ventana
    def reaccionar(self, otra_ventana):
        #Opción 4 -> desplegando ventanas con show y hide
        if otra_ventana.isVisible():
            otra_ventana.hide() # hace que la ventana sea invisible: visible = False
        else:
            otra_ventana.show() # hace que la ventan sea visible: visible = True

    #Primera forma de manejar eventos
    def reaccionar1(self):
        
        #Opción 4 -> desplegando ventanas con show y hide
        if self.ventana_secundaria_1.isVisible():
            self.ventana_secundaria_1.hide() # hace que la ventana sea invisible: visible = False
        else:
            self.ventana_secundaria_1.show() # hace que la ventan sea visible: visible = True


    #Primera forma de manejar eventos
    def reaccionar2(self):
        
        #Opción 4 -> desplegando ventanas con show y hide
        if self.ventana_secundaria_2.isVisible():
            self.ventana_secundaria_2.hide() # hace que la ventana sea invisible: visible = False
        else:
            self.ventana_secundaria_2.show() # hace que la ventan sea visible: visible = True
            
# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()