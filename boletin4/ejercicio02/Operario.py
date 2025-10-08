from Empleado import Empleado

class Operario(Empleado):
    # Constructor
    def __init__(self, nombre):
        super().__init__(nombre)
    
    # Métodos
    def __str__(self):
        cadena = f"{super().__str__()} --> Operario"
        return cadena