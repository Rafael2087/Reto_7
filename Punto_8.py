def Primo(num):
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def Imprimir_Primos():
    num = 1
    while num <= 100:
        if Primo(num):
            print(num)
        num += 1

Imprimir_Primos()
