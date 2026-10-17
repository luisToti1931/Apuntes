from tokenize import Double

from modelos import Producto, Pedido, LineaPedido


def listarProductos(lista):
    mensaje = ""
    if len(lista) >= 1:
        for linea in lista:
            mensaje += f"Producto: {linea.nombre} | Precio: {linea.precio} | Stock: {linea.stock}\n"
    else:
        mensaje = "No se han listado correctamente"
    return mensaje


def aniadir_lineas_pedido(pedido, producto):
    return pedido.agregar_linea(producto)


def mostrar_detalles(pedido):
    mensaje = ""
    if not pedido.lineas:
        return f"El pedido de {pedido.cliente} esta vacio"
    for i, linea in enumerate(pedido.lineas, 1):
        mensaje += (
            f"{i}. Producto: {linea.producto.nombre} "
            f"| Cantidad: {linea.cantidad} "
            f"| Precio Un: {linea.precio:.2f}€ "
            f"| Subtotal: {linea.subtotal():.2f}€\n"
        )
    return mensaje


def main():
    lista_productos = []
    lista_productos.append(Producto("Teclado", 25.50, 8))
    lista_productos.append(Producto("Ratón", 12.75, 5))
    lista_productos.append(Producto("Monitor", 149.99, 2))

    cliente = input("Introduzca nombre del cliente: ").strip()
    pedido = Pedido(cliente)
    opcion = 0

    while opcion != -1:

        print(
            "Op-1: Salir\nOp1: Ver productos y stock\nOp2: Añadir linea al pedido\nOp3: Listar detalle del pedido\nOp4: Calcular total"
        )
        opcion = int(input("Introduce la opcion: "))
        if opcion == 1:
            print(listarProductos(lista_productos))
        elif opcion == 2:
            print(f"\n{listarProductos(lista_productos)}")
            nombre_buscar = input("Introduce nombre del producto que buscas: ")

            producto_encontrado = None

            for producto in lista_productos:
                if producto.nombre.casefold() == nombre_buscar.casefold():
                    producto_encontrado = producto
            if producto_encontrado:
                cantidad = int(
                    input("Introduce la cantidad que quieres del producto: ")
                )
                if producto_encontrado.vender(cantidad):
                    nueva_Linea = LineaPedido(
                        producto_encontrado, producto_encontrado.precio, cantidad
                    )
                    aniadir_lineas_pedido(pedido, nueva_Linea)
                else:
                    print("Stock insuficiente")

        elif opcion == 3:
            detalles_pedido = mostrar_detalles(pedido)
            print(detalles_pedido)
        elif opcion == 4:
            total_pedido = pedido.total()
            print(f"Total a pagar por {pedido.cliente}: {total_pedido:.2f} EUR")


if __name__ == "__main__":
    main()
