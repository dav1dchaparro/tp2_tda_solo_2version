def resto(monedas, tabla, inicio, fin):
    if inicio > fin:
        return 0

    if monedas[inicio] >= monedas[fin]:
        inicio = inicio + 1
    else:
        fin = fin - 1

    if inicio > fin:
        return 0
    return tabla[inicio][fin]


def calcular(monedas):
    n = len(monedas)
    if n == 0:
        return [], []

    tabla = []
    eleccion = []
    for fila in range(n):
        tabla.append([0] * n)
        eleccion.append([""] * n)

    for largo in range(1, n + 1):
        for inicio in range(n - largo + 1):
            fin = inicio + largo - 1

            tomar_izq = monedas[inicio] + resto(monedas, tabla, inicio + 1, fin)
            tomar_der = monedas[fin] + resto(monedas, tabla, inicio, fin - 1)

            if tomar_izq >= tomar_der:
                tabla[inicio][fin] = tomar_izq
                eleccion[inicio][fin] = "izq"
            else:
                tabla[inicio][fin] = tomar_der
                eleccion[inicio][fin] = "der"

    return tabla, eleccion


def jugar(monedas, eleccion):
    inicio = 0
    fin = len(monedas) - 1
    turno_sophia = True
    jugadas = []

    while inicio <= fin:
        if turno_sophia:
            jugador = "Sophia"
            lado = eleccion[inicio][fin]
        else:
            jugador = "Mateo"
            if monedas[inicio] >= monedas[fin]:
                lado = "izq"
            else:
                lado = "der"

        if lado == "izq":
            jugadas.append((jugador, "primera", monedas[inicio]))
            inicio = inicio + 1
        else:
            jugadas.append((jugador, "ultima", monedas[fin]))
            fin = fin - 1

        turno_sophia = not turno_sophia

    return jugadas


