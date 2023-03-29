from abc import ABC, abstractmethod

class Animal(ABC):
    
    # ABC indica que no se debe tener un constructor
    
    @abstractmethod
    def make_sound(self):
        pass