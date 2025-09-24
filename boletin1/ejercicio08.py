n = int(input("Introduce la base y altura del triángulo: "))
for fila in range(1, n+1):
	print(" " * (n - fila) + "* " * fila)
