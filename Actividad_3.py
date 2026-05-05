#Actividad 3: Clasificador de IMC

print("=" * 50)
print("Clasificador de IMC")
print("=" * 50)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print("-" * 50)

if peso <= 0 or altura <= 0:
    print("Error: El peso y la altura deben ser mayores a cero.")
    exit()
print("-" * 50)

if imc < 18.5:
    print("Tu IMC es: ", round(imc,2))
    print("Clasificación: Bajo peso")
elif imc >= 18.5 and imc < 24.9:
    print("Tu IMC es: ", round(imc,2))
    print("Clasificación: Peso normal")
elif imc >= 25 and imc < 29.9:
    print("Tu IMC es: ", round(imc,2))
    print("Clasificación: Sobrepeso")
else:
    print("Tu IMC es: ", round(imc,2))
    print("Clasificación: Obesidad")
print("-" * 50)
