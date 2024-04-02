if __name__ == "__main__":
    i : float = 25000000
    j : float = 18900000
    k : int = 0
    while i > j :
        i = (102/100)*i
        j = (103/100)*j
        k = k + 1
         
    print("La población B superara a la población A en el año " + str(2022 + k))

