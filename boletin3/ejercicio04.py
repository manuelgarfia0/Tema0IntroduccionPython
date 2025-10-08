# Creacion de clase
class Articulo:

    IVA = 21

    def __init__(self, nombre, precio, cuantosQuedan):
        self.__nombre = nombre
        self.__precio = precio
        self.__cuantosQuedan = cuantosQuedan
    
    # Getters
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    def getCuantosQuedan(self):
        return self.__cuantosQuedan
    
    # Setters
    def setCuandosQuedan(self, cuantosQuedan):
        self.__cuantosQuedan = cuantosQuedan

    # Métodos
    def getPVP(self):
        PVP = self.__precio * (1 + Articulo.IVA / 100)
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
        cadena = f"Nombre: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__cuantosQuedan}"
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