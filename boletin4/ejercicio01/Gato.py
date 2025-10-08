
# Definimos las clases hijas
from Animal import Animal


class Gato(Animal):
    # Constructor
    def __init__(self, nombre, numPatas):
        super().__init__(nombre, numPatas)
    
    # Métodos
    def habla(self):
        cadena = "Miau"
        return cadena
    
    def __str__(self):
        cadena = f"Soy un gato. {super().__str__()}"
        return cadena