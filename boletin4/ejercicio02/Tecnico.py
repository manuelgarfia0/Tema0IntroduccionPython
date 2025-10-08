from Operario import Operario

class Tecnico(Operario):
    # Constructor
    def __init__(self, nombre):
        super().__init__(nombre)
    # Métodos
    def __str__(self):
        return f"{super().__str__()} --> Tecnico"