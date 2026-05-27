# SENTENCIA MATCH (PYTHON 3.10+) => SWITCH

dia = int(input("Ingrese el número del dia: "))

# SENTENCIA MATCH

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Dia incorrecto")