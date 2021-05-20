import math


def cilindro_volumen(h, r):
    return math.pi * (r ** 2) * h


def run():
    print("Calculador de volumen de un cilindro")
    altura = float(input("Escribe la altura en metros: "))
    radio = float(input("Escribe el radio en metros: "))
    volumen = round(cilindro_volumen(altura, radio), 2)
    litros = volumen * 1000
    print(f"El cilindro tiene un volumen de {volumen} metros cúbicos o {litros} litros")


if __name__ == "__main__":
    run()
