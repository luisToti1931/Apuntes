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

    def reponer(self, cantidad):
        self.stock += cantidad

    def mostrar(self):
        print(f"Nombre: {self.nombre}. Precio: {self.precio}.  Stock: {self.stock}")

# ------------------------ MAIN---------------

producto = Producto("Teclado", 15.95, 3)

producto.mostrar()
producto.vender(2)
producto.mostrar()
producto.reponer(5)
producto.mostrar()