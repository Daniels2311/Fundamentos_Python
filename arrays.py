# 1. Crear una lista (ordenada, mutable, con duplicados)
invitados = ["Ana", "Betto", "Carla", "Betto"]
print("Lista inicial:", invitados)

# 2. Acceso por índices y Slicing (rangos)
print("El primer invitado es:", invitados[0]) 
print("Los dos primeros son:", invitados[:2]) # No incluye el índice 2

# 3. Medir el largo con len()
print("Cantidad de invitados:", len(invitados))

# 4. Modificar un elemento (Mutabilidad)
invitados[1] = "Bernardo" # Cambiamos a 'Betto' por su nombre real
print("Lista tras corrección:", invitados)

# 5. Agregar elementos (append e insert)
invitados.append("Daniel")            # Al final
invitados.insert(2, "Elena")          # En la posición 2
print("Lista tras agregar:", invitados)

# 6. Eliminar elementos (remove y pop)
invitados.remove("Betto")             # Elimina la primera coincidencia de 'Betto'
eliminado = invitados.pop(0)          # Elimina y guarda a 'Ana' (índice 0)
print("Invitado que no pudo venir:", eliminado)
print("Lista actual:", invitados)

# 7. Comprobar pertenencia (in)
if "Elena" in invitados:
    print("Elena ya está en la lista.")

# 8. Ordenar (sort y reverse)
invitados.sort()                      # Orden alfabético: ['Bernardo', 'Carla', 'Daniel', 'Elena']
print("Lista ordenada:", invitados)

invitados.reverse()                   # Invierte el orden
print("Lista invertida:", invitados)

# 9. Unir listas (+ y extend)
nuevos = ["Fran", "Gaby"]
lista_final = invitados + nuevos      # Crea una nueva
print("Lista final combinada:", lista_final)