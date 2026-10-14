with open("cliente.txt", "w", encoding="utf-8") as archivo:
    cliente_max = 4
    cliente_min = 1
    for i in range(cliente_min,cliente_max):
        print(f"\n Cliente {i}")
        nombre = input("Introduce un nombre: ")
        ciudad = input("Introduce una ciudad: ")
        
        archivo.write(f"{nombre};{ciudad}\n")

with open("cliente.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())
