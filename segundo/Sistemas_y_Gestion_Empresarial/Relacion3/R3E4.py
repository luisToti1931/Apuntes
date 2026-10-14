destino = input("Introduce el destino (PENINSULA, BALEARES O CANARIAS): ").upper().strip()
pedido_total = float(input("Introduce el precio total del pedido: "))
gastos_envio = 0
total_pedido = 0
if destino == "PENINSULA":
    if total_pedido >= 100:
        gastos_envio = 0
    else:
        gastos_envio = 6
    total_final = total_pedido + gastos_envio
    print(f"Gastos de envío: {gastos_envio:.2f} EUR\nTotal final: {total_final:.2f} EUR")
elif destino == "BALEARES":
    gastos_envio = 12
    total_final = total_pedido + gastos_envio
    print(f"Gastos de envío: {gastos_envio:.2f} EUR\nTotal final: {total_final:.2f} EUR")
elif destino == "CANARIAS":
    gastos_envio = 18
    total_final = total_pedido + gastos_envio
    print(f"Gastos de envío: {gastos_envio:.2f} EUR\nTotal final: {total_final:.2f} EUR")
else:
    print("Destino no válido")
 