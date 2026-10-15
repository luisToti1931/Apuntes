from calculos import calcular_subtotal, aplicar_descuento

def main():
    precio = float(input("Introduce precio: "))
    cantidad = int(input("Introduce una cantidad: "))
    descuento = int(input("Introduce el descuento (%): "))

    subtotal = calcular_subtotal(precio, cantidad)
    total = aplicar_descuento(subtotal, descuento)

    print(f"Precio sin descuento: {subtotal}")
    print(f"Precio con descuento: {total}")

if __name__ == "__main__":
    main()