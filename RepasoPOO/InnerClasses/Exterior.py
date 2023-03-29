class Exterior:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        
        
    def __str__(self):
        return f"{self.mensaje}"
    
    def instanciador(self):
        # obliga al programador a tener una secuencia obligatoria para crear una instancia
        return self.__Interior("Mensaje preestablecido")
    
    class __Interior:
        def __init__(self, mensaje):
            self.mensaje_interior = mensaje
            
        def __str__(self):
            return f"{self.mensaje_interior}"