from dataclasses import dataclass

@dataclass
class Persona:
    rut: str
    nombre: str
    fecha_nacimiento: str

    def __str__(self):
        return f"La persona es {self.nombre}(rut:{self.rut}) fecha_nacimiento: {self.fecha_nacimiento}"