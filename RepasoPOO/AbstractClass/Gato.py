from Animal import Animal

class Gato(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def make_sound(self):
        return f"{self.nombre} hace MIAUU!!!"