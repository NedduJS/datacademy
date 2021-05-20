def area(base, altura):
    return (base * altura) / 2


def run():
    base = float(input("Escribe la base: "))
    altura = float(input("Escribe la altura: "))
    s = area(base, altura)
    print(f"El área del triángulo es {s}")


if __name__ == "__main__":
    run()
