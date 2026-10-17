class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):

        hay_stock = False
        if cantidad <= 0 or cantidad > self.stock:
            return hay_stock
        else:
            self.stock -= cantidad
            hay_stock = True
            return hay_stock

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