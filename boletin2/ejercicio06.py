# Pedimos una cadena de texto como entrada
cadena = str(input("Introduce una cadena de texto: "))
# Generamos una diccionario que cuente la frecuencia de cada palabra en la cadena
palabras = {}
for i in cadena.split():
    if i in palabras:
        palabras[i] += 1
    else:
        palabras[i] = 1
# Mostramos el resultado
print(palabras)