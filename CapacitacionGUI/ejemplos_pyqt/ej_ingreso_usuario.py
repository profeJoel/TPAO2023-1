import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QGridLayout, QPushButton, QStackedLayout, QVBoxLayout, QHBoxLayout, QWidget

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Aplicación en PyQt6")
        self.setFixedSize(QSize(600,300))
        caja_grande = QVBoxLayout()
        caja_superior = QHBoxLayout()
        self.caja_inferior = QStackedLayout()
        
        #Componentes caja superior
        boton1 = QPushButton("Iniciar Sesión")
        boton2 = QPushButton("Registrarse")
        boton3 = QPushButton("Recuperar Contraseña")
        caja_superior.addWidget(boton1)
        caja_superior.addWidget(boton2)
        caja_superior.addWidget(boton3)
        
        boton1.clicked.connect(self.cambiar_a_layout_1)
        boton2.clicked.connect(self.cambiar_a_layout_2)
        boton3.clicked.connect(self.cambiar_a_layout_3)
        
        #Componentes caja inferior
        # QStackedLayout No tiene el metodo addLayout
        # QStackedLayout -> QWidget -> Layout
        contenedor1 = QWidget()
        layout1 = QVBoxLayout(contenedor1)
        contenedor2 = QWidget()
        layout2 = QVBoxLayout(contenedor2)
        contenedor3 = QWidget()
        layout3 = QVBoxLayout(contenedor3)
        
        #layout1
        texto_inicio = QLabel("Inicio de Sesión")
        formulario_inicio = QGridLayout()
        inicio_usuario = QLabel("Usuario")
        inicio_entrada_usuario = QLineEdit()
        inicio_psw = QLabel("Password")
        inicio_entrada_psw = QLineEdit()
        inicio_entrada_psw.setEchoMode(QLineEdit.EchoMode.Password)
        inicio_btn = QPushButton("Iniciar Sesión")
        
        formulario_inicio.addWidget(inicio_usuario, 0,0)
        formulario_inicio.addWidget(inicio_entrada_usuario, 0,1)
        formulario_inicio.addWidget(inicio_psw, 1,0)
        formulario_inicio.addWidget(inicio_entrada_psw, 1,1)
        formulario_inicio.addWidget(inicio_btn, 2,1)
        
        layout1.addWidget(texto_inicio)
        layout1.addLayout(formulario_inicio)
        
        #layout2
        texto_registrar = QLabel("Registrarse")
        formulario_registrar = QGridLayout()
        registrar_nombre = QLabel("Nombre")
        registrar_entrada_nombre = QLineEdit()
        registrar_apellido = QLabel("Apellido")
        registrar_entrada_apellido = QLineEdit()
        registrar_usuario = QLabel("Usuario")
        registrar_entrada_usuario = QLineEdit()
        registrar_psw = QLabel("Password")
        registrar_entrada_psw = QLineEdit()
        registrar_btn = QPushButton("Iniciar Sesión")
        
        formulario_registrar.addWidget(registrar_nombre, 0,0)
        formulario_registrar.addWidget(registrar_entrada_nombre, 0,1)
        formulario_registrar.addWidget(registrar_apellido, 0,2)
        formulario_registrar.addWidget(registrar_entrada_apellido, 0,3)
        formulario_registrar.addWidget(registrar_usuario, 1,0)
        formulario_registrar.addWidget(registrar_entrada_usuario, 1,1)
        formulario_registrar.addWidget(registrar_psw, 1,2)
        formulario_registrar.addWidget(registrar_entrada_psw, 1,3)
        formulario_registrar.addWidget(registrar_btn, 2,3)
        
        layout2.addWidget(texto_registrar)
        layout2.addLayout(formulario_registrar)
        
        
        #layout3
        texto_recuperar = QLabel("Inicio de Sesión")
        formulario_recuperar = QHBoxLayout()
        recuperar_usuario = QLabel("Usuario")
        recuperar_entrada_usuario = QLineEdit()
        recuperar_btn = QPushButton("Iniciar Sesión")
        
        formulario_recuperar.addWidget(recuperar_usuario)
        formulario_recuperar.addWidget(recuperar_entrada_usuario)
        
        layout3.addWidget(texto_recuperar)
        layout3.addLayout(formulario_recuperar)
        layout3.addWidget(recuperar_btn)
        
        
        # Configuración para agregar layout en QStackedLayout
        self.caja_inferior.addWidget(contenedor1)
        self.caja_inferior.addWidget(contenedor2)
        self.caja_inferior.addWidget(contenedor3)
        
        
        #Agregar los layout interiores al VBox
        caja_grande.addLayout(caja_superior)
        caja_grande.addLayout(self.caja_inferior)
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja_grande)
        self.setCentralWidget(ventana)
        
    def cambiar_a_layout_1(self):
        self.caja_inferior.setCurrentIndex(0)
        
    def cambiar_a_layout_2(self):
        self.caja_inferior.setCurrentIndex(1)
        
    def cambiar_a_layout_3(self):
        self.caja_inferior.setCurrentIndex(2)
        
    #Primera forma de manejar eventos
    def reaccionar(self):
        pass
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()