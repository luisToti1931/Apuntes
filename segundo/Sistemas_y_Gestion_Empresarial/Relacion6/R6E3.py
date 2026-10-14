total = 0
importes = 0
contador = 0
importes = float(input("Introduzca cuantos importes se han registrado: "))

while importes != 0:
    total += importes
    contador += 1
    importes = float(input("Introduzca cuantos importes se han registrado: "))

print(f"Contador: {contador}\nTotal: {total:.2f}")
