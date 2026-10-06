precio = float(input("Introduce precio unitario: "))
cantidad = int(input("Introduce la cantidad: "))

subtotal = precio * cantidad

if cantidad < 5: 
    descuento = subtotal * 0/100
    total = subtotal - descuento
    print(total)
elif cantidad >= 5 and cantidad <= 9:
    descuento = subtotal * 5/100
    total = subtotal - descuento
    print(total)
elif cantidad >= 10:
    descuento = subtotal * 10/100
    total = subtotal - descuento
    print(total)

