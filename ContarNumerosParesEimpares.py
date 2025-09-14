# Contar números pares e impares
#Pedir al usuario varios números, ver Arreglos PSeint  para guardarlos en un arreglo, PISTA usando un PARA.
#miLista[i] = Leer número
#Una vez que tengamos el arreglo, hay que recorrer todos los elementos e identificar cuántos son pares y cuántos son impares. 
#Ejemplo: [4, 8, 12, 11, 9, 6, 10, 3] salida -> 5 números pares y 3 número impares

# Paso 1: Crear lista y pedir cantidad de números
miLista = []
cantidad = int(input("¿Cuántos números vas a ingresar? "))

# Paso 2: Llenar la lista
for i in range(cantidad):
    numero = int(input(f"Escribe el número {i+1}: "))
    miLista.append(numero)

# Paso 3: Contar pares e impares
pares = 0
impares = 0

for numero in miLista:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Paso 4: Mostrar resultado
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
