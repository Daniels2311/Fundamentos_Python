#Ejercicio Calculadora

print("Calculadora de Python")
print("Por favor ingrese dos numeros para realizar las operaciones aritmeticas")

Valor1= float (input("Ingrese un numero: "))
print(Valor1)
  
Valor2 = float (input("Ingrese otro numero: "))
print(Valor2)

print("Ingrese la operacion que desea realizar: \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division: ")

Eleccion = input("La operacion que eligio es: ")

if Eleccion == "1":
    resultado = Valor1 + Valor2
    print("El resultado de la suma es: ", resultado)
elif Eleccion == "2":
    resultado = Valor1 - Valor2
    print("El resultado de la resta es: ", resultado)
elif Eleccion == "3":
    resultado = Valor1 * Valor2
    print("El resultado de la multiplicacion es: ", resultado)
elif Eleccion == "4":
    resultado = Valor1 / Valor2
    print("El resultado de la division es: ", resultado)
else:
    print("Opcion no valida, por favor ingrese una opcion del 1 al 4")
