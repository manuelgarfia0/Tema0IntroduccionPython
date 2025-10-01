# Creamos un diccionario para agregar, eliminar y buscar los contactos
agenda = {}
opciones = 0
# Función para agregar un contacto
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado con el teléfono {telefono}.")
# Función para eliminar un contacto
def eliminar_contacto(nombre):
    if nombre in agenda:
        agenda.pop(nombre)
        print("Contacto eliminado.")
    else:
        print("El contacto no existe.")
# Función para buscar un contacto
def buscar_contacto(nombre):
    if nombre in agenda:
        print("Nombre:",nombre, "\nTeléfono:", agenda[nombre])
    else:
        print("El contacto no existe.")
# Menú de opciones
while opciones != 4:
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Salir")
    opciones = int(input("Elige una opción: "))
    if opciones == 1:
        nombre = str(input("Introduce el nombre del contacto: "))
        telefono = str(input("Introduce el teléfono del contacto: "))
        agregar_contacto(nombre, telefono)
    elif opciones == 2:
        nombre = str(input("Introduce el nombre del contacto a eliminar: "))
        eliminar_contacto(nombre)
    elif opciones == 3:
        nombre = str(input("Introduce el nombre del contacto a buscar: "))
        buscar_contacto(nombre)
    elif opciones == 4:
        print("Saliendo del programa...")
    else:
        print("Opción no valida, intentalo de nuevo.")