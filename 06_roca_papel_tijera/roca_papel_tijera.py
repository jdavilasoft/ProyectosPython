import random

juego = ["ROCA", "PAPEL", "TIJERA"]

play1, play2 = random.randint(0, 2), random.randint(0, 2)

if play1 == play2:
    print("EMPATE [ Jugador 1:", juego[play1], "Jugador 2:", juego[play2], "]")
elif play1 - play2 == 1:
    print("GANA Jugador 1:", juego[play1], "Jugador 2:", juego[play2], "]")
elif play2 - play1 == 1:
    print("GANA Jugador 2:", juego[play2], "Jugador 1:", juego[play1], "]")
elif play1 - play2 == 2:
    print("GANA Jugador 2:", juego[play2], "Jugador 1:", juego[play1], "]")
elif play2 - play1 == 2:
    print("GANA Jugador 1:", juego[play1], "Jugador 2:", juego[play2], "]")