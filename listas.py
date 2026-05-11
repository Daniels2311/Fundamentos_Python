# Listas 

#Estructura de una lista

#indice : 0

listas = ["objeto_1","objeto_2","objeto_3"]
print(type (listas))

#lista de aprendices SENA ADSO
#Crear una lista vacia 

aprendices = ["Simon","Daniel","Daniela", "Accosta", "Sebastian"]
print(aprendices)

listas_mixtas = ["Andres", 25, True, 3.14]
print(listas_mixtas)

#consultar rango de elementos de la lista
print(aprendices[0:2]) #imprime desde el indice 0 hasta el indice 1
print(aprendices[:2]) #imprime desde el indice 0 hasta el indice 2
print(aprendices[2:4]) #imprime desde el indice 2 hasta el final de la lista
print(aprendices[2:5]) #imprime desde el indice 2 hasta el final de la lista
print(aprendices[2:1]) #imprime desde el indice 2 hasta el final de la lista

#contatenar listas

aprendices_ficha_3321349 = ["Andres", "Daniela", "Sebastian", "Accosta", "Simon"]
aprendices_ficha_3256784 = ["Camilo", "Sofia", "Valentina", "Juan", "Maria"]

aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_3256784
print(aprendices_adso)





