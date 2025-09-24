# Pedir al usuario que introduzca un número
numero = int(input("Introduce un número: "))
# Inicializar la variable factorial
factorial = 1
# Calcular el factorial del número introducido
for i in range(numero, 0, -1):
    factorial *= i
# Mostrar el resultado
print("El factorial de", numero, "es", factorial)