from Productos import Productos

class Perecedero(Productos):
    def __init__(self, nombre, precio, diasCaducar):
        super().__init__(nombre, precio)
        self.__diasCaducar = diasCaducar
    
    def calcular(self, cantidad):
        if self.__diasCaducar == 1:
            calculo = super().calcular(cantidad/4)
        elif self.__diasCaducar == 2:
            calculo = super().calcular(cantidad/3)
        elif self.__diasCaducar == 3:
            calculo = super().calcular(cantidad/2)
        return calculo