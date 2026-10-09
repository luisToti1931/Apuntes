total = 0

for dia in range(1, 8):
    ventas = float(input("Indica la cantidad de ventas del dia: "))
    total += ventas

    media = total / 7


    print(f"Total: {total:.2f} EUR \nMedia: {media:.2f} EUR ")