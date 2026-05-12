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

print(aprendices[3]) #imprime un elemento de la lista

aprendices[0] = "Camilo" #modificar un elemento de la lista
print(aprendices)

#consultar rango de elementos de la lista
print(aprendices[0:2]) #imprime desde el indice 0 hasta el indice 1
print(aprendices[:2]) 
print(aprendices[2:4]) 
print(aprendices[2:5]) 
print(aprendices[2:1]) 

#contatenar listas

aprendices_ficha_3321349 = ["Andres", "Daniela", "Sebastian", "Accosta", "Simon"]
aprendices_ficha_3256784 = ["Camilo", "Sofia", "Valentina", "Juan", "Maria"]

aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_3256784
print(aprendices_adso)

#unir listas con extend

aprendices_ficha_3256784.extend(aprendices_ficha_3321349)
print(aprendices_ficha_3256784)

#medir el largo de una lista

longuitud_aprendices_ficha_3321349 = len(aprendices_ficha_3321349)
print(f"La lista de aprendices tiene {longuitud_aprendices_ficha_3321349} elementos")

#contar elementos repetidos de una lista  

count_Andres = aprendices_ficha_3321349.count("Andres")
print(f"El nombre Andres se encuentra {count_Andres} veces en la lista de aprendices")

#obtener el indice de un elemento de la lista

index_Simon = aprendices_ficha_3321349.index("Simon")
print(f"El nombre Simon se encuentra en el indice {index_Simon} de la lista de aprendices")

#copiar la lista

nueva_lista_adso = aprendices_ficha_3321349.copy()
print(nueva_lista_adso)

#agregar un elemento a la lista

nueva_lista_adso.append("Valentina")
nueva_lista_adso.insert(0,"Sharit")
print(nueva_lista_adso)

#eliminar un elemento de la lista

nueva_lista_adso.remove("Sharit")
print(nueva_lista_adso)

nueva_lista_adso.pop(0) 
print(nueva_lista_adso)

#comprobar si un elemento se encuentra en la lista

if "Andres" in nueva_lista_adso:
    print("El nombre Andres se encuentra en la lista de aprendices")
else:    
    print("El nombre Andres no se encuentra en la lista de aprendices")

#ordenar una lista ascendente y descendente

nueva_lista_adso.sort()
print(nueva_lista_adso)

nueva_lista_adso.reverse()
print(nueva_lista_adso)

#limpiar una lista

nueva_lista_adso.clear()
print(nueva_lista_adso)