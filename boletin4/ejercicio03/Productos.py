class Productos:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    def calcular(self, cantidad):
        calculo = self.__precio * cantidad
        return calculo
    
    def __str__(self):
        return f"El producto {self.__nombre} cuesta {self.__precio} €"
    
    def __lt__(self, objeto):
        menor = False
        if self.__precio < objeto.precio:
            menor = True
        return menor