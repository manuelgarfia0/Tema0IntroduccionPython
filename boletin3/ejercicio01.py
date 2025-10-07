# Creación de la clase
class CuentaCorriente:
    def __init__(self, dni, saldo, nombre = ""):
        self.__dni = dni
        self.__nombre = nombre
        self.__saldo = saldo

    # Getters
    def get_dni(self):
        return self.__dni
    
    def get_nombre(self):
        return self.__nombre
    
    def get_saldo(self):
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
        cadena = "DNI:", self.__dni, "Nombre:", self.__nombre, "Saldo:", self.__saldo
        return cadena

    def __eq__(self, objeto):
        iguales = False
        if self.get_dni() == objeto.dni:
            iguales = True
        return iguales

    def __lt__(self, objeto):
        menor = False
        if self.get_saldo() < objeto.saldo:
            menor = True
        return menor