# MANEJO DE ERRORES

#estructura:

try:
    print("Hola mundo")
except:
    print("Algo salio mal")
finally:
    print("Finalmente")

#Ejemplo: convertir o castear dato de la entrada del usuario

try:
    edad_usuario = int(input("Ingresa tu edad: "))
except ValueError:
    print("Error: ingresa solo valores numéricos")
    
#ejemplo: variable no definida

# try:
#     print(x)
# except NameError:
#     print("Error: la variable no s sido definida")
    

#Ejemplo: division por cero

try:
    numero = 10/0
except ZeroDivisionError:
    print("Error:No se puede dividir por cero")


