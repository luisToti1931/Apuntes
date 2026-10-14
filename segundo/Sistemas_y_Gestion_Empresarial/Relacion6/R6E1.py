pedidos = int(input("Introduce numero de pedidos: "))

if pedidos < 1: 
    print("Cantidad no válida")
else:
    codigos = []

    for numero in range(1, pedidos + 1):
        codigos.append(f"PED-{numero:03d}")

    print("\n".join(codigos))