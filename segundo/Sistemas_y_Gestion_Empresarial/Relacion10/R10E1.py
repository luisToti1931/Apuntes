class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(f"Nombre: {self.nombre}. Precio: {self.precio}.  Stock: {self.stock}")


# ------------------------ MAIN---------------

producto = Producto("Teclado", 15.95, 3)
producto.mostrar()