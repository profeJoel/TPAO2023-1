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
        self.setFixedSize(QSize(400,600))
        #caja = QHBoxLayout()
        caja_grande = QVBoxLayout()
        caja = QGridLayout()
        
        #Componentes de la interfaz
        self.historial = QLabel("")
        self.display = QLineEdit("")
        self.A = None
        self.B = None
        self.Resultado = None
        self.operacion = None
        
        self.btn0 = QPushButton("0")
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        
        self.btn_igual = QPushButton("=")
        self.btn_suma = QPushButton("+")
        self.btn_resta = QPushButton("-")
        self.btn_multi = QPushButton("*")
        self.btn_div = QPushButton("/")
        
        #Acciones
        self.btn0.clicked.connect(self.agregar0)
        self.btn1.clicked.connect(self.agregar1)
        self.btn2.clicked.connect(self.agregar2)
        self.btn3.clicked.connect(self.agregar3)
        self.btn4.clicked.connect(self.agregar4)
        self.btn5.clicked.connect(self.agregar5)
        self.btn6.clicked.connect(self.agregar6)
        self.btn7.clicked.connect(self.agregar7)
        self.btn8.clicked.connect(self.agregar8)
        self.btn9.clicked.connect(self.agregar9)
        self.btn_igual.clicked.connect(self.calcular_igual)
        self.btn_suma.clicked.connect(self.calcular_suma)
        self.btn_resta.clicked.connect(self.calcular_resta)
        self.btn_multi.clicked.connect(self.calcular_multi)
        self.btn_div.clicked.connect(self.calcular_div)
        
        
        # Se agregan los componentes al layout definido
        caja_grande.addWidget(self.historial)
        caja_grande.addWidget(self.display)
        caja.addWidget(self.btn_div, 0,3)
        caja.addWidget(self.btn7, 1,0)
        caja.addWidget(self.btn8, 1,1)
        caja.addWidget(self.btn9, 1,2)
        caja.addWidget(self.btn_multi, 1,3)
        
        caja.addWidget(self.btn4, 2,0)
        caja.addWidget(self.btn5, 2,1)
        caja.addWidget(self.btn6, 2,2)
        caja.addWidget(self.btn_resta, 2,3)
        
        caja.addWidget(self.btn1, 3,0)
        caja.addWidget(self.btn2, 3,1)
        caja.addWidget(self.btn3, 3,2)
        caja.addWidget(self.btn_suma, 3,3)
        
        caja.addWidget(self.btn0, 4,1)
        caja.addWidget(self.btn_igual, 4,3)

        
        caja_grande.addLayout(caja)
        #asigna el layout a la ventana

        ventana = QWidget()
        ventana.setLayout(caja_grande)
        self.setCentralWidget(ventana)
        
        
        
    #Primera forma de manejar eventos
    def agregar0(self):
        self.display.setText(self.display.text() + "0")
        self.historial.setText(self.historial.text() + "0")
    
    def agregar1(self):
        self.display.setText(self.display.text() + "1")
        self.historial.setText(self.historial.text() + "1")
    
    def agregar2(self):
        self.display.setText(self.display.text() + "2")
        self.historial.setText(self.historial.text() + "2")
        
    def agregar3(self):
        self.display.setText(self.display.text() + "3")
        self.historial.setText(self.historial.text() + "3")
    
    def agregar4(self):
        self.display.setText(self.display.text() + "4")
        self.historial.setText(self.historial.text() + "4")
    
    def agregar5(self):
        self.display.setText(self.display.text() + "5")
        self.historial.setText(self.historial.text() + "5")
    
    def agregar6(self):
        self.display.setText(self.display.text() + "6")
        self.historial.setText(self.historial.text() + "6")
    
    def agregar7(self):
        self.display.setText(self.display.text() + "7")
        self.historial.setText(self.historial.text() + "7")
    
    def agregar8(self):
        self.display.setText(self.display.text() + "8")
        self.historial.setText(self.historial.text() + "8")
    
    def agregar9(self):
        self.display.setText(self.display.text() + "9")
        self.historial.setText(self.historial.text() + "9")
        
    def calcular_suma(self):
        if self.display.text() != "" and self.display.text() != "Indeterminado":
            self.A = float(self.display.text()) 
            self.display.setText("")
            self.historial.setText(self.historial.text() + "+")
            self.operacion = "suma"
        
    def calcular_resta(self):
        if self.display.text() != "" and self.display.text() != "Indeterminado":
            self.A = float(self.display.text())
            self.display.setText("")
            self.historial.setText(self.historial.text() + "-")
            self.operacion = "resta"
    
    def calcular_multi(self):
        if self.display.text() != "" and self.display.text() != "Indeterminado":
            self.A = float(self.display.text())
            self.display.setText("")
            self.historial.setText(self.historial.text() + "*")
            self.operacion = "multi"
        
    def calcular_div(self):
        if self.display.text() != "" and self.display.text() != "Indeterminado":
            self.A = float(self.display.text())
            self.display.setText("")
            self.historial.setText(self.historial.text() + "/")
            self.operacion = "div"
        
    def calcular_igual(self):
        self.B = float(self.display.text()) if self.display.text() != "" else None
        
        if self.operacion == "suma":
            self.Resultado = self.A + self.B
        elif self.operacion == "resta":
            self.Resultado = self.A - self.B
        elif self.operacion == "multi":
            self.Resultado = self.A * self.B
        elif self.operacion == "div":
            self.Resultado = float(self.A / self.B) if self.B != 0 else "Indeterminado"
        else:
            self.Resultado = None
            
        if self.Resultado is not None:
            self.display.setText(str(self.Resultado))
            self.Resultado = None
        else:
            self.display.setText("")
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()