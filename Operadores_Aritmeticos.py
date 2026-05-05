#Operadores aritmeticos
import math
import random
a = 10

b = 5

#Suma
suma = a + b
print(f"Suma: {suma}")

#Resta
resta = a - b
print(f"Resta: {resta}")

#Multiplicacion
multiplicacion = a * b
print(f"Multiplicacion: {multiplicacion}")

#Division
division = a / b
print(f"Division: {division}")

#Division entera
division_entera = a // b
print(f"Division entera: {division_entera}")

#Modulo
modulo = a % b
print(f"Modulo: {modulo}")

#Potencia
potencia = a ** b
print(f"Potencia: {potencia}")

#precencia de operadores 

resultado = a + b * 2
print(f"El resultado de la operacion es: {resultado}")

resultado_2 = (a + b) * 2
print(f"El resultado de la operacion con parentesis es: {resultado_2}")

resultado_3 = a * b // 3
print(f"El resultado de la operacion con potencia es: {resultado_3}")

resultado_4 = (a * b) // 3
print(f"El resultado de la operacion con potencia y parentesis es: {resultado_4}")

resultado_5 = a *( b // 3 )   
print(f"El resultado de la operacion con potencia y parentesis es: {resultado_5}")

resultado_6 = (a + 7) * ((b - 12) % 4) // 5 
print(f"El resultado de la operacion es: {resultado_6}")

#Librerias de matematicas


print(f"El valor de pi es: {math.pi}")
print(f"El valor de e es: {math.e}")
print(f"El valor de la raiz cuadrada de 16 es: {math.sqrt(16)}")

#libreria de random

random.random() #genera un numero aleatorio entre 0 y 1
numero_aleatorio = random.randint(1, 10) #genera un numero aleatorio entre 1 y 10
print(random.random())
print({numero_aleatorio}) 