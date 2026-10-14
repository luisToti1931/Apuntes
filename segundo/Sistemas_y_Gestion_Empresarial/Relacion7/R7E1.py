productos = ["Teclado", "Raton", "Monitor"]
productos.append("Webcam")
productos.remove("Raton")

# el .sort es para ordenar de manera ascendente ( en este caso lo queremos por orden alfabetico)
productos.sort()

lineas = []

for numero, producto in enumerate(productos, start=1):

    lineas.append(f"{numero}. {producto}")


print("\n".join(lineas))
