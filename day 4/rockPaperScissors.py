import random
import asciiArt

game = ["rock", "paper", "scissors"]
player = input("Rock, Paper, or Scissors? ") .lower()

if player not in game:
    print("Invalid Choice")

else:
    player = game.index(player)
    computer = random.randint(0, 2)

    command = f"{game[player].capitalize()} {asciiArt.art[player]}" "\n" f"{game[computer].capitalize()} {asciiArt.art[computer]}"
    if player == computer:
        print(command, "\nDraw")

    elif player == 0 and computer == 2:
        print(command, "\nWin")

    elif player == 1 and computer == 0:
        print(command, "\nWin")

    elif player == 2 and computer == 1:
        print(command, "\nWin")

    else:
        print(command, "\nLose")