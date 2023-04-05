from candidato import Candidato
from empleado import Empleado
from gerente import Gerente
from jefe_proyecto import Jefe_Proyecto


if __name__ == "__main__":
    
    gerente1 = Gerente(1, "Pedro", "Gerente TI")
    gerente1.add_capability("Liderazgo")
    gerente1.add_capability("Empatía")
    gerente1.add_capability("Trabajo en equipo")
    gerente1.add_capability("Proactividad")
    
    jfp1 = Jefe_Proyecto(2, "David", "Jefe de desarrollo de telecomunicaciones", "telecomunicaciones")
    jfp1.add_capability("Liderazgo")
    jfp1.add_capability("Control de riesgo")
    jfp1.add_capability("Experiencia")
    
    empleado1 = Empleado(3, "Luis")
    empleado1.add_capability("Puntualidad")
    empleado1.add_capability("Colaboración")
    empleado1.add_capability("Creatividad")
    empleado1.add_capability("Trabajo en equipo")
    empleado1.add_capability("Autogestion")
    
    candidatos = []
    candidatos.append(gerente1)
    candidatos.append(jfp1)
    candidatos.append(empleado1)
    
    for persona in candidatos:
        print(type(type(persona)))
    
    