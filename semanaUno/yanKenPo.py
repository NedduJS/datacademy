import random


def rock_cases(election):
    result = 0
    if election == 2:
        result = 2
    elif election == 3:
        result = 1
    return result


def paper_cases(election):
    result = 0
    if election == 3:
        result = 2
    elif election == 1:
        result = 1
    return result


def scissors_cases(election):
    result = 0
    if election == 1:
        result = 2
    elif election == 2:
        result = 1
    return result


functions = {1: rock_cases, 2: paper_cases, 3: scissors_cases}


def compare(election1, election2):
    use = functions[election1]
    return use(election2)


def bot_election():
    return random.randint(1, 3)


def match_1j():
    j1_election = int(input("Escribe tu elección: "))
    bot = bot_election()
    return compare(j1_election, bot)


def match_2j():
    j1_election = int(input("J1 Escribe tu elección: "))
    j2_election = int(input("J2 Escribe tu elección: "))
    return compare(j1_election, j2_election)


def print_state(points1, points2, are_bot):
    if are_bot:
        print(f"J1 {points1}:{points2} IA")
        print("")
    else:
        print(f"J1 {points1}:{points2} J2")
        print("")


def run():
    print(
        """Bienvenido a Yan-Ken-Po
    Consigue 3 puntos para ganar
    Elije el modo de juego
    1J: Escribe 1
    2J: Escribe 2"""
    )
    game_mode = input(":")
    print("Escribe el número según...  1:piedra   2:papel   3:tijera")
    if game_mode == "1":
        j1_points = 0
        bot_points = 0
        while j1_points != 3 and bot_points != 3:
            result = match_1j()
            if result == 1:
                j1_points += 1
                print("Ganaste :)")
                print_state(j1_points, bot_points, True)
            elif result == 2:
                bot_points += 1
                print("La IA ganó")
                if bot_points == 2:
                    print("IA is dominating")
                print_state(j1_points, bot_points, True)
            else:
                print("Empate")
                print_state(j1_points, bot_points, True)
        winner = "IA ganó el juego" if bot_points == 3 else "Ganaste el juego"
        print(winner)
    else:
        j1_points = 0
        j2_points = 0
        while j1_points != 3 and j2_points != 3:
            result = match_2j()
            if result == 1:
                j1_points += 1
                print("J1 ganó")
                if j1_points == 2:
                    print("J2 is dominating")
                print_state(j1_points, j2_points, False)
            elif result == 2:
                j2_points += 1
                print("J2 ganó")
                if j2_points == 2:
                    print("J2 is dominating")
                print_state(j1_points, j2_points, False)
            else:
                print("Empate")
                print_state(j1_points, j2_points, False)
        winner = "J1 ganó el juego" if j1_points == 3 else "J2 ganó el juego"
        print(winner)


if __name__ == "__main__":
    run()
