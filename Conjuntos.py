#Conjuntos

#Estructura de un conjunto
conjunto = {}  
print(type(conjunto))  # Esto no es un conjunto, es un diccionario vacío

#creacion

lenguajes = {"Python", "Java", "C++", "JavaScript"} 
print(lenguajes)

conjunto_vacio = set()  # Esto es un conjunto vacío 
conjunto_vacio = {}

#Metodos de modificacion
frutas = {"manzana", "banana", "naranja"}
frutas.add("pera")
frutas.add("manzana") 
frutas.remove("banana")
frutas.discard("uva")
elem = frutas.pop()
print(frutas)

#Verificar pertenecia 

print("manzana" in frutas)
print("banana" in frutas)

python_devs = {"Simon", "Daniel", "Santiago", "Valentina"}
java_devs = {"Andres", "Camilo", "Santiago", "Valentina", "Maria"}

todos = python_devs.union(java_devs)
print("Union: ",todos)

interseccion = python_devs.intersection(java_devs)
print("Interseccion: ", interseccion)

solo_python = python_devs.difference(java_devs)
print("Solo Python: ", solo_python)

solo_java = java_devs.difference(python_devs)
print("Solo Java: ", solo_java)

exclusivos = python_devs.symmetric_difference(java_devs)
print("Exclusivos: ", exclusivos)    