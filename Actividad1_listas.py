#Actividad 1: Inventario de la Tienda Escolar

#1 punto
productos = ["Cuadernos", "Lápices", "Borradores", "Colores", "Reglas", "Tijeras"]

#2 punto
precios = [5500, 2500, 1000, 7000, 3500, 4000]

#3 punto
cantidades = [47, 30, 45, 80, 100, 60]

#4 punto
cantidad_productos = len(productos) 

print ("inventario tienda escolar:" 
       "\nProductos: ", productos, 
       "\nPrecios: ", precios, 
       "\nCantidades: ", cantidades, 
       "\nCantidad de productos: ", cantidad_productos)

print(f"El producto : {productos[0]}, tiene un precio de: {precios[0]}, y una cantidad de: {cantidades[0]}")
print(f"El producto : {productos[1]}, tiene un precio de: {precios[1]}, y una cantidad de: {cantidades[1]}")
print(f"El producto : {productos[2]}, tiene un precio de: {precios[2]}, y una cantidad de: {cantidades[2]}")
print(f"El producto : {productos[3]}, tiene un precio de: {precios[3]}, y una cantidad de: {cantidades[3]}")
print(f"El producto : {productos[4]}, tiene un precio de: {precios[4]}, y una cantidad de: {cantidades[4]}")
print(f"El producto : {productos[5]}, tiene un precio de: {precios[5]}, y una cantidad de: {cantidades[5]}")

#5 punto
print(type(productos))
print(type(productos[0]))