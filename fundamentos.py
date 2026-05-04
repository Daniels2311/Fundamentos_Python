print("Hello Everybody")

#Tipos de escritura de variables

camelCase = "SENA"
aprendizSena = "SENA"

PascalCase = "SENA"
AprendizSena= "SENA"

snake_case = "SENA"
aprendiz_sena = "SENA"

_aprendiz = "SENA"

# Variables

nombre = "Daniel"
apeliido = "Granados"
edad = 18
altura = 1.76
activo = True
correo = "dsantiagogranados117@gmail.com"
telefono = "3209359011"
cedula = "1013117908"

# Castear Variables

telefono_int = int(telefono)
edad_float = float(edad)
altura_int = int(altura)
cedula_str = str(cedula)
  

print(type(nombre), nombre)
print(type(apeliido), apeliido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print(type(cedula), cedula)
print(type(telefono_int), telefono_int)
print(type(edad_float), edad_float)
print(type(altura_int), altura_int)
print(type(cedula_str), cedula_str)

#identacion en Python

if 5 < 2:
    print("5 es mayor que 2")
else:
    print("5 es menor que 2")

#input

nombre_completo = input("Ingrese su nombre: ")
print("Hola " + nombre_completo)
  
edad_aprendiz = int (input("Ingrese su edad: "))
print("Tu edad es: " , edad_aprendiz)

print(type(edad_aprendiz), edad)

#Imprimir con formato f-string

print(f"Tu nombre es {nombre_completo} y tu edad es {edad_aprendiz}")
