 class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
        
    def eat(self):
        print(f"{self.name} está comiendo algo...")
        
    def make_sound(self):
        print(f"{self.name} hace un sonido...")