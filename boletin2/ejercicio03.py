# Pedir al usuario que introduzca 8 números enteros
num = []
for i in range(8):
    numero = int(input("Introduce un número entero: "))
    num.append(numero)
# Mostrar los números con par o impar al lado del número dependiendo de cada uno
for n in num: 
    if n % 2 == 0:
        print(n, "par")
    else:
        print(n, "impar")