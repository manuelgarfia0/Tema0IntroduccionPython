from Productos import Productos

class NoPerecedero(Productos):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.__tipo = tipo
    
    def calcular(self, cantidad):
        return super().calcular(cantidad)
    
