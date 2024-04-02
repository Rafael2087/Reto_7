import random
def Divisores (n1 : int , n2 : int):
    if n1 % n2 == 0 :
        return True
    else:
        return False
if __name__ == "__main__" :
    i : int = random.randint(2,50)
    j : int = 1

    while i >= j :
        k : bool = Divisores(i,j)
        if k == True :
            print(str(j) + " es divisor de " + str (i))
        j = j + 1
        