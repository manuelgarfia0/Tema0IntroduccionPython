# Dicionario que almacene las letras del abecedario como claves y una puntuación como valor
abecedario = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3,
               "n": 1, "o": 1, "p": 3, "q": 5, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}
# Pedimos una palabra al usuario
palabra = str(input("Introduce una palabra: "))
# Calculamos la puntuación total de la palabra
puntuacion = 0
for letra in palabra.lower():
    if letra in abecedario:
        puntuacion += abecedario[letra]
# Mostramos el resultado
print("La puntuación total de la palabra", palabra, "es:", puntuacion)