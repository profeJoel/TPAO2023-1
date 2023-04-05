from abc import ABC, abstractmethod

class Candidato(ABC):
    
    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def get_capabilities(self):
        pass