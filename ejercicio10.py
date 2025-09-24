num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

def mayor(a, b):
    if a > b:
        return a
    else:
        return b
    
print("El número mayor es:", mayor(num1, num2))