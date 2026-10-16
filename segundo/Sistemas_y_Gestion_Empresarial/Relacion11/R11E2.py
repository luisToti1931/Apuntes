import csv
from pathlib import Path

ruta_csv = Path(__file__).with_name("clientes.csv")


def alta_cliente(lista, nombre, email, ciudad):
    if not nombre or not email or not ciudad:
        return "faltan_datos"
    if any(cliente["email"].casefold() == email.casefold() for cliente in lista):
        return "duplicado"

    lista.append({"nombre": nombre, "email": email, "ciudad": ciudad, "activo": True})
    return "aniadido"


def listarClientes(lista):
    if len(lista) >= 1:
        mensaje = ""
        for linea in lista:
            mensaje += f"Nombre: {linea['nombre']} | Email: {linea['email']} | Ciudad: {linea['ciudad']} | Activo: {linea['activo']}\n"
    else:
        mensaje = "Lista vacía"
    return mensaje


def buscar_por_texto(lista, texto):
    busqueda = texto.casefold()
    resultado = []
    for cliente in lista:
        if (
            busqueda in cliente["nombre"].casefold()
            or busqueda in cliente["email"].casefold()
            or busqueda in cliente["ciudad"].casefold()
        ):
            resultado.append(cliente)
    return resultado


def desactivar_cliente(lista, email):
    for cliente in lista:
        if cliente["email"].casefold() == email.casefold():
            cliente["activo"] = False
            return True
    return False


def guardar_csv(lista):
    with open(ruta_csv, "w", encoding="utf-8") as archivo:
        entrada = csv.DictWriter(
            archivo, fieldnames=["nombre", "email", "ciudad", "activo"]
        )
        entrada.writeheader()
        entrada.writerows(lista)
    return len(lista)


# -----------------MAIN-----------
def main():
    lista_clientes = []

    lista_clientes.append(
        {
            "nombre": "Capo",
            "email": "capo@gmail.com",
            "ciudad": "Granada",
            "activo": True,
        }
    )
    lista_clientes.append(
        {
            "nombre": "Migue",
            "email": "migue@gmail.com",
            "ciudad": "Almeria",
            "activo": False,
        }
    )
    lista_clientes.append(
        {"nombre": "Pepe", "email": "pepe@gmail.com", "ciudad": "Cenes", "activo": True}
    )

    opcion = 0
    while opcion != -1:
        print(
            "Op-1: Salir\nOp1: Alta\nOp2: Listado\nOp3: Busqueda por texto\nOp4: Desactivacion\nOp5: Guardado CSV"
        )
        opcion = int(input(f"Introduce una opcion: "))

        if opcion == 1:
            nombre = input(f"Introduce el nombre: ")
            email = input(f"Introduce el email: ")
            ciudad = input(f"Introduce la ciudad: ")
            resultado = alta_cliente(lista_clientes, nombre, email, ciudad)
            if resultado == "faltan_datos":
                print("Faltan datos")
            elif resultado == "duplicado":
                print(f"Mail ya añadido")
            else:
                print(f"Cliente añadido")

        if opcion == 2:
            print(listarClientes(lista_clientes))

        if opcion == 3:
            texto = input("Introduce el texto de busqueda: ").strip()
            encontrados = buscar_por_texto(lista_clientes, texto)

            if not encontrados:
                print("No se ha encontrado el cliente")
            else:
                for cliente in encontrados:
                    print(
                        f"{cliente['nombre']} | {cliente['email']} | {cliente['ciudad']} | Activo: {cliente['activo']}"
                    )

        if opcion == 4:
            email = input("Introduce el email: ").strip()

            if desactivar_cliente(lista_clientes, email):
                print("Cliente desactivado")
            else:
                print("Error al desactivar")

        if opcion == 5:
            guardar_csv(lista_clientes)
            print("Guardado en csv")


if __name__ == "__main__":
    main()
