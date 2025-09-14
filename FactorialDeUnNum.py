n = int(input("Escribe un número entero positivo: "))

factorial = 1   # acumulador

for i in range(1, n + 1):  # desde 1 hasta n (incluido n)
    factorial = factorial * i

print("El factorial de", n, "es:", factorial)
