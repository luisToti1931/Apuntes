import csv
from pathlib import Path

ruta = Path(__file__).with_name("productos.csv")

productos = [
    {"nombre": "Teclado", "precio": 25.50, "stock": 8},
    {"nombre": "Ratón", "precio": 12.75, "stock": 15},
    {"nombre": "Monitor", "precio": 149.99, "stock": 4},
]

with open (ruta, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "stock"])
    escritor.writeheader()
    escritor.writerows(productos)

with open(ruta, "r", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        print(f"{fila['nombre']}: {fila['precio']} EUR, stock {fila['stock']}")