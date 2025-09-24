# Pedimos al usuario que introduzca dos números enteros
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
# Definimos la función calculadora que realiza una operación básica
def calculadora(a, b, operacion):
    if operacion == 1:
        resultado = a + b
    elif operacion == 2:
        resultado = a - b
    elif operacion == 3:
        resultado = a * b
    elif operacion == 4:
        resultado = a / b
    else:
        resultado = "Operación no válida"
    return resultado
# Pedimos al usuario que elija una operación
op = int(input("¿Qué operación deseas realizar? (1=suma, 2=resta, 3=multiplicación, 4=división): "))
# Llamamos a la función calculadora con los números y la operación elegida
resultado = calculadora(num1, num2, op)
# Imprimimos el resultado
print("Resultado:", resultado)