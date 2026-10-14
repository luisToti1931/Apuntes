def leer_mensaje(mensaje, minimo, maximo):
    numero_valido = False
    numero = 0
    while not numero_valido:
        try:
            numero = int(input(mensaje))
            numero_valido = (minimo <= numero <= maximo)
            if not numero_valido:
                print(f"Tiene que estar entre {minimo} y {maximo}")
        except ValueError:
            print("Introduce un numero valido")
    return numero

resultado = leer_mensaje("Introduce un numero entre 1 y 100: ", 1, 100)
