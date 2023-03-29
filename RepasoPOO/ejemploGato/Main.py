from Gato import Gato
from Perro import Perro

if __name__ == "__main__":
    oscar = Gato("Oscar", "Felino","macho", 3, 7, "Marrón", "Rayado")
    luna = Gato("Luna", "Felino", "hembra", 2, 5, "gris", "lisa")
    
    oscar.purr()
    luna.purr()
    """
    print(f"{oscar.name} tiene el color {oscar.__color}")
    
    oscar.__color = "verde"
    
    print(f"{oscar.name} tiene el color {oscar.__color}")
    """
    
    print(f"{oscar.name} tiene el color {oscar.get_color()}")
    
    oscar.set_color("verde")
    
    print(f"{oscar.name} tiene el color {oscar.get_color()}")
    
    oscar.eat()
    luna.eat()
    
    oscar.make_sound()
    luna.make_sound()
    
    firulais = Perro("Firulais", "Canido", "Puro")
    firulais.make_sound()