# Actividad 2: Análisis de Temperaturas Semanales

#1 punto
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

#2 punto
print(f"La temperatura del dia uno es: {temperaturas[0]} grados")
print(f"La temperatura del ultimo dia es: {temperaturas[-1]} grados")
print(f"La temperatura del dia siete es: {temperaturas[6]} grados")
print(f"La temperatura del penuntimo dia : {temperaturas[-2]} grados")

#3 punto
print(f"Las temperaturas de los primeros 7 dias son: {temperaturas[0:7]} grados")
print(f"Las temperaturas de los ultimos 7 dias son: {temperaturas[7:14]} grados")
print(f"Las temperaturas de los dias pares son: {temperaturas[1::2]} grados")
print(f"Las temperaturas en orden invertido son: {temperaturas[::-1]} grados")

#4 punto

temperaturas_semana1 = temperaturas[0:7]
temperaturas_semana2 = temperaturas[7:14]
promedio_semana1 = sum(temperaturas_semana1) / len(temperaturas_semana1)
promedio_semana2 = sum(temperaturas_semana2) / len(temperaturas_semana2)

print(f"El promedio de temperatura de la semana 1 es: {promedio_semana1} grados")
print(f"El promedio de temperatura de la semana 2 es: {promedio_semana2} grados")


#5 punto

if promedio_semana1 > promedio_semana2:
    print("La semana 1 tuvo un promedio mayor de temperatura que la semana 2.")
elif promedio_semana1 < promedio_semana2:
    print("La semana 2 tuvo un promedio mayor de temperatura que la semana 1.")
else:
    print("Ambas semanas tuvieron el mismo promedio de temperatura.")