# BUCLE FOR = Instrucción de control que se repite un número determinado de veces

lenguaje = "Python"

for letra in lenguaje:
    print(letra)


# Recorrer una lista con un bucle FOR
frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    if fruta == "banana":
        #break  # Detiene el bucle si encuentra "banana"
        continue  # Salta a la siguiente iteración si encuentra "banana"
    print(fruta)
else:
    print("Se han recorrido todas las frutas")


# Recorrer un rango de números con un bucle FOR
for i in range(5):
    print(i)

for i in range(1,6):
    pass # No hace nada, se utiliza para indicar que el bloque de código está vacío


# Recorrer una tupla con un bucle for
colores = ("rojo", "verde", "azul")

for color in colores:
    print(color)


# Recorrer un diccionario con un bucle for
diccionario_aprendices = {"nombre": "Felipe", "edad": 32, "ciudad":"Duitama"}

for clave, valor in diccionario_aprendices.items():
    print(f"{clave}: {valor}")


