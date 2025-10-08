# Definimos la clase base
class Empleado:

    # Constructor
    def __init__(self, nombre):
        self.__nombre = nombre
    
    # Get
    def getNombre(self):
        return self.__nombre

    # Set
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    # Métodos
    def __str__(self):
        cadena = f"Empleado {self.__nombre}"
        return cadena