letra = str(input("Introduce una letra: ")).lower()

def vocal(letra):
    if letra in 'aeiou':
        return True
    else:
        return False
if vocal(letra):
    print("La letra", letra, "es una vocal.")
else:
    print("La letra", letra, "no es una vocal.")