listaPrecios = [40, 15, 2.5, 9, 5]

lineas = []

for precio in listaPrecios:
    lineas.append(f"{precio:.2f} EUR")


cantidad = len(listaPrecios)
suma = sum(listaPrecios)
minimo = min(listaPrecios)
maximo = max(listaPrecios)
media = suma/cantidad

lineas.append(f"Cantidad: {cantidad}")
lineas.append(f"Suma: {suma:.2f} EUR")
lineas.append(f"Mínimo: {minimo:.2f} EUR")
lineas.append(f"Máximo: {maximo:.2f} EUR")
lineas.append(f"Media: {media:.2f} EUR")

print("\n".join(lineas))