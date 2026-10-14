productos = [
    {"nombre": "Teclado", "categoria": "Periféricos", "precio": 25.50, "stock": 4},
    {"nombre": "Ratón", "categoria": "Periféricos", "precio": 15.00, "stock": 0},
    {"nombre": "Monitor", "categoria": "Pantallas", "precio": 180.00, "stock": 3},
    {"nombre": "Webcam", "categoria": "Periféricos", "precio": 45.00, "stock": 2}
]

disponibles = 0
lineas = []

for producto in productos:
    if producto["stock"] <= 0:
        print(f"Stock insuficiente para {producto['nombre']}")
else:
    lineas.append(producto["nombre"])
    disponibles += 1

lineas.append(f"Disponibles: {disponibles}")

print("\n".join(lineas))