from Animal import Animal

class Gato(Animal):
    
    def __init__(self, name, specie, sex, age, weight, color, texture):
        super().__init__(name, specie)
        self.sex = sex
        self.age = age
        self.weight = weight
        self.__color = color
        self.texture = texture
        
    def purr(self):
        print(f"{self.name} hace purrrrrr...")
        
    #Los atributos que deben ser privados deben tener un getter y setter
    # Getter para entregar información
    # Setter para modificar información
    
    def get_color(self):
        return self.__color
    
    def set_color(self, nuevo_color):
        if nuevo_color in ["negro", "blanco", "marrón", "gris", "rojizo"]:
            self.__color = nuevo_color
        else:
            print("COLOR NO ACEPTADO...")
            
    def make_sound(self):
        print(f"{self.name} hace MIAUUUU...")