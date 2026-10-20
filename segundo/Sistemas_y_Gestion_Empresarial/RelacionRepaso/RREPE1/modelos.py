class Trabajo:
    def __init__(self, codigo, cliente, horas, estado):
        self.codigo = codigo
        self.cliente = cliente
        self.horas = horas
        self.estado = estado

        def control_estados(self, estado_nuevo):
            if self.estado == "pendiente" and estado_nuevo == "en curso":
                self.estado = estado_nuevo
            elif self.estado == "en curso" and estado_nuevo == "finalizado":
                self.estado = estado_nuevo
            else:
                raise ValueError("Error en la transición")
            


class Reparacion(Trabajo):
    def __init__(self, codigo, cliente, horas, estado, precio_pieza):
        super().__init__(codigo, cliente, horas, estado)
        self.precio_pieza = precio_pieza

    def calcular_importe(self):
        total = (self.horas * 25) + self.precio_pieza
        return total


class AsistenciaRemota(Trabajo):
    def __init__(self, codigo, cliente, horas, estado):
        super().__init__(codigo, cliente, horas, estado)

        def calcular_importe(self):
            total = self.horas * 20
            return total
