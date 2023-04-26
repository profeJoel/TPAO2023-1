import sys
from PyQt6 import QtWidgets, uic

#Importar las vistas
from ej_ui_1 import Ui_VentanaPrincipal

class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        
        #Controlar acción desde el main
        self.boton.clicked.connect(self.saludar)
        
    def saludar(self):
        self.texto.setText(f"Hola {self.entrada.text()}")
        self.entrada.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()