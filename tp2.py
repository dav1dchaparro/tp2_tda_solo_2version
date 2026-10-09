import sys


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


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tp2.py ruta/a/listado-monedas.txt")
        sys.exit(1)

    monedas = leer_monedas(sys.argv[1])
    print("Monedas:", monedas)


if __name__ == "__main__":
    main()
