# Pedimos al usuario que introduzca dos números enteros
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
# Definimos la función mayor que devuelve el mayor de dos números
def mayor(a, b):
    # Comparamos los dos números y devolvemos el mayor
    if a > b:
        return a
    else:
        return b
# Imprimimos el resultado llamando a la función mayor con los números introducidos por el usuario
print("El número mayor es:", mayor(num1, num2))