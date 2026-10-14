total = float(input("Introduce el precio total: "))
es_premium = input("¿El cliente es premium? (S/N): ").strip().upper()

if total > 500 or (es_premium == "S" and total > 250):
    print("El pedido es prioritario")
else:
    print("El pedido es normal")