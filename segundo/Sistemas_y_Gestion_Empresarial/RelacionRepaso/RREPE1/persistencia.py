import csv
from modelos import Reparacion, AsistenciaRemota

trabajos_csv = "trabajos.csv"


def cargar_trabajos():
    trabajos = {}

    try:
        with open(trabajos_csv, "r", encoding="utf-8") as archivos:
            lector = csv.DictReader(archivos)
            for linea in lector:
                tipo = linea["tipo"]
                codigo = linea["codigo"]
                cliente = linea["cliente"]
                horas = float(linea["horas"])
                estado = linea["estado"]
                if tipo == "Reparacion":
                    precio_pieza = (
                        float(linea["precio_pieza"]) if linea["precio_pieza"] else 0.0
                    )
                    trabajo = Reparacion(codigo, cliente, horas, estado, precio_pieza)

                else:
                    trabajo = AsistenciaRemota(codigo, cliente, horas, estado)
                trabajos[codigo] = trabajo
    except FileNotFoundError:
        pass
    return trabajos


def guardar_trabajos(trabajos):
    with open(trabajos_csv, "w", encoding="utf-8", newline="") as archivos:
        escritor = csv.DictWriter(archivos)
        escritor.writerow(["tipo", "codigo", "cliente", "horas", "estado", "precio_pieza"])
        for trabajo in trabajos.values():
            if isinstance(trabajo, Reparacion):
                tipo = "Reparacion"
                precio_pieza = trabajo.precio_pieza
            else:
                tipo = "AsistenciaRemota"
                precio_pieza = ""

            escritor.writerow([tipo, trabajo.codigo, trabajo.cliente, trabajo.horas, trabajo.estado, precio_pieza])