import math
# Creacion de la clase
class Punto:
    # Constructor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    # Getters
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    # Setters
    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    # Métodos
    def desplaza(self, dX, dY):
        self.__x += dX
        self.__y += dY

    def distancia(self, punto):
        distancia = math.sqrt((punto.getX() - self.__x) ** 2 + (punto.getY() - self.__y) ** 2)
        return distancia

    def __str__(self):
        cadena = f"({self.__x}, {self.__y})"
        return cadena