class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario


class Comercial(Empleado):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_bonus(self):
        return self.ventas * 0.05

    def salario_mas_bonus(self):
        total = self.salario + self.calcular_bonus()
        return total
    def resumen(self):
        return (
            f"Comercial: {self.nombre}\n"
            f"Salario: {self.salario:.2f} EUR\n"
            f"Ventas: {self.ventas:.2f} EUR\n"
            f"Bonus (5%): {self.calcular_bonus():.2f} EUR\n"
            f"Salario + bonus: {self.salario_mas_bonus()} EUR"
        )

# ------------- main -----------

comercial = Comercial("Luis", 1500, 4000)
print(comercial.resumen())