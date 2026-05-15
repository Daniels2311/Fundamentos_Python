#TUPLAS

#Estructura de una tupla
#indice  0           1           2

tupla = ("elemento1", "elemento2", "elemento3")
print(type(tupla))

tupla2 = "a", "b","c"
print(type(tupla2))

tupla3 = ("Hola",)
print(type(tupla3))

tupla4 = tuple("Hola",)
print(tupla4)

tuplas_mixtas = ("Hola", 1, 3.14, [1,2,3], (4,5,6))
print(tuplas_mixtas)

#tupla aprendices adso

aprendices = ("Andres", "Camilo", "Santiago", "Valentina")
print(aprendices)

#acceder a un elemento de la tupla
print(aprendices[0])

#modfiicar un elemento de la tupla
#aprendices[0] = "Maria" #Esto no se puede hacer porque las tuplas son inmutables

#consultar rangos de elementos de la tupla
print(aprendices[0:2]) 
print(aprendices[1:4])
print(aprendices[1:])

#sumar tuplas

tupla5 = (1,2,3)
tupla6 = (4,5,6)
tupla_suma = tupla5 + tupla6
print(tupla_suma)

#multiplicar tuplas
tupla_multiplicada = tupla5 * 3
print(tupla_multiplicada)

#metodos de las tuplas

#medir el rango de una tupla

print(len(aprendices))

#contar cuantas veces aparece un elemento en la tupla
print(aprendices.count("Andres"))

#encontrar el indice de un elemento en la tupla
print(aprendices.index("Santiago"))

#modificar una tupla a lista

print(type(aprendices))
lista_aprendices = list(aprendices)
print(type(lista_aprendices))

#agregar un elemento a la lista de aprendices
lista_aprendices.append("Maria")
print(lista_aprendices)

#volver a convertir la lista de aprendices a tupla 
aprendices = tuple(lista_aprendices)
print(aprendices)

#comprobar si un elemento esta en la tupla

print("Maria" in aprendices)
print("Daniel" in aprendices)

#empaquetar tuplas

programa1 = "ADSO"
programa2 = "SST"
programa3 = "Tipografia"

tupla_programas = (programa1, programa2, programa3)
print(tupla_programas)

#desempaquetar tuplas

tupla_desempaquetada = ("ADSO", "SST", "Tipografia")
programa1, programa2, programa3 = tupla_desempaquetada
print(programa1)

#ejercicio 2 desempaqietar tupla

Tupla_ciudades = ("Bogota", "Medellin", "Cali")   

Ciudad1, *Ciudad2= Tupla_ciudades
print(Ciudad1)
print(Ciudad2)  

for ciudad in Tupla_ciudades:
    print(ciudad)


