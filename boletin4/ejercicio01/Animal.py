# Definimos la clase
class Animal:

    # Constructor
    def __init__(self, nombre, numPatas):
        self.__nombre = nombre
        self.__numPatas = numPatas

    # Métodos
    def habla(self):
        cadena = ""
        return cadena
    
    def __str__(self):
        cadena = f"Me llamo {self.__nombre}, tengo {self.__numPatas} patas y sueno así: {self.habla()}"
        return cadena