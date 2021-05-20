def milla_km(d):
    return d * 1.609


def km_milla(d):
    return d / 1.609


def run():
    print("Bienvenido al conversor de millas y kilómetros")
    tipo = input(
        """
  Elija el tipo de conversión
  1: millas a kilómetros
  2: kilómetros a millas
  --->
  """
    )
    valor = float(input("Ingrese la cantidad a convertir :"))
    if tipo == "1":
        valor = milla_km(valor)
        print(f"El resultado de la conversión es: {valor}km")
    elif tipo == "2":
        valor = km_milla(valor)
        print(f"El resultado de la conversión es: {valor} millas")
    else:
        print("Elección inválida")


if __name__ == "__main__":
    run()
