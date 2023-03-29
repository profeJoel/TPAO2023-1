from Exterior import Exterior

if __name__ == "__main__":
    
    objeto_exterior = Exterior("Estoy en la clase exterior")
    print(objeto_exterior)
    
    #Opción 1
    #objeto_interior = objeto_exterior.Interior("Estoy en la clase interior, ahora si...")
    #print(objeto_interior)
    
    #Opción 2
    objeto_interior_instanciado = objeto_exterior.instanciador()
    print(objeto_interior_instanciado)