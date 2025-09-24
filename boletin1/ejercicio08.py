# Pedimos al usuario la base y altura del triángulo
n = int(input("Introduce la base y altura del triángulo: "))
# Con un bucle for, imprimimos cada fila del triángulo
for fila in range(1, n+1):
	# Imprimimos los espacios y los asteriscos correspondientes a la fila actual
	print(" " * (n - fila) + "* " * fila)
