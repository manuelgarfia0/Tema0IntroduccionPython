# Diccionario para el registro de ventas de una tienda
tienda = {}
opciones = 0
# Función para agregar un producto
def agregar_producto(nombre, total_vendido):
    if total_vendido <= 0:
        print("El total vendido debe ser un número positivo.")
    elif nombre in tienda:
        tienda[nombre] += total_vendido
    else:
        tienda[nombre] = total_vendido

# Función para calcular el total de ventas de un producto
def total_ventas(nombre):
    cont = 0
    if nombre in tienda:
        cont = tienda[nombre]
    return cont

# Menú de opciones
while opciones != 3:
    print("1. Agregar producto")
    print("2. Total de ventas de un producto")
    print("3. Salir")
    opciones = int(input("Elige una opción: "))
    if opciones == 1:
        nombre = str(input("Introduce el nombre del producto: "))
        total_vendido = int(input("Introduce el ventas en el producto: "))
        agregar_producto(nombre, total_vendido)
    elif opciones == 2:
        nombre = str(input("Introduce el nombre del producto a consultar: "))
        if total_ventas(nombre) == 0:
            print("El producto no existe.")
        else:
            print("Se han vendido", total_ventas(nombre), "unidades del producto", nombre)
    elif opciones == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no valida, intentalo de nuevo.")