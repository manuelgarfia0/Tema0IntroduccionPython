# Pedimos al usuario que introduzca una letra
letra = str(input("Introduce una letra: ")).lower()
# Definimos la función vocal que comprueba si una letra es vocal
def vocal(letra):
    # Comprobamos si la letra está en la cadena de vocales
    if letra in 'aeiou':
        letra_vocal = True
    else:
        letra_vocal = False
    return letra_vocal
# Imprimimos el resultado llamando a la función vocal con la letra introducida por el usuario
if vocal(letra):
    print("La letra", letra, "es una vocal.")
else:
    print("La letra", letra, "no es una vocal.")