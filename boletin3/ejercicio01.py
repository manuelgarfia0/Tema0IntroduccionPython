# Creación de la clase
class CuentaCorriente:
    def __init__(self, dni, saldo, nombre = ""):
        self.__dni = dni
        self.__nombre = nombre
        self.__saldo = saldo

    # Getters
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getSaldo(self):
        return self.__saldo
    
    # Métodos
    def sacarDinero(self, cantidad):
        retirada = False
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            retirada = True
        return retirada
    
    def ingresarDinero(self, cantidad):
        self.__saldo += cantidad

    def __str__(self):
        cadena = f"DNI: {self.__dni}, Nombre: {self.__nombre}, Saldo: {self.__saldo}"
        return cadena

    def __eq__(self, objeto):
        iguales = False
        if self.getDni() == objeto.getDni():
            iguales = True
        return iguales

    def __lt__(self, objeto):
        menor = False
        if self.getSaldo() < objeto.getSaldo():
            menor = True
        return menor