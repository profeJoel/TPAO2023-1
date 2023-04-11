from Animal import Animal
from Gato import Gato
from Perro import Perro

if __name__ == "__main__":
    """
    animal = Animal()
    print(animal)
    """
    oscar = Gato("Oscar")
    print(oscar.make_sound())
    
    
    firulais = Perro("Firulais")
    print(firulais.make_sound())
    
    oscar.eat()
    firulais.eat()
    
    oscar.sleep()
    firulais.sleep()