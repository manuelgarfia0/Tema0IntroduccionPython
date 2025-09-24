numero = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

def intervalo(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        print(i)

intervalo(numero, numero2)