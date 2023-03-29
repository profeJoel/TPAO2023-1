from Animal import Animal

class Perro(Animal):
    def __init__(self, name, specie, pedigri):
        super().__init__(name, specie)
        self.pedigri = pedigri
        
    
    def make_sound(self):
        print(f"{self.name} hace GUAU!!!")