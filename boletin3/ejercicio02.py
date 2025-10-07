# Creacion de la clase
class Libro:
    # Constructor
    def __init__(self, titulo, autor, ejemplares, ejemplaresPrestados):
        self.__titulo = titulo
        self.__autor = autor
        self.__ejemplares = ejemplares
        self.__ejemplaresPrestados = ejemplaresPrestados
    
    # Getters
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getEjemplares(self):
        return self.__ejemplares
    def getEjemplaresPrestados(self):
        return self.__ejemplaresPrestados
    
    # Setters
    def setEjemplares(self, ejemplares):
        self.__ejemplares = ejemplares
    def setEjemplaresPrestados(self, ejemplaresPrestados):
        self.__ejemplaresPrestados = ejemplaresPrestados

    # Métodos
    def prestamo(self):
        prestado = False
        if self.__ejemplares - self.__ejemplaresPrestados > 0:
            self.__ejemplaresPrestados += 1
            prestado = True
        return prestado
    
    def devolucion(self):
        devuelto = False
        if self.__ejemplaresPrestados > 0:
            self.__ejemplaresPrestados -= 1
            devuelto = True
        return devuelto

    def __str__(self):
        cadena = f"Libro: {self.__titulo}, autor: {self.__autor}, "
        return cadena

    def __eq__(self, objeto):
        iguales = False
        if self.getTitulo() == objeto.getTitulo() and self.getAutor() == objeto.getAutor():
            iguales = True
        return iguales
    
    def __lt__(self, objeto):
        menor = False
        if self.getAutor() < objeto.getAutor():
            menor = True
        return menor