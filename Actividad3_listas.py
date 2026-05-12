#Actividad 3: Gestión de Lista de Reproducción Musical

#1 punto
canciones = ["Freaks", "Me rehuso", "Dig it", "Hakurai ", "Sabor Caramelo"]   

#2 punto
canciones.append("yoko")
print(canciones)

canciones.insert(2,"Master of Puppets")
print(canciones)

nueva_lista = ["Bonus Track 1", "Bonus Track 2"]
nueva_lista.extend(canciones)
print(nueva_lista)

#3 punto

nueva_lista.remove("Freaks")
print(nueva_lista)

nueva_lista.pop(-1) 
print(nueva_lista)

#4 punto
nueva_lista.sort()
print(nueva_lista)

#5 punto

print(f"El numero de canciones es: {len(nueva_lista)}")

print(f"La primera cancion que agregue se encuentra en el indice: {nueva_lista.index("Dig it")}")

print(f"El string que agregamos aparece: {nueva_lista.count("Bonus Track 1")} veces en la lista")

