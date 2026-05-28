#open (nombre archivo, nombre de modo) funcion de python para manipular archivos

# R  (Read) Lectura
# W  (Write) Escritura
# X  (Crear archivo nuevo)
# A  (Add) escribri nuevo texto

#Leer un archivo del sistema
try:
    file = open("archivo.txt", "r") # Abre el archivo
    print(file.readline()) # Lee la primera linea del archivo
    file.close() # Cierra el archivo
except FileNotFoundError:
    print("Archivo no encontrado")

#Uso de with para no cerrar el archivo manualmente
try: 
    with open("archivo.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("Archivo no encontrado")

#sobreescrcribir un archivo del sistema
try:
    with open("archivo.txt", "w") as file:
        file.write("Texto sobreescrito")
    with open("archivo.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("Archivo no encontrado")

#Escribir un texto nuevo en un archivo del sistema
try:
    with open("archivo.txt", "a") as file:
        file.write("Texto nuevo")
    with open("archivo.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Archivo no encontrado")

#creacion de un archivo en el sisitema

try:
    with open("archivo_2.txt", "x") as file:
        file.write("Texto nuevo")
except FileNotFoundError:
    open("archivo_2.txt", "x")
    print("Archivo no encontrado")
