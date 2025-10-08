from Operario import Operario
class Oficial(Operario):
    # Constructor
    def __init__(self, nombre):
        super().__init__(nombre)
    # Métodos
    def __str__(self):
        cadena = f"{super().__str__()} --> Oficial"
        return cadena