import sys
from dinamica import calcular, jugar


def leer_monedas(ruta):
    monedas = []
    with open(ruta) as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "" or linea.startswith("#"):
                continue
            linea = linea.replace(";", " ").replace(",", " ")
            for valor in linea.split():
                monedas.append(int(valor))
    return monedas


def mostrar(jugadas):
    total_sophia = 0
    total_mateo = 0

    for jugador, lado, valor in jugadas:
        print(jugador, "saca la", lado, "moneda:", valor)
        if jugador == "Sophia":
            total_sophia = total_sophia + valor
        else:
            total_mateo = total_mateo + valor

    print()
    print("Total Sophia:", total_sophia)
    print("Total Mateo:", total_mateo)

    if total_sophia > total_mateo:
        print("Gana Sophia")
    elif total_mateo > total_sophia:
        print("Gana Mateo")
    else:
        print("Empate")


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tp2.py ruta/a/listado-monedas.txt")
        sys.exit(1)

    monedas = leer_monedas(sys.argv[1])
    print("Monedas:", monedas)

    if not monedas:
        print("El archivo no tiene monedas")
        return

    tabla, eleccion = calcular(monedas)
    jugadas = jugar(monedas, eleccion)
    mostrar(jugadas)


if __name__ == "__main__":
    main()