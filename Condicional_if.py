#Condiconales if/ else / elif

if False:
    print("La condicion es veradadera")
elif False:
    print("La condicion es falsa")
elif True:  
    print("La condicion es veradadera")
else:    
    print("La condicion es falsa")

#Ejercicio:Clasificacion de edad

edad = int(input("Ingrese su edad: "))

if edad <18:
    print("Eres un menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres un adulto")
else:    
    print("Eres un adulto mayor")

#Ejercicio: CLasificaion de edad con if anidado

edad = int(input("Ingrese su edad: "))

if edad < 18:    
    if edad > 12 and edad < 18:
        print("Eres un adolescente")
    else:
        print("Eres un niño")
else:
    if edad >=18 and edad < 60:
        print("Eres un adulto")
    else:
        print("Eres un adulto mayor")

#operador ternario 

numero = 4

if numero % 2 == 0:
    print("El numero es par")
else:    
    print("El numero es impar")

print("El numero es par" if numero % 2 == 0 else "El numero es impar")