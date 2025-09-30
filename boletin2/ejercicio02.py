# Pedimos al usuario que introduzca diez números positivos
num = []
for i in range(10):
    numero = int(input("Introduce un número positivo: "))
    num.append(numero)
# Indicamos el mayor y el menor número de la lista recorriendola
mayor = num[0]
menor = num[0]
# Recorremos la lista para encontrar el mayor y el menor número
for n in num:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
print("El mayor es:", mayor)
print("El menor es:", menor)
