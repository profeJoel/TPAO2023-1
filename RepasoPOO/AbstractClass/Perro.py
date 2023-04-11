from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
        self.specie = "canino"
        
    def make_sound(self):
        return f"{self.nombre} de especie {self.specie} hace GUAUU!!!"
    
        
    def sleep(self):
        print(f"{self.nombre} está durmiendo...ZZZZ")