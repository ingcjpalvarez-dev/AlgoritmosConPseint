#Definir si son números amigos
#Pedir dos números enteros a y b.
#Pedir el divisor.
#Definir si son amigos, siempre y cuando el residuo de ambos sea igual.
#Ejemplo: si a = 8 y b = 6 y el divisor = 2, entonces son números amigos.
#Ejemplo: si a = 8 y b = 9  y el divisor = 3, entonces no son números amigos.

# Pedir los números
a = int(input("Escribe el primer número: "))
b = int(input("Escribe el segundo número: "))
divisor = int(input("Escribe el divisor: "))

# Calcular residuos
residuo_a = a % divisor
residuo_b = b % divisor

# Comparar y mostrar resultado
if residuo_a == residuo_b:
    print("¡Son números amigos!")
else:
    print("No son números amigos.")
