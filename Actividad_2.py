# Actividad 2: Calculadora de Notas
print("=" * 50)
print("Calculadora de Notas")
print("=" * 50)
print("Por favor ingrese las tres notas del estudiante para calcular el promedio y determinar su estado")
print("-" * 50)

Nota_1 = float(input("Ingrese la primera nota: "))
Nota_2 = float(input("Ingrese la segunda nota: "))
Nota_3 = float(input("Ingrese la tercera nota: "))

if Nota_1 > 5.0 or Nota_2 > 5.0 or Nota_3 > 5.0:
    print("Error: Las notas tienen que ser menores a 5")
    if Nota_1 < 0 or Nota_2 < 0 or Nota_3 < 0:
        print("Error: Las notas no pueden ser negativas")
else:
    Promedio = (Nota_1 + Nota_2 + Nota_3) / 3
    nota_faltante = 3 - Promedio

    print("-" * 50)
    print("Primera nota:", Nota_1)
    print("Segunda nota:", Nota_2)
    print("Tercera nota:", Nota_3)
    print("El promedio del aprendiz es: ", round(Promedio,2))
    print("-" * 50)


    if Promedio <= 2.9:
        print("El aprendiz no aprobo sacando un promedio de: ", round(Promedio,2))
        print("Para aprobar necesita una nota de: ", round(nota_faltante,2))
        print("Nivel de desempeño: Bajo")
    elif Promedio >=3.0 and Promedio < 4.9:
        print("El aprendiz aprobo con un promedio de: ", round(Promedio,2))
        print("Nivel de desempeño: Alto")
    else:
        print("El aprendiz aprobo: ", round(Promedio,2))
        print("Nivel de desempeño: Superior")
print("-" * 50)