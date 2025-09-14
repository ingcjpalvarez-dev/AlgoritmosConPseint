# Adivinar un número
# 1.-Generar un número aleatorio entre 1 y 100 (defínanlo).
# 2.-El usuario debe adivinar el número.
# 3.-Pedir un número entero positivo n.
# 4.-Después de cada intento, mostrar si n, es mayor o menor.
# 5.-Repetir hasta que el usuario acierte.


import random

# La computadora genera un número aleatoriamente
numSecreto = random.randint(1, 100)

print("Adivina el número entre el 1 y el 100")

# Inicializamos en bucle en 0
numIntento = 0

while numIntento != numSecreto:                                #inicializamos un bucle que se repite si la variable adivina no es la variable numero generada por la computadora
    numIntento = int(input("Escribe tu intento: "))         #Ingresamos nuestro intento
    
    if numIntento < numSecreto:                                      #Si el numero ingresado en la variable adivina es menor  la variable numero generada por la computadora
        print("Demasiado pequeño, intenta otra vez.")          #Imprime mensaje 
    elif numIntento > numSecreto:                                     #Si es mayor
        print("Demasiado grande, intenta otra vez.")           #Imprime mensaje 

print("¡Lo lograste! ¡Adivinaste el número!")                   #El bucle termina hasta que se adivina el número 

