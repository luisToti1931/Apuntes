def aplicar_descuento(importe, porcentaje=0):
    return importe * porcentaje / 100

sin_descuento = aplicar_descuento(100)
con_descuento = aplicar_descuento(100, 10)

print(f"{sin_descuento:.2f}\n{con_descuento:.2f}")