# Pedimos al usuario que introduzca dos números enteros
numero = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))
# Definimos la función intervalo que imprime los números entre a y b
def intervalo(a, b):
    # Si a es mayor que b, intercambiamos sus valores
    if a > b:
        a, b = b, a
    # Imprimimos los números desde a hasta b (inclusive)
    for i in range(a, b + 1):
        print(i)
# Llamamos a la función intervalo con los números introducidos por el usuario
intervalo(numero, numero2)