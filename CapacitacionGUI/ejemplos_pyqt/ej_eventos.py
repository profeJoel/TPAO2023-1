import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

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
        self.entrada = QLineEdit("Ingresa tu nombre")
        self.boton = QPushButton("Ingresar")
        self.boton.clicked.connect(self.reaccionar) #Clicked es una señal
        
        # Se agregan los componentes al layout definido
        caja.addWidget(self.texto)
        #caja.addWidget(self.entrada)
        #caja.addWidget(self.boton)
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
        
        
        
    #Primera forma de manejar eventos
    def reaccionar(self): # Slot
        self.texto.setText("Bienvenido/a " + self.entrada.text())
        self.entrada.setText("")
        self.boton.setText("Ingresado")
        
    # Más acciones de eventos desde mouse
    def mouseMoveEvent(self, e):
        self.texto.setText("El raton se mueve!!!")
        
    def mousePressEvent(self, e):
        # evento button() especifica al botón que gatilla el evento
        # evento buttons() estado de todos los botones del mouse
        # position() la posición del mouse -> QPoint
        
        if e.button() == Qt.MouseButton.RightButton:
            self.texto.setText("Se presionó el botón derecho")
        elif e.button() == Qt.MouseButton.LeftButton:
            self.texto.setText("Se presionó el botón izquierdo")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.texto.setText("Se presionó el botón medio")
            
    
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.texto.setText("Se liberó el botón izquierdo")
        if e.button() == Qt.MouseButton.RightButton:
            self.texto.setText("Se liberó el botón derecho")
        if e.button() == Qt.MouseButton.MiddleButton:
            self.texto.setText("Se liberó el botón medio")
            
    
    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.texto.setText("Se presionó doble el botón izquierdo")
        if e.button() == Qt.MouseButton.RightButton:
            self.texto.setText("Se presionó doble el botón derecho")
        if e.button() == Qt.MouseButton.MiddleButton:
            self.texto.setText("Se presionó doble el botón medio")
    
    
    # Más acciones de eventos desde teclado
    def keyPressEvent(self, e):
        self.texto.setText(f"La tecla presionada es: {e.key()}")
        if e.key() == Qt.Key.Key_W:
            self.texto.setText(f"La tecla presionada es: arriba")
        if e.key() == Qt.Key.Key_S:
            self.texto.setText(f"La tecla presionada es: abajo")
        if e.key() == Qt.Key.Key_A:
            self.texto.setText(f"La tecla presionada es: izquierda")
        if e.key() == Qt.Key.Key_D:
            self.texto.setText(f"La tecla presionada es: derecha")

    
    def keyReleaseEvent(self, e):
        self.texto.setText(f"La tecla liberada es: {e.key()}")
        if e.key() == Qt.Key.Key_W:
            self.texto.setText(f"La tecla liberada es: arriba")
        if e.key() == Qt.Key.Key_S:
            self.texto.setText(f"La tecla liberada es: abajo")
        if e.key() == Qt.Key.Key_A:
            self.texto.setText(f"La tecla liberada es: izquierda")
        if e.key() == Qt.Key.Key_D:
            self.texto.setText(f"La tecla liberada es: derecha")
            
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()