# formato de valores separados por coma (CSV)
# permite ver la información como si fueran filas y columnas
# Ej: persona (rut, nombre, fecha_nacimiento)
# "11111111-1", "Juan Perez", "01/01/2001"
# "22222222-2", "Lucho Mendez", "02/02/2002"
# ...

if __name__ == "__main__":
    try:
        texto_csv = open("archivo_personas.csv", "a")
        texto_csv.write('"11111111-1", "Juan Perez", "01/01/2001"\n')
        texto_csv.write('"22222222-2", "Lucho Mendez", "02/02/2002"\n')
    
    except Exception as e:
        print(f"El archivo 'archivo_personas.csv' no se encuentra... {e}")