def Cuadrado (x : int):
    Square = x ** 2
    return Square
    
if __name__ == "__main__" :
    i : int = 1
    while ( i <= 100) :
        print ("El cuadrado de " + str(i) + " es igual a " + str(Cuadrado(i)))
        i += 1
        