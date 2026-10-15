def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

def aplicar_descuento(importe, porcentaje):
    descuento = importe - importe * porcentaje / 100
    return descuento