from Animal import Animal

class Gato(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
        self.specie = "felino"
        
    def make_sound(self):
        return f"{self.nombre} de especie {self.specie} hace MIAUU!!!"
    
    def sleep(self):
        print(f"{self.nombre} está durmiendo...ZZZZ")