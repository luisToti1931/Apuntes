import csv
from pathlib import Path

ruta_csv = Path(__file__).with_name("inventario.csv")


def encontrarProducto(nombre, lista):

    for linea in lista:
        if linea["nombre"].casefold() == nombre.casefold():
            return linea
    return None


def listarProductos(lista):
    if len(lista) >= 1:
        mensaje = ""
        for linea in lista:
            mensaje += f"Producto: {linea['nombre']} | Categoría: {linea['categoria']} | Stock: {linea['stock']}\n"
    else:
        mensaje = "Lista vacía"
    return mensaje


def aniadirProducto(lista, nombre, categoria, stock):
    lista.append({"categoria": categoria, "nombre": nombre, "stock": stock})


def modificarStock(lista, stock_nuevo, nombre):
    producto = encontrarProducto(nombre, lista)
    if producto == None:
        return False
    else:
        producto["stock"] = stock_nuevo
        return True


def guardarCSV(lista):
    with open("ruta_csv", "w", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["categoria", "nombre", "stock"])
        escritor.writeheader()
        escritor.writerows(lista)
    return len(lista)


# MAIN----------------
lista_productos = []
lista_productos.append(
    {"categoria": "Electrodoméstico", "nombre": "Lavadora", "stock": 10}
)
lista_productos.append({"categoria": "Verdura", "nombre": "Lenteja", "stock": 7})
lista_productos.append({"categoria": "Electrónica", "nombre": "Iphone", "stock": 9})

opcion = 0
while opcion != -1:
    print(
        "\nOp-1: Salir\nOp1: listar\nOp2: Añadir\nOp3: Modificar\nOp4: Buscar por nombre\nOp5: Guardar en CSV"
    )
    opcion = int(input(f"Opcion: "))
    if opcion == -1:
        print("Saliendo del programa")
    elif opcion == 1:
        print(listarProductos(lista_productos))
    elif opcion == 2:
        categoria = input(f"Introduce la categoria: ")
        nombre = input(f"Introduce el nombre: ").strip()
        stock = int(input(f"Introduce el stock: "))
        aniadirProducto(lista_productos, nombre, categoria, stock)
        print(f"Producto añadido correctamente")
    elif opcion == 3:
        nombre = input(f"Introduce el nombre: ").strip()
        stock = int(input(f"Modifica el stock: "))
        if modificarStock(lista_productos, stock, nombre):
            print(f"Modificado correctamente")
        else:
            print(f"error, no existe en el inventario ese producto")

    elif opcion == 4:
        nombre = (input(f"Introduce el nombre que buscas: ")).strip()
        resultado = encontrarProducto(nombre, lista_productos)

        if encontrarProducto:
            print(
                f"Encontrado: {resultado['nombre']} | Categoría: {resultado['categoria']} | Stock: {resultado['stock']}"
            )
        else:
            print("No se ha encontrado ningun producto")

    elif opcion == 5:
        if guardarCSV(lista_productos):
            print("Guardado en CSV")
        else:
            print("Ha habido un error")
