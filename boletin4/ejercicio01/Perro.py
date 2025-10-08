

from Animal import Animal


class Perro(Animal):
    # Constructor
    def __init__(self, nombre, numPatas):
        super().__init__(nombre, numPatas)
    
    # Métodos
    def habla(self):
        cadena = "Guau"
        return cadena
    
    def __str__(self):
        cadena = f"Soy un perro. {super().__str__()}"
        return cadena