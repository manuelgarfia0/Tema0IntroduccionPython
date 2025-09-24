# Pedimos que el usuario introduzca un número entero positivo
numero = int(input("Introduce un número entero positivo: "))
# Mientras el número no sea positivo, seguimos pidiendo un número
while numero <= 0:
	numero = int(input("Por favor, introduce un número entero positivo: "))
# Si el número es 1, no es primo
if numero == 1:
	print("1 no es primo.")

else:
	es_primo = True
	i = 2
	#  Mientras i sea menor que el número y es_primo sea True, seguimos comprobando
	while i < numero and es_primo:
		# Si el número es divisible por i, no es primo
		if numero % i == 0:
			es_primo = False
		# Incrementamos i en 1 para comprobar el siguiente número
		i += 1
	# Si es_primo sigue siendo True, el número es primo
	if es_primo:
		print(numero,"es primo.")
	# Si es_primo es False, el número no es primo
	else:
		print(numero,"no es primo.")
