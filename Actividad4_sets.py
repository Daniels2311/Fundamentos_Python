# Actividad : Análisis de Matrículas del Centro de Formación
# Primer punto
python_curso = {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro'}
java_curso = {'Luis', 'Carlos', 'Pedro', 'Laura', 'Diego'}
bd_curso = {'Marta', 'Sofia', 'Laura', 'Ana', 'Miguel'}

print("--- RESULTADOS DE LA ACTIVIDAD DE CONJUNTOS ---")

# Segundo punto

# Unión triple
todos_los_aprendices = python_curso.union(java_curso).union(bd_curso)
print(f"\nAprendices únicos totales: {len(todos_los_aprendices)}")
print(todos_los_aprendices)

# Aprendices en Python y Java a la vez
python_y_java = python_curso.intersection(java_curso)
print(f"\nAprendices en Python y Java a la vez: {len(python_y_java)}")

# Aprendices que solo cursan Python
solo_python = python_curso.difference(java_curso).difference(bd_curso)
print(f"\nAprendices que solo cursan Python: {len(solo_python)}")

# Aprendices que cursan exactamente dos programas
en_exactamente_dos = (
    (python_curso & java_curso) | 
    (java_curso & bd_curso) | 
    (python_curso & bd_curso)
) - (python_curso & java_curso & bd_curso)

print(f"\nAprendices matriculados en exactamente dos programas: {len(en_exactamente_dos)}")

# Tercer punto
inscripciones = ['Ana', 'Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana']
conjunto_unicos = set(inscripciones)

print(f"\nCantidad de inscritos únicos: {len(conjunto_unicos)}")
print(f"Quiénes son: {conjunto_unicos}")


# Cuarto punto
conteo_programas = {}

for aprendiz in conjunto_unicos :
    cantidad = inscripciones.count(aprendiz)
    conteo_programas[aprendiz] = cantidad

print("\nCantidad de inscripciones por aprendiz:", conteo_programas)


# Quinto punto
en_los_tres = python_curso.intersection(java_curso).intersection(bd_curso)
print("\nMatriculados en los tres programas a la vez:")
if en_los_tres:
    print(en_los_tres)
else:
    print("Ningún aprendiz está en los tres cursos al tiempo.")