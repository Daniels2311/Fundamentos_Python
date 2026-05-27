python_devs   = {"Ana", "Luis", "Marta", "Carlos", "Sofia"}
java_devs     = {"Luis", "Carlos", "Pedro", "Laura"}

#UNION DE CONJUNTOS
union = {"Ana", "Luis", "Marta", "Carlos", "Sofia", "Pedro", "Laura"}
todos = python_devs | java_devs
union = python_devs.union(java_devs)
print("Unión:", todos) # {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro', 'Laura'}


# INTERSECCIÓN
interseccion = {"Luis", "Carlos"}
ambos = python_devs & java_devs
interseccion = python_devs.intersection(java_devs)
print("Intersección:", ambos)   # {'Luis', 'Carlos'}


# DIFERENCIA

diferencia = {"Ana", "Marta", "Sofia"}
solo_python = python_devs - java_devs
diferencia = python_devs.difference(java_devs)
print("Solo Python: ", solo_python)  # {'Ana', 'Marta', 'Sofia'}
solo_java = java_devs - python_devs
print("Solo Java: ",solo_java ) # {'Pedro', 'Laura'}


# DIFERENCIA SIMETRICA

diferencia_simetrica = {"Ana", "Marta", "Sofia", "Pedro", "Laura"}
exclusivos = python_devs ^ java_devs
diferencia_simetrica = python_devs.symmetric_difference(java_devs)
print("Exclusivos:", exclusivos) # {'Ana', 'Marta', 'Sofia', 'Pedro', 'Laura'}