#Actividad : Sistema de Registro de Aprendices
# Primer punto
grupo = {
    3321349: {
        "nombre": "Daniel",
        "edad": 19,
        "notas": [4.0, 3.5, 4.2, 4.8],
        "ciudad": "Duitama"
    },

    3213508: {
        "nombre": "Sofia",
        "edad": 21,
        "notas": [2.5, 3.0, 2.8, 3.2],
        "ciudad": "Bogota"
    },

    3113511: {
        "nombre": "Daniela",
        "edad": 18,
        "notas": [4.5, 4.7, 4.3, 4.9],
        "ciudad": "Sogamoso"
    },

    3313524: {
        "nombre": "Miguel",
        "edad": 23,
        "notas": [3.0, 3.2, 3.1, 2.9],
        "ciudad": "Tunja"
    }
}

# Segundo punto
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Tercer punto
print("Reporte de aprendices\n")

for ficha, datos in grupo.items():

    promedio = calcular_promedio(datos["notas"])

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Ciudad: {datos['ciudad']}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")
    print("----------------------")

# Cuarto punto
grupo[321353] = {
    "nombre": "Samuel",
    "edad": 18,
    "notas": [4.1, 3.9, 4.0, 4.3],
    "ciudad": "Sogamoso"
}

# Actualizar ciudad
grupo[3321349]["ciudad"] = "Nueva Ciudad"

# Quinto punto
print("\nAprendices ordenados por promedio\n")

aprendices_ordenados = sorted(
    grupo.items(),
    key=lambda x: calcular_promedio(x[1]["notas"]),
    reverse=True
)

for ficha, datos in aprendices_ordenados:
    promedio = calcular_promedio(datos["notas"])

    print(f"{datos['nombre']} - Promedio: {promedio:.2f}")