class LineaPedido:
    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.lineas = []

    def agregar_linea(self, linea):
        self.lineas.append(linea)

    def total(self):
        return sum(linea.subtotal() for linea in self.lineas)


# -------------- MAIN -------------

pedido = Pedido("Maria")
pedido.agregar_linea(LineaPedido("Raton", 15.50, 5))
pedido.agregar_linea(LineaPedido("Teclado", 80.00, 1))
pedido.agregar_linea(LineaPedido("Cable USB", 4.50, 3))

print(f"Pedido de {pedido.cliente}")
for linea in pedido.lineas:
    print(
        f"{linea.producto}: {linea.cantidad} x {linea.precio:.2f} = {linea.subtotal():.2f} EUR"
    )


print(f"Total: {pedido.total():.2f} EUR")

total_manual = 5 * 15.50 + 1 * 80.00 + 3 * 4.50

print(f"Coincide con la suma manual: {abs(pedido.total() - total_manual)}")
