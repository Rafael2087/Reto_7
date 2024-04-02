import random

if __name__ == "__main__" :
    i : int = random.randint(1,100)
    j : int = 0
    while j != i :
        if j > i :
            print ("El número es mayor")
        else:
            print ("El número es menor")
        j = int(input("Dijite un número: "))