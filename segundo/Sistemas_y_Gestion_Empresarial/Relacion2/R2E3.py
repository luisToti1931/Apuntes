nombre = input("Introduce un nombre: ")
precio = float(input("Introduce su precio: "))
cantidad = int(input("Introduce la cantidad: "))
porcentaje = float(input("Introduce el porcentaje: "))
subtotal = precio * cantidad
descuento_total = subtotal * porcentaje
precio_con_descuento = subtotal - descuento_total

print(f"Con precio {precio}, cantidad {cantidad} y descuento {porcentaje}, el total es {precio_con_descuento} EUR")