import math

def doble(n):
    return n*2

def distancia(dX,dY):
    return math.sqrt(dX+dY)

if __name__ == "__main__":
    print(doble(5))
    
    #Expresión Lambda
    por_dos = lambda n : n*2
    
    print(por_dos(5))
    
    delta = lambda p1,p2 : p2-p1
    
    x1, x2 = 1,1
    y1, y2 = 2,1
    
    print(f"la diferencia es: {distancia(delta(x1,x2)**2, delta(y1,y2)**2)}")
    