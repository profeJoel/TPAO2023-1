from abc import ABC, abstractmethod

class Animal(ABC):
    
    # ABC indica que no se debe tener un constructor
    
    specie: str
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def eat(self):
        print(f"Este animal {self.specie} está comiendo...")
        
    @abstractmethod
    def sleep(self):
        pass