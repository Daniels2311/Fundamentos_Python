# BUCLE WHILE = Instrucción de control que se repite mientras una condición sea verdadera TRUE

i = 0 # Inicialización de la variable de control

while i < 6: # Mientras i sea menor que 6, se ejecutará el bloque de código dentro del bucle
    print("Hola, soy un bucle WHILE")
    if i == 3:
        break # Detiene el bucle si i es igual a 3
    i += 1 # Incremento para evitar un bucle infinito


while i < 6: # Mientras i sea menor que 6, se ejecutará el bloque de código dentro del bucle
    i += 1 # Incremento para evitar un bucle infinito
    if i == 3:
        continue # Saltar el bucle si i es igual a 3
    print(i)
else: # El bloque de código dentro del ELSE se ejecutará cuando la condición del WHILE sea falsa
    print("El bucle WHILE ha terminado")


# Juego de Pokemon

puntos_vida = 100
pokemon = input("Elige tu pokemon: Pikachu, Charmander o Bulbasaur: ")

# Mientras los puntos de vida sean mayores a 0, el juego continúa
while puntos_vida > 0:
    print(f"Tu {pokemon} tiene {puntos_vida} puntos de vida")
    ataque = int(input("Ingresa el daño del ataque: "))
    puntos_vida -= ataque # Resta el daño del ataque a los puntos de vida
print(f"Tu {pokemon} ha sido derrotado")
