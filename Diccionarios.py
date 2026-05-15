#Diccionarios

#Creacion de un diccionario

#Estruuctura de un diccionario

diccionario = { 
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}

#Diccionario vacio

diccionario_vacio = {}

#Diccionario con elementos

diccionario_aprendizes = {
    "nombre": "Daniel",
    "apeliido": "Granados",
    "programa": "ADSO",
    "ficha": "3321349",
    "edad": 18
}

print(type(diccionario_aprendizes))

#Acceder a los valores de un diccionario 

print(diccionario_aprendizes["nombre"])
print(diccionario_aprendizes.get["programa"])

#Obtener las claves de un diccionario

print(diccionario_aprendizes.keys())

#Obtener solo los valores de un diccionario
 
print(diccionario_aprendizes.values())

#Obtener la clase y el valor

print(diccionario_aprendizes.items())

#agregar un nuevo elemento a un diccionario

diccionario_aprendizes["correo"] = "dsantiagogranados117@gmail.com"
print(diccionario_aprendizes)

#modificar un elemento de un diccionario
diccionario_aprendizes["edad"] = 19
print(diccionario_aprendizes)

#Metodo UPDATE ()
diccionario_aprendizes.update({"nombre": "Santiago"})
diccionario_aprendizes.update({"telefono": "3216549870"})
print(diccionario_aprendizes)

#comprobar pertenencia 

if "ficha" in diccionario_aprendizes:
    print("La clave 'ficha' existe en el diccionario")

#Recorrer solo los elementos de un diccionario

for clave in diccionario_aprendizes.values():
    print(clave)

#Recorrer solo las claves de un diccionario
for clave in diccionario_aprendizes.keys():
    print(clave)

#Recorrer las claves y los valores de un diccionario

for clave, valor in diccionario_aprendizes.items():
    print(f"Clave: {clave}, Valor: {valor}")

#eliminar un elemento de un diccionario

diccionario_aprendizes.popitem()
print(diccionario_aprendizes)

diccionario_aprendizes.pop("programa")
print(diccionario_aprendizes)

diccionario_aprendizes.clear()
print(diccionario_aprendizes)

#DICIONARIOS ANIDADOS

aprendices = {
    "aprendiz1": {
        "nombre": "Daniel",
        "apellido": "Granados",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 19
    },
    "aprendiz2": {
        "nombre": "Daniela",
        "apellido": "Rodriguez",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 18
    },
    "aprendiz3": {
        "nombre": "Simon",
        "apellido": "Pineda",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 22
        }
}
#Acceder a los valores de un diccionario anidado
print(aprendices["aprendiz1"]["nombre"])
print(aprendices["aprendiz2"]["programa"])
print(aprendices["aprendiz3"]["edad"])  

#Recorrer un diccionario anidado
for aprendiz, datos in aprendices.items():
    print(f"Aprendiz: {aprendiz}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
