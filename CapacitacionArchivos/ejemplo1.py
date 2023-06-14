# Ruta relativa -> donde esta el archivo desde el punto de ejecución
# Ruta Absoluta -> donde esta el archivo desde la raíz del computador

# Alcanzar el archivo
# R. Relativa -> "texto1.txt"
# R. Absoluta -> "/Users/joelsebastiantorrescarrasco/Documents/Ulagos/TPA/TPAO2023-1/CapacitacionArchivos/texto1.txt"

#Open es el método para poder hacer manejar el contenido de un archivo
# modo implica que:
# "r" corresponde a solo lectura
# "w" corresponde a escritura (sobreescritura)
# "a" corresponde a escritura, pero agregando contenido al final
# "x" corresponde a crear el archivo

# modos extra_
# "t" archivo de texto
# "b" archivo binarioss

import os

if __name__ == "__main__":

    #Leer archivo plano

    #Excepciones
    try: # intentar una sección de código
        texto_recuperado = open("/Users/joelsebastiantorrescarrasco/Documents/Ulagos/TPA/TPAO2023-1/CapacitacionArchivos/texto1.txt", "r")
        #texto_recuperado = open("texto1.txt", "r")
        print(texto_recuperado.read())
        texto_recuperado.close()

    except Exception as e: # La acción de capturar la excepción generada
        print(f"El archivo 'texto1.txt' no se encuentra... {e}")

    #Escribir un archivo
    try:
        #texto_escrito = open("CapacitacionArchivos/texto2.txt", "w") # si no encuentra archivo, entonces lo crea
        texto_escrito = open("CapacitacionArchivos/texto2.txt", "a") # si no encuentra archivo, entonces lo crea
        texto_escrito.write("Se agregan nuevas lineas\n")
        texto_escrito.write("Sin problemas de sobreescritura\n")
        texto_escrito.close()
    except Exception as e:
        print(f"El archivo 'texto1.txt' no se encuentra... {e}")

    # Crear solamente archivo
    try:
        #texto_creado = open("CapacitacionArchivos/textocreado.txt", "x")
        #texto_creado.close()

        #Para eliminar un archivo
        os.remove("CapacitacionArchivos/textocreado.txt")
    except Exception as e:
        print(f"El archivo 'texto1.txt' no se encuentra... {e}")