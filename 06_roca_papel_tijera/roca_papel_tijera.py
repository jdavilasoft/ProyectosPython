import random

game = ["ROCK", "PAPER", "SCISSORS"]
play1, play2 = random.randint(0, 2), random.randint(0, 2)

if play1 == play2:
    print("DRAW [ Player 1:", game[play1], "= Player 2:", game[play2], "]")
elif play1 - play2 == 1 or play2 - play1 == 2:
    print("WIN Player 1:", game[play1], "Player 2:", game[play2])
elif play2 - play1 == 1 or play1 - play2 == 2:
    print("WIN Player 2:", game[play2], "Player 1:", game[play1])