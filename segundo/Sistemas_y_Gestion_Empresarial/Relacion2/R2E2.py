nombre = input("Introduce un nombre: ")
servicio = input("Introduce un servicio: ")
precio_unitario = float(input("Introduce un precio unitario: "))
cantidad = int(input("Introduce una cantidad: "))

subtotal = precio_unitario * cantidad

print(f"Con precio {precio_unitario} y cantidad {cantidad}, el subtotal es {subtotal} EUR")