#Operadores logicos

#AND

import re


print(True and True) #Si ambos son verdaderos = true
print(True and False) #Si uno es falso = false
print(False and True) #Si uno es falso = false
print(False and False) #Si ambos son falsos = false

#OR
print(True or True) #Si ambos son verdaderos = true
print(True or False) #Si uno es verdadero = true
print(False or True) #Si uno es verdadero = true
print(False or False) #Si ambos son falsos = false

#NOT
print(not True) #Si es verdadero = false
print(not False) #Si es falso = true

#Ejercicio 

resultado = (5 > 3 and 2 < 4) #true and true = true
print({resultado})