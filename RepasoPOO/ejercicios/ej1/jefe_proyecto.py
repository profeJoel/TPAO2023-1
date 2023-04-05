from candidato import Candidato

class Jefe_Proyecto(Candidato):
    
    def __init__(self, id, name, rol, equipo):
        self.id = id
        self.name = name
        self.rol = rol
        self.equipo = equipo
        self.capabilities = []
        
    def add_capability(self, cap:str):
        self.capabilities.append(cap)
        
    def get_id(self):
        return self.id
    
    def get_capabilities(self):
        return self.capabilities.__len__()