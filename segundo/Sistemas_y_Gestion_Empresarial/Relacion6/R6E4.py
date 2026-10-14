opcion = -1

while opcion != 0:
    print("Elije: 1) Alta ficticia \n2) Consulta ficticia \n3) Informe ficticio \n0) Salir")
    opcion = int(input("Elije: "))

    if opcion == 1:
        print("Alta ficticia")
    elif opcion == 2:
        print("Consulta ficticia")
    elif opcion == 3:
        print("Informe ficticio")
    elif opcion != 0:
        print("Opción no válida")
