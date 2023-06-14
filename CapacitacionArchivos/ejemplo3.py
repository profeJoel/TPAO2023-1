#Leer los datos de un archivo csv

from Persona import Persona

if __name__ == "__main__":
    lista_personas = []

    try:
        archivo = open("archivo_personas.csv", "r")
        lineas = archivo.readlines()

        for linea in lineas:
            dato = linea.split(",")
            rut = dato[0].replace('"','')
            nombre = dato[1].replace('"','')
            fecha_nacimiento = dato[2].replace('"','')
            lista_personas.append(Persona(rut,nombre,fecha_nacimiento))
        
        for persona in lista_personas:
            print(persona)

    
    except Exception as e:
        print(f"El archivo 'archivo_personas.csv' no se encuentra... {e}")