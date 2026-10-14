productos = int(input("Número de productos: "))
meses = int(input("Número de meses: "))

lineas = []

for producto in range(1, productos + 1):
    for mes in range(1, meses + 1):
        lineas.append(f"Producto {producto} - Mes {mes}")

print("\n".join(lineas))
