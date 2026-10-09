# dinamica.py

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
        return 0

    tabla = []
    for fila in range(n):
        tabla.append([0] * n)

    for largo in range(1, n + 1):
        for inicio in range(n - largo + 1):
            fin = inicio + largo - 1

            tomar_izq = monedas[inicio] + resto(monedas, tabla, inicio + 1, fin)
            tomar_der = monedas[fin] + resto(monedas, tabla, inicio, fin - 1)

            if tomar_izq >= tomar_der:
                tabla[inicio][fin] = tomar_izq
            else:
                tabla[inicio][fin] = tomar_der

    return tabla[0][n - 1]


print(calcular([3, 9, 1, 2]))  # 11
print(calcular([1, 10, 5]))    # 6