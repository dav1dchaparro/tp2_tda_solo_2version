import random
from dinamica import calcular, jugar


def bruta(monedas):
    if len(monedas) == 0:
        return 0
    tomar_izq = monedas[0] + turno_mateo(monedas[1:])
    tomar_der = monedas[-1] + turno_mateo(monedas[:-1])
    return max(tomar_izq, tomar_der)


def turno_mateo(monedas):
    if len(monedas) == 0:
        return 0
    if monedas[0] >= monedas[-1]:
        return bruta(monedas[1:])
    return bruta(monedas[:-1])


def total_pd(monedas):
    if len(monedas) == 0:
        return 0
    tabla, eleccion = calcular(monedas)
    return tabla[0][len(monedas) - 1]


def suma_sophia(jugadas):
    total = 0
    for jugador, lado, valor in jugadas:
        if jugador == "Sophia":
            total = total + valor
    return total


def probar_bruta():
    random.seed(1)
    for prueba in range(500):
        n = random.randint(1, 12)
        monedas = []
        for k in range(n):
            monedas.append(random.randint(1, 20))
        assert total_pd(monedas) == bruta(monedas), monedas
    print("paso prueba: comparacion con fuerza bruta")


def probar_conocidos():
    assert total_pd([3, 9, 1, 2]) == 11
    assert total_pd([1, 10, 5]) == 6
    print("paso prueba: ejemplos conocidos")


def probar_bordes():
    assert total_pd([7]) == 7
    assert total_pd([4, 8]) == 8
    assert total_pd([8, 4]) == 8
    assert total_pd([5, 5, 5, 5]) == 10
    assert total_pd([5, 5, 5]) == 10
    assert total_pd([]) == 0
    print("paso prueba: casos borde")


def probar_jugar():
    random.seed(2)
    for prueba in range(500):
        n = random.randint(1, 12)
        monedas = []
        for k in range(n):
            monedas.append(random.randint(1, 20))
        tabla, eleccion = calcular(monedas)
        jugadas = jugar(monedas, eleccion)
        assert len(jugadas) == n, monedas
        assert suma_sophia(jugadas) == tabla[0][n - 1], monedas
    print("paso prueba: consistencia de jugar")


def probar_empate():
    monedas = [100, 5, 9, 1, 5]
    tabla, eleccion = calcular(monedas)
    jugadas = jugar(monedas, eleccion)
    assert jugadas[1] == ("Mateo", "primera", 5)
    assert total_pd(monedas) == 110
    print("paso prueba: desempate de Mateo")


probar_bruta()
probar_conocidos()
probar_bordes()
probar_jugar()
probar_empate()
print("todas las pruebas pasaron")