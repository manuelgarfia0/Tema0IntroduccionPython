# Declaro las variables suma y número
suma = 0
num = 0
# Pido al usuario que introduzca un número
num = int(input("Introduce un número entero positivo (o un número negativo para terminar): "))
# Mientras el número sea positivo, lo sumo a la variable suma
while num >= 0:
    # Si el número es positivo, lo sumo a la variable suma
    suma += num
    # Pido al usuario que introduzca un número
    num = int(input("Introduce un número entero positivo (o un número negativo para terminar): "))
# Muestro la suma de los números positivos introducidos
print("La suma de los números positivos introducidos es:", suma)