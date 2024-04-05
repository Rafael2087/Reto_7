if __name__ == "__main__":
    i : int = int(input("Dijite un número natural: "))
    j : int = i
    k : int = 1
    while (j > 1):
        j = j - 1
        i = i * j
    print("El factorial de " + str(k) + " es " + str(i))
