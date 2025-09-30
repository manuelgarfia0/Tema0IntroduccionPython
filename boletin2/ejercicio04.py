# Crear una lista vacía
num = []
# Pedir al usuario que introduzca 10 números enteros
for i in range (10):
    numero = int(input("Introduce un número entero: "))
    num.append(numero)
# Mostrar la lista ordenada de mayor a menor
num.sort(reverse=True)
print(num)
