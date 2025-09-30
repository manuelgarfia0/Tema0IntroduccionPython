import random
# Crear una lista vacía
num = []
# Rellenar la lista con 100 números aleatorios entre 1 y 10
for i in range(100):
    numero = random.randint(1, 10)
    num.append(numero)
# Pedir un valor al usuario y mostrar cuántas veces aparece ese valor en la lista
numeroBuscar = int(input("Introduce un número entre 1 y 10: "))
contador = 0
for n in num:
    if n == numeroBuscar:
        contador += 1
# Mostrar la lista y el resultado
print(num)
print("El número", numeroBuscar, "aparece", contador, "veces en la lista.")