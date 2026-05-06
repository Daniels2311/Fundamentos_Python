# Ejercicio creativo: Catalgo de compra de videojuegos

print("=" * 50)
print("Catalogo de Videojuegos")
print("=" * 50)

# Se crean las variables para los datos personales

usuario = input("Ingrese su nombre de usuario: ")
print("-" * 50)
contraseña = input("Ingrese su contraseña: ")
print("-" * 50)
edad = int(input("Ingrese su edad: "))
print("-" * 50)

print("Bienvenido al catalogo de videojuegos, ", usuario)
print("-" * 50)

# Se muestra las opciones de compañias de videojuegos disponibles
# Se selecciona la opcion que uno desea

print(
    "A continuación seleccione que compañia de juego desea ver  \n1.Xbox \n2.PlayStation \n3.Nintendo Switch:"
)

Eleccion = input("La compañia que eligio es: ")
print("-" * 50)

if Eleccion == "1":
    print(
        "Has seleccionado Xbox, estos son los juegos disponibles: \n1.Halo Infinite  Master Collection 300.000 $ \n2.Forza Horizon 300.000 $  \n3.Gears 5 300.000 $"
    )
    Opcion = input("El juego que eligio es: ")
    print("-" * 50)
    if Opcion == "1":
        print("Has seleccionado Halo Infinite Master Collection, el precio es de 300.000 $")
        print("-" * 50)
    elif Opcion == "2":
        print("Has seleccionado Forza Horizon, el precio es de 300.000 $")
        print("-" * 50)
    elif Opcion == "3":
        print("Has seleccionado Gears 5, el precio es de 300.000 $")
        print("-" * 50)
    else:
        print("Opcion no valida, por favor ingrese una opcion del 1 al 3")
        print("-" * 50)
    print("Desea comprar este juego? (si/no)")
    compra = input("Su respuesta es: ")
    print("-" * 50)
    if compra == "si":
        if edad < 18:
            print("Lo sentimos, para comprar videojuegos debes ser mayor de edad")
            exit()
        else:
            print("El valor del juego es de 300.000 $")
            print("-" * 50)
            precio = 300000
            valor = int(input("Ingrese el valor con el que va a pagar: "))
            print("-" * 50)
            cambio = valor - precio
            print("Gracias por su compra, disfrute su juego!")
            print("Su cambio es de: ", cambio)   
    elif compra == "no":
        print("Gracias por visitar nuestro catalogo, vuelva pronto!")
    else:
        print("Opcion no valida, por favor ingrese si o no")
elif Eleccion == "2":
    print(
        "Has seleccionado PlayStation, estos son los juegos disponibles: \n1.God of War 200.000 $ \n2.The Last of Us Part II 200.000 $\n3.Horizon Zero Dawn 200.000 $"
    )
    Opcion = input("El juego que eligio es: ")
    print("-" * 50)
    if Opcion == "1":
        print("Has seleccionado God of War, el precio es de 200.000 $")
        print("-" * 50)
    elif Opcion == "2":
        print("Has seleccionado The Last of Us Part II, el precio es de 200.000 $")
        print("-" * 50)
    elif Opcion == "3":
        print("Has seleccionado Horizon Zero Dawn, el precio es de 200.000 $")
        print("-" * 50)
    else:
        print("Opcion no valida, por favor ingrese una opcion del 1 al 3")
    print("Desea comprar este juego? (si/no)")
    compra = input("Su respuesta es: ")
    print("-" * 50)
    if compra == "si":
        if edad < 18:
            print("Lo sentimos, para comprar videojuegos debes ser mayor de edad")
            exit()
        else:
            print("El valor del juego es de 300.000 $")
            print("-" * 50)
            precio = 200000
            valor = int(input("Ingrese el valor con el que va a pagar: "))
            print("-" * 50)
            cambio = valor - precio
            print("Gracias por su compra, disfrute su juego!")
            print("Su cambio es de: ", cambio)
    elif compra == "no":
        print("Gracias por visitar nuestro catalogo, vuelva pronto!")
    else:
        print("Opcion no valida, por favor ingrese si o no")
elif Eleccion == "3":
    print(
        "Has seleccionado Nintendo Switch, estos son los juegos disponibles: \n1.The Legend of Zelda: Breath of the Wild 100.000 $ \n2.Super Mario Odyssey 100.000 $\n3.Animal Crossing: New Horizons 100.000 $"
    )
    Opcion = input("El juego que eligio es: ")
    print("-" * 50)
    if Opcion == "1":
        print(
            "Has seleccionado The Legend of Zelda: Breath of the Wild, el precio es de 100.000 $"
        )
        print("-" * 50)
    elif Opcion == "2":
        print("Has seleccionado Super Mario Odyssey, el precio es de 100.000 $")
        print("-" * 50)
    elif Opcion == "3":
        print(
            "Has seleccionado Animal Crossing: New Horizons, el precio es de 100.000 $"
        )
        print("-" * 50)
    else:
        print("Opcion no valida, por favor ingrese una opcion del 1 al 3")
    print("Desea comprar alguno de estos juegos? (si/no)")
    compra = input("Su respuesta es: ")
    print("-" * 50)
    if compra == "si":
        if edad < 18:
            print("Lo sentimos, para comprar videojuegos debes ser mayor de edad")
            exit()
        else:
            print("El valor del juego es de 300.000 $")
            print("-" * 50)
            precio = 100000
            valor = int(input("Ingrese el valor con el que va a pagar: "))
            print("-" * 50)
            cambio = valor - precio
            print("Gracias por su compra, disfrute su juego!")
            print("Su cambio es de: ", cambio)
    elif compra == "no":
        print("Gracias por visitar nuestro catalogo, vuelva pronto!")
    else:
        print("Opcion no valida, por favor ingrese si o no")
else:
    print("-" * 50)
    print("Opcion no valida, por favor ingrese una opcion del 1 al 3")
    