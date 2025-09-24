numero = int(input("Introduce un número entero positivo: "))
while numero <= 0:
	numero = int(input("Por favor, introduce un número entero positivo: "))

if numero == 1:
	print("1 no es primo.")
else:
	es_primo = True
	i = 2
	while i < numero and es_primo:
		if numero % i == 0:
			es_primo = False
		i += 1
	if es_primo:
		print(numero,"es primo.")
	else:
		print(numero,"no es primo.")
