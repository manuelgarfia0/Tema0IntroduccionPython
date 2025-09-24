# Importamos la librería random para generar un número aleatorio
import random
# Generamos un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 101)
# Inicializamos la variable intento
intento = 0
# Usamos un bucle while para que hasta que el usuario no adivine el número o se rinda siga pidiendo números
while intento != numero_secreto and intento != -1:
    # Pedimos al usuario que introduzca un número
    intento = int(input("Adivina el número secreto (entre 1 y 100): "))
    # Comprobamos si el número es mayor, menor o igual al número secreto
    if intento < numero_secreto and intento != -1:
        print("Demasiado bajo. Inténtalo de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Inténtalo de nuevo.")
    # Introduciendo -1 el usuario se rinde
    elif intento == -1:
        print("Te has rendido. El número secreto era:", numero_secreto)
    else:
        print("¡Felicidades! Has adivinado el número secreto.")