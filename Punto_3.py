if __name__ == "__main__":
    i : int = int(input("Dijite un entero: "))
    if i % 2 != 0 :
        i = i - 1
    while (i >= 2):
        print(i)
        i = i - 2
    if i < 2 :
        print("Dijite un número mayor o igual a 2")
