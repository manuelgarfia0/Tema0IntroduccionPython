# Crea un diciconario para las letras que intoduce el usuario y las letras a las que se deben cambiar
encriptador = {"e":"p", "y":"v", "k":"i", "m":"u", "p":"m", "q":"t", "r":"e", "t":"r", "u":"q", "v":"s"}
# Pedimos una cadena la usuario
frase = str(input("Introduce una cadena de texto: "))
# Generamos una nueva cadena encriptada
frase_encriptada = ""
for letra in frase:
    if letra in encriptador:
        frase_encriptada += encriptador[letra]
    else:
        frase_encriptada += letra
# Mostramos el resultado
print("La cadena encriptada es:", frase_encriptada)