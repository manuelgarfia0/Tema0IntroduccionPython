# Creacion de clase
class Articulo:
    def __init__(self, nombre, precio, cuantosQuedan):
        self.__nombre = nombre
        self.__precio = precio
        self.__iva = 21
        self.__cuantosQuedan = cuantosQuedan
    
    # Getters
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    def getIva(self):
        return self.__iva
    def getCuantosQuedan(self):
        return self.__cuantosQuedan
    
    # Setters
    def setCuandosQuedan(self, cuantosQuedan):
        self.__cuantosQuedan = cuantosQuedan

    # Métodos
    def getPVP(self):
        PVP = self.__precio * (1 + self.__iva / 100)
        return PVP
    
    def getPVPDescuento(self, descuento):
        PVPDescuento = self.getPVP() - self.getPVP() * descuento
        return PVPDescuento
    
    def vender(self, cantidadVendida):
        actualizado = False
        if cantidadVendida > 0 and cantidadVendida <= self.__cuantosQuedan:
            self.__cuantosQuedan -= cantidadVendida
            actualizado = True
        return actualizado
    
    def almacenar(self, cantidadAlmacenar):
        self.__cuantosQuedan += cantidadAlmacenar

    def __str__(self):
        cadena = f"Nombre: {self.__nombre}, Precio: {self.__precio}, IVA: {self.__iva}, Stock: {self.__cuantosQuedan}"
        return cadena

    def __eq__(self, objeto):
        iguales = False
        if self.getNombre() == objeto.getNombre():
            iguales = True
        return iguales

    def __lt__(self, objeto):
        menor = False
        if self.getNombre() < objeto.getNombre():
            menor = True
        return menor