class Cliente:
    def __init__(self, nombre, email, ciudad):
        self.nombre = nombre
        self.email = email
        self.ciudad = ciudad

    def cambiar_ciudad(self, nueva_ciudad):
        self.ciudad = nueva_ciudad

    def ficha(self):
        return f"{self.nombre} | {self.email} | {self.ciudad}"

    # --------------------- MAIN ----------------

cliente = Cliente("Ana", "a@gmail.com", "Granada")
print("Antes: ", cliente.ficha())
cliente.cambiar_ciudad("Sevilla")
print("Despues: ", cliente.ficha())
        