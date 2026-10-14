cliente = {
    "nombre": "Ana",
    "ciudad": "Granada",
    "email": "ana@example.com",
    "activo": True
}

cliente_anterior = cliente.copy()

cliente["ciudad"] = "Malaga"
cliente["telefono"] = "600000000"


print(f"{cliente_anterior}\n{cliente}")