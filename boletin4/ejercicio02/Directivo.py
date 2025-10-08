from Empleado import Empleado

# Definimos clases hijas
class Directivo(Empleado):
    # Constructor
    def __init__(self, nombre):
        super().__init__(nombre)
    
    # Métodos
    def __str__(self):
        cadena = f"{super().__str__()} --> Directivo"
        return cadena