numRange = int(input("Ingresa un número entero positivo: "))   #Pedimos al usuario un número entero positivo
if numRange < 1 :
    print("El número ingresado es negativo, por favor ingrese un número positivo") #Arrancamos desde 1

i = 1                  #Empezamos desde 1
while i <= numRange:     #Recorremos todos los números hasta n
    if i % 2 != 0:         #Verificamos si el número es par o impar
        print(i)            #Imprimimos si la division de i entre 2 es diferente por lo tanto de ser asi imprimimos el n° imprar
    i = i + 1