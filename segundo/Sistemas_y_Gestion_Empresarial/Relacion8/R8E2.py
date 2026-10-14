def clasificar_stock (stock):
    if stock == 0:
        return "Agotado"
    elif stock <= 5:
        return "Stock bajo"
    else:
        return "Stock suficiente"


print(f"{clasificar_stock(0)}, {clasificar_stock(3)}, {clasificar_stock(10)}")